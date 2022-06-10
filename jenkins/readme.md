kubectl apply -f jenkins-pvc.yaml

kubectl apply -f jenkins-sa.yaml

https://www.jenkins.io/doc/book/installing/kubernetes/#configure-helm

https://artifacthub.io/packages/helm/jenkinsci/jenkins

helm upgrade --cleanup-on-fail \
--install jenkins jenkinsci/jenkins \
--namespace jenkins \
--create-namespace \
--version=1.2.0 \
--timeout=15m \
--values jenkins-helm-values.yaml \
--dry-run \
--debug