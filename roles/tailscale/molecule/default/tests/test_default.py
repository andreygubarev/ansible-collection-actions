"""Role testing files using testinfra."""


def test_tailscale_is_installed(host):
    """Check if tailscale is installed."""
    assert host.package("tailscale").is_installed
