# Airflow

```bash
helm repo add airflow-stable https://airflow-helm.github.io/charts

argocd app set helm-guestbook --values values-production.yaml

## create the namespace
kubectl create ns "$AIRFLOW_NAMESPACE"

helm search repo airflow-stable/airflow

## install using helm 3
helm upgrade --cleanup-on-fail \
  --install airflow-cluster airflow-stable/airflow \
  --namespace af \
  --create-namespace \
  --version=8.6.0 \
  --timeout=15m \
  --dry-run \
  --debug \
  --values ./custom-values.yaml
```

## reference
- [airflow helm chart](https://github.com/airflow-helm/charts/tree/main/charts/airflow/examples/google-gke)
- [helm subchart](https://github.com/argoproj/argo-cd/issues/2789)
