# `andreygubarev.common.kubernetes`

# Example

https://raw.githubusercontent.com/istio/istio/master/samples/httpbin/httpbin.yaml

# Reference

## Cilium (Custom CNI)

- https://docs.k3s.io/networking/basic-network-options#custom-cni
- https://docs.cilium.io/en/stable/installation/k3s/
- https://docs.cilium.io/en/stable/installation/k8s-install-helm/

### Gateway API Support

- https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/gateway-api/
- https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/#kubeproxy-free

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/experimental-install.yaml
```
