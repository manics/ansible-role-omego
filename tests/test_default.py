import testinfra.utils.ansible_runner
import re
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.xfail(reason='omego version may return UNKNOWN')
def test_omego(Command):
    out = Command.check_output('/opt/omero/omego/bin/omego version')
    assert re.match('\d+\.\d+\.\d+', out)
