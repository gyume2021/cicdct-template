# airflow

## 
argocd app set helm-guestbook --values values-production.yaml

## create the namespace
kubectl create ns "$AIRFLOW_NAMESPACE"

helm search repo airflow-stable/airflow

## install using helm 3
helm install \
  airflow-cluster airflow-stable/airflow \
  --namespace argocd-production \
  --version "8.6.0" \
  --timeout 30m \
  --values ./custom-values.yaml


- [airflow helm chart](https://github.com/airflow-helm/charts/tree/main/charts/airflow)
