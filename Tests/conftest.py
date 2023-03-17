import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )
    parser.addoption(
        "--xfail-all",
        action="store_true",
        default=False,
        help="Mark all tests with xfail",
    )

def mark_all_tests_with_xfail(items):
    """Mark all tests with xfail"""
    xfail_marker = pytest.mark.xfail(
        reason="All tests are expected to fail", strict=True
    )
    for item in items:
        item.add_marker(xfail_marker)


def pytest_collection_modifyitems(config, items):

    if config.getoption("--xfail-all"):
        mark_all_tests_with_xfail(items)
    
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
