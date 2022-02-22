import os

from _pytest.config import Config, PytestPluginManager

from pytest_squadcast.squadcast import Squadcast


def test_squadcast():
    PytestPluginManager()
    config = Config(PytestPluginManager())
    obj = Squadcast(config)
    exitstatus = 0
    if config.hook.pytest_squadcast_send_alert(exitstatus=exitstatus):
        obj.send_incident(session, exitstatus)
