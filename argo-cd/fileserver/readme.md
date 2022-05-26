# HTTP Fileserver

```bash
$ kubectl create ns fileserver
kubectl label ns debug istio-injection=enabled
$ kubectl apply -f k8s

zone name: e2eelab-org	
dns name:  e2eelab.org.

gcloud dns --project=helical-realm-307202 record-sets transaction start --zone="e2eelab-org"
gcloud dns --project=helical-realm-307202 record-sets transaction add 34.80.170.9 --name="debug.e2eelab.org." --ttl="300" --type="A" --zone="e2eelab-org"
gcloud dns --project=helical-realm-307202 record-sets transaction remove 34.80.170.9 --name="debug.e2eelab.org." --ttl="300" --type="A" --zone="e2eelab-org"
gcloud dns --project=helical-realm-307202 record-sets transaction execute --zone="e2eelab-org"

# enter the server
$ kubectl exec -it $(kubectl get pod -n fileserver -o name) -n fileserver -- sh
```

## upload file

The document root in fileserver is
    /usr/share/nginx/html
```bash
$ export pod_id=$(kubectl get pod --selector="service=http-fileserver" -n fileserver -o jsonpath='{.items[0].metadata.name}')
$ kubectl cp test-image.png fileserver/$(pod_id):/usr/share/nginx/html/test/test-image.png -c http-fileserver
$ kubectl cp <local file> fileserver/$(pod_id):/usr/share/nginx/html/test/<target file> -c http-fileserver
```

## download file

```bash
curl https://file.e2eelab.org/test-image.png --output download.png
curl https://file.e2eelab.org/<target file> --output <downloaded file>
```

## configuration

```bash
cat /etc/nginx/nginx.conf
```

## reference
- [kubernetes HTTP Fileserver](https://github.com/mpolinowski/http-fileserver-kubernetes)
- [nginx server setting](https://www.maxlist.xyz/2020/06/18/flask-nginx/)
- [nginx tutorial](https://www.huaweicloud.com/articles/19a73f3d65f52df15849a06e57eeffb5.html)
- [nginx-upload-module](https://www.nginx.com/resources/wiki/modules/upload/)