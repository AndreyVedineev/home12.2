import pytest

from utils.dicts import get_val, datam, append_str


@pytest.mark.parametrize("collect, ky, result", [
    (datam, 'pps', 'mars'),
    (datam, 'aaa', 'git'),
    ([], 'pps', 'git')
])
def test_get_val(collect, ky, result):
    assert get_val(collect, ky) == result


@pytest.fixture
def date_fixture():
    return ['AAA', 'BBB', 'CCC']


def test_append_str(date_fixture):
    assert append_str(date_fixture, 'DDD') == ['AAA', 'BBB', 'CCC', 'DDD']

def test_append_str(date_fixture):
    assert append_str(date_fixture, 5) == ['AAA', 'BBB', 'CCC']