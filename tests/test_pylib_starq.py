
from click.testing import CliRunner

from pylib_starq import longest
from pylib_starq.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
