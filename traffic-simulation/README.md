# Get started

```bash
virtualenv stream-simulation
source stream-simulation/bin/activate
pip install --upgrade google-cloud-pubsub
python send_sensor_data.py --speedFactor=1 --project=$PROJECT_ID
```

# reference
- [pubsub](https://cloud.google.com/pubsub/docs/reference/libraries#create-service-account-console)
