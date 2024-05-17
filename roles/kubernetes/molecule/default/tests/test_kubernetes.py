"""Role testing files using testinfra."""

testinfra_hosts = ["instance-1"]


def test_kubeconfig_file(host):
    """Validate kubeconfig file."""
    f = host.file("/etc/rancher/k3s/k3s.yaml")

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


def test_kubectl_command(host):
    """Validate kubectl command."""
    cmd = host.run("k3s kubectl version")

    assert cmd.rc == 0
    assert "Client Version:" in cmd.stdout
    assert "Server Version:" in cmd.stdout


def test_kubernetes_nodes_ready(host):
    """Validate all Kubernetes nodes are in Ready state."""
    cmd = host.run("k3s kubectl get nodes")
    assert cmd.rc == 0

    lines = cmd.stdout.splitlines()[1:]
    assert len(lines) == 2

    for line in lines:
        fields = line.split()
        assert len(fields) >= 5
        assert fields[1] == "Ready"
