import pytest

try:
    from pytest_h5compare import assert_compare_info
except ImportError:
    pytestmark = pytest.mark.skipif(True, reason="Missing pytest_h5compare plugin.")


def test_Pos(compare_regex):
    failed, total = compare_regex(r".*Pos$", atol=1e-6, rtol=1e-8)
    assert_compare_info(failed, total)
