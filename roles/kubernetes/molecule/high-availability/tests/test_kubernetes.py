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
    assert len(lines) == 3

    for line in lines:
        fields = line.split()
        assert len(fields) >= 5
        assert fields[1] == "Ready"


def test_kubernetes_api_server(host):
    """Validate Kubernetes API server is running."""
    cmd = host.run("k3s kubectl get componentstatuses")

    assert cmd.rc == 0
    lines = cmd.stdout.splitlines()[2:]  # Skip the header line

    for line in lines:
        fields = line.split()
        assert len(fields) >= 2
        assert fields[1] == "Healthy"


def test_kubernetes_namespaces(host):
    """Validate Kubernetes namespaces are correctly configured."""
    cmd = host.run("k3s kubectl get namespaces")

    assert cmd.rc == 0
    lines = cmd.stdout.splitlines()[1:]

    for line in lines:
        fields = line.split()
        assert len(fields) >= 2
        assert fields[1] == "Active"


def test_kubernetes_pods_running(host):
    """Validate all Kubernetes pods are running."""
    cmd = host.run("k3s kubectl get pods --all-namespaces")

    assert cmd.rc == 0
    lines = cmd.stdout.splitlines()[1:]  # Skip the header line

    for line in lines:
        fields = line.split()
        assert len(fields) >= 4
        assert fields[3] == "Running"


def test_kubernetes_services(host):
    """Validate Kubernetes services are correctly configured."""
    cmd = host.run("k3s kubectl get services --all-namespaces")

    assert cmd.rc == 0
    lines = cmd.stdout.splitlines()[1:]  # Skip the header line

    for line in lines:
        fields = line.split()
        assert len(fields) >= 5
        assert fields[3] != "<none>"
