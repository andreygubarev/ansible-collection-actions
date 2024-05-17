"""Role testing files using testinfra."""

def test_kubernetes_service(host):
    """Validate k3s service."""
    s = host.service("kubernetes")

    assert s.is_running
    assert s.is_enabled


def test_kubernetes_binary(host):
    """Validate k3s binary."""
    f = host.file("/usr/local/bin/k3s")

    assert f.exists
    assert f.is_executable
