## reference

helm install my-release spark-operator/spark-operator --namespace spark-operator --create-namespace

helm upgrade --cleanup-on-fail \
  --install spark-cluster spark-operator/spark-operator \
  --namespace spark-operator \
  --create-namespace \
  --version=1.1.25 \
  --timeout=15m \
  --dry-run \
  --debug \
  --values ./custom-values.yaml



- [spark operator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator)