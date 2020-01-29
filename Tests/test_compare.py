import pytest

try:
    from pytest_h5compare import assert_compare_info
except ImportError:
    pytestmark = pytest.mark.skipif(True, reason="Missing pytest_h5compare plugin.")


def test_Base(compare_regex, make_anytest_record):
    pattern = r"Output:()|(Epot)|(Ekin)|(Emech)|(Pmech)|(MaxMuscleActivity)"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Pos(compare_regex, make_anytest_record):
    pattern = r"Output/.*((/r$)|(/Axes$)|(/sRel$)|(Pos$))"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Vel(compare_regex, make_anytest_record):
    pattern = r"Output/.*((/rDot$)|(/omega$)|(Vel$))"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Acc(compare_regex, make_anytest_record):
    pattern = r"Output/.*((/rDDot$)|(/omegaDot$)|(Acc$))"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Fin(compare_regex, make_anytest_record):
    pattern = r"Output/.*((/Fin$))"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Fout(compare_regex, make_anytest_record):
    pattern = r"Output/.*((/Fout$))"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Activity(compare_regex, make_anytest_record):
    pattern = r"Output/.*((/Activity$))"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Muscles(compare_regex, make_anytest_record):
    pattern = (
        r"Output/.*((/Activity$)|(/CorrectedActivity$)|(/Fm$)|(/Ft$)"
        r"|(/Fp$)|(/Strength$)|(/Ft0$)|(/Ft0Grad$)|(/PennationAngle$)"
        r"|(/EPOTt$)|(/EPOTp$)|(/EPOTmt$)|(/Pt$)|(/Pm$)|(/Pmet$))"
    )
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_Contact(compare_regex, make_anytest_record):
    pattern = (
        r"Output/.*((/Fmaster$)|(/Fslave$)|(/Mmaster$)|(/Mslave$)"
        r"|(/MCOP$)|(/COP$)|(/ContactArea$)|(/MaxPenetration$))"
    )
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)


def test_SelOut(compare_regex, make_anytest_record):
    pattern = r"Output/.*?/SelectedOutput/.*"
    failed, total = compare_regex(pattern, atol=1e-6, rtol=1e-8)
    for item in failed:
        make_anytest_record(item)
    assert_compare_info(failed, total)

