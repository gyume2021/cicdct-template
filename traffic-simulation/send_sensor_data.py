#!/usr/bin/env python3

import time
import gzip
import logging
import argparse
import datetime
from google.cloud import pubsub_v1

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
TOPIC = 'your-topic-id'
INPUT = 'sensor_obs2008.csv.gz'

def publish(publisher, topic, events):
   numobs = len(events)
   if numobs > 0:
      logging.info('Publishing {0} events from {1}'.format(numobs, get_timestamp(events[0])))
      for event_data in events:
         publisher.publish(topic,event_data)

def get_timestamp(line):
   ## convert from bytes to str
   line = line.decode('utf-8')

   # look at first field of row
   timestamp = line.split(',')[0]
   return datetime.datetime.strptime(timestamp, TIME_FORMAT)

def simulate(topic, ifp, firstObsTime, programStart, speedFactor):
   # sleep computation
   def compute_sleep_secs(obs_time):
      time_elapsed = (datetime.datetime.utcnow() - programStart).seconds
      sim_time_elapsed = ((obs_time - firstObsTime).days * 86400.0 + (obs_time - firstObsTime).seconds) / speedFactor
      to_sleep_secs = sim_time_elapsed - time_elapsed
      return to_sleep_secs

   topublish = list() 

   for line in ifp:
      event_data = line   # entire line of input CSV is the message
      obs_time = get_timestamp(line) # from first column

      # how much time should we sleep?
      if compute_sleep_secs(obs_time) > 1:
         # notify the accumulated topublish
         publish(publisher, topic, topublish) # notify accumulated messages
         topublish = list() # empty out list

         # recompute sleep, since notification takes a while
         to_sleep_secs = compute_sleep_secs(obs_time)
         if to_sleep_secs > 0:
            logging.info('Sleeping {} seconds'.format(to_sleep_secs))
            time.sleep(to_sleep_secs)
      topublish.append(event_data)

   # left-over records; notify again
   publish(publisher, topic, topublish)

def peek_timestamp(ifp):
   # peek ahead to next line, get timestamp and go back
   pos = ifp.tell()
   line = ifp.readline()
   ifp.seek(pos)
   return get_timestamp(line)

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Send sensor data to Cloud Pub/Sub in small groups, simulating real-time behavior')
   parser.add_argument('--speedFactor', help='Example: 60 implies 1 hour of data sent to Cloud Pub/Sub in 1 minute', required=True, type=float)
   parser.add_argument('--project', help='Example: --project $DEVSHELL_PROJECT_ID', required=True)
   args = parser.parse_args()

   # create Pub/Sub notification topic
   logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
   publisher = pubsub_v1.PublisherClient()
   event_type = publisher.topic_path(args.project,TOPIC)

   # Initialize request argument(s)
   request = pubsub_v1.types.GetTopicRequest(
      topic=event_type   
   )

   try:
      # get topic
      publisher.get_topic(request)
      logging.info('Reusing pub/sub topic {}'.format(TOPIC))
   except:
      # create topic
      publisher.create_topic(request={"name": event_type})
      logging.info('Creating pub/sub topic {}'.format(TOPIC))

   # notify about each line in the input file
   programStartTime = datetime.datetime.utcnow() 
   with gzip.open(INPUT, 'rb') as ifp:
      header = ifp.readline()  # skip header
      firstObsTime = peek_timestamp(ifp)
      logging.info('Sending sensor data from {}'.format(firstObsTime))
      logging.info('programStartTime: {}'.format(programStartTime))
      simulate(event_type, ifp, firstObsTime, programStartTime, args.speedFactor)
