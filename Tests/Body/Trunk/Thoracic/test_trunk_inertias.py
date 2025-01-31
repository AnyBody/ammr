from pathlib import Path
from itertools import product, groupby
from collections import ChainMap
from anypytools import AnyPyProcess, macro_commands as mc
from anypytools.abcutils import AnyPyProcessOutputList
from anypytools.tools import winepath, ON_WINDOWS

import pytest

ABS_TOL = 3 # we round off numbers from ams to 1e-3 which for masses is a 1gram precision
MODEL_FILE = "inertia_model.any"
AMS_VARIABLES = [
    "Main.test_variables.trunk_mass",
    "Main.test_variables.trunk_segments_masses",
]

DEFINES_COMBINATIONS = product(
    [
        {'BM_TRUNK_CAVITY_MODEL': 0}, # _CAVITY_MODEL_BUCKLE_
        {'BM_TRUNK_CAVITY_MODEL': 1} # _CAVITY_MODEL_VOLUME_
    ],
    [
        {'BM_TRUNK_THORACIC_MODEL': 0}, # _THORACIC_MODEL_RIGID_
        {'BM_TRUNK_THORACIC_MODEL': 1}, # _THORACIC_MODEL_FLEXIBLE_
    ],
    [
        {"TEST_NAME":"test_inertia_0"}, # set to indicate running from test framework
    ],
)

DEFINES = [dict(**ChainMap(*defs)) for defs in DEFINES_COMBINATIONS]


def all_equal(iterable) -> bool:
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def extract_output(output: AnyPyProcessOutputList) -> dict[str,list]:
    """ extract output variables from the model into a dict""" 
    formatted = {}
    for result in output:
        for var in AMS_VARIABLES:
            formatted.setdefault(var.split(".")[-1], []).append(result[var])
    
    return formatted    


def make_dump_commands(variables: list[str]) -> list[mc.MacroCommand]: 
    return [mc.Dump(var) for var in variables]


@pytest.fixture(scope="module")
def model_output() -> dict:
    """ run the models and provide the test output"""

    model = next(Path().rglob(MODEL_FILE)).resolve()

    if not ON_WINDOWS:
        model = winepath(model, "-w")

    macros = []
    for defs in DEFINES:
        macros.append(
            [
                mc.Load(model, defs=defs),
                *make_dump_commands(AMS_VARIABLES),
            ]
        )

    app = AnyPyProcess(
        num_processes=2,
        anybodycon_path= pytest.anytest.ams_path
    )

    results = app.start_macro(macros)
    for result, defs in zip(results, DEFINES):
        if 'ERROR' in result:
            pytest.fail(f"Model had erros:\n{result['ERROR']}\n, defs: {defs}")

    return extract_output(results)


def test_trunk_masses(model_output: AnyPyProcessOutputList):
    """ test the trunk region mass"""
    thorax_masses = model_output["trunk_mass"]
    
    thorax_masses = [round(mass, ABS_TOL) for mass in thorax_masses]
    assert all_equal(thorax_masses) 


@pytest.mark.skip("Not implemented")
def test_trunk_segment_masses(model_output: AnyPyProcessOutputList)  -> None:
    """ assert that the segment mass of each segment is equal across BM configs"""

    trunk_segments_masses = model_output["trunk_segments_masses"]
    rounded = []

    for trial in trunk_segments_masses:
        rounded.append([round(segment_mass, ABS_TOL) for segment_mass in trial])
    
    for trial in rounded:
        for idx, _ in enumerate(trial):
            masses = [t[idx] for t in rounded]
            assert(all_equal(masses))
