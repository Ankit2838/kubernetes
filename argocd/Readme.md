```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm install test-argocd argo/argo-cd -f values.yaml -n test