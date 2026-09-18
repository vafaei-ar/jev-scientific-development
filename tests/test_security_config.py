from pathlib import Path

import pytest

from jev_research.config import JevConfig
from jev_research.mcp.server import _validate_bind_host


@pytest.mark.parametrize("host", ["127.0.0.1", "localhost", "::1"])
def test_loopback_hosts_are_allowed(host: str) -> None:
    _validate_bind_host(host)


@pytest.mark.parametrize("host", ["0.0.0.0", "192.168.1.10", "example.com"])
def test_remote_bind_is_rejected(host: str) -> None:
    with pytest.raises(RuntimeError, match="refuses non-loopback"):
        _validate_bind_host(host)


def test_config_loads_dotenv_from_working_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("TYPESAFE_API_KEY", raising=False)
    monkeypatch.delenv("JEV_API_KEY", raising=False)
    (tmp_path / ".env").write_text("TYPESAFE_API_KEY=from-dotenv\nJEV_MODEL=jev-test\n")

    config = JevConfig.from_env()

    assert config.api_key == "from-dotenv"
    assert config.model == "jev-test"
