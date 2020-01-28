import pytest

try:
    from pytest_h5compare import assert_compare_info
except ImportError:
    pytestmark = pytest.mark.skipif(True, reason="Missing pytest_h5compare plugin.")


def test_Pos(compare_regex, make_anytest_record):
    failed, total = compare_regex(r".*Pos$", atol=1e-6, rtol=1e-8)
    
    for item in failed:
        make_anytest_record(item)
    make_anytest_record({"max_abs_err":1e-4})
    assert_compare_info(failed, total)


# def test_Vel(compare_regex, make_anytest_record):
#     failed, total = compare_regex(r".*Vel$", atol=1e-6, rtol=1e-8)
#     map(make_anytest_record, failed)
#     assert_compare_info(failed, total)
