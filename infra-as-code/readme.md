# Crossplane

## Install Crossplane
```bash
kubectl create namespace crossplane-system
helm repo add crossplane-stable https://charts.crossplane.io/stable
helm repo update
helm search repo crossplane-stable/crossplane --versions
helm upgrade --cleanup-on-fail \
  --install crossplane crossplane-stable/crossplane \
  --namespace crossplane-system \
  --create-namespace \
  --version=1.7.0 \
  --timeout=15m
```

## Check Crossplane Status
```bash
helm list -n crossplane-system
kubectl get all -n crossplane-system
```

## Install Crossplane CLI
```bash
curl -sL https://raw.githubusercontent.com/crossplane/crossplane/master/install.sh | sh
sudo mv kubectl-crossplane ~/.local/bin
kubectl crossplane --help
```

## Install Custom Resource for GCP
```bash
kubectl crossplane install configuration registry.upbound.io/xp/getting-started-with-gcp:v1.7.0
watch kubectl get pkg # Wait until all packages become healthy
```

## Get GCP Account Keyfile
```bash
PROJECT_ID=<my-project>
NEW_SA_NAME=<test-service-account-name>

# create service account
SA="${NEW_SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
gcloud iam service-accounts create $NEW_SA_NAME --project $PROJECT_ID

# enable cloud API
SERVICE="sqladmin.googleapis.com"
gcloud services enable $SERVICE --project $PROJECT_ID

# grant access to cloud API
ROLE="roles/cloudsql.admin"
gcloud projects add-iam-policy-binding --role="$ROLE" $PROJECT_ID --member "serviceAccount:$SA"

# create service account keyfile
gcloud iam service-accounts keys create creds.json --project $PROJECT_ID --iam-account $SA
```

## Create a Provider Secret
```bash
kubectl create secret generic gcp-creds -n crossplane-system --from-file=creds=./cred.json
```

## Uninstalling the Chart
```bash
helm delete crossplane --namespace crossplane-system
```

## [Adding Google Cloud Platform to Crossplane](https://crossplane.io/docs/v1.7/cloud-providers/gcp/gcp-provider.html)