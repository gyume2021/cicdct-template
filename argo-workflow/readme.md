# install argo-workflow
```bash
kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/quick-start-postgres.yaml
kubectl -n argo port-forward deployment/argo-server 2746:2746
```

# install artifact
```bash
helm repo add minio https://helm.min.io/ 
helm repo update
helm install argo-artifacts minio/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts
kubectl  port-forward deployment/argo-artifacts 9000:9000
```

- [argo workflow](https://github.com/argoproj/argo-workflows/blob/master/docs/quick-start.md)
- [minio artifactory](https://github.com/argoproj/argo-workflows/blob/master/docs/configure-artifact-repository.md)