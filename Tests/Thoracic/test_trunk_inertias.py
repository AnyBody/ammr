from pathlib import Path
from itertools import product, groupby
from anypytools import AnyPyProcess, macro_commands as mc
import pytest

def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def test_inertia_properties():
    defs = {"TEST_NAME":"test_inertia_0"}
    model = next(Path().rglob("inertia_model.any")).resolve()

    defines = product(
        [
            {'BM_TRUNK_CAVITY_MODEL': 0}, # _CAVITY_MODEL_BUCKLE_
            {'BM_TRUNK_CAVITY_MODEL': 1} # _CAVITY_MODEL_VOLUME_
        ],
        [
            {'BM_TRUNK_THORACIC_MODEL': 0}, # _THORACIC_MODEL_RIGID_
            {'BM_TRUNK_THORACIC_MODEL': 1}, # _THORACIC_MODEL_FLEXIBLE_
        ],
    )

    macros = []
    for cavitymodel, thoracicmodel in defines:
        defs.update(cavitymodel)
        defs.update(thoracicmodel)
        macros.append([
            mc.Load(model, defs=defs),
            mc.OperationRun("Main.RunTest"),
            mc.Dump("Main.test_variables.thorax_mass"),
            mc.Dump("Main.test_variables.trunk_segments_masses"),
        ])

    app = AnyPyProcess(
        num_processes=2,
        anybodycon_path= pytest.anytest.ams_path
    )
    results = app.start_macro(macros)

    thorax_masses = []
    trunk_segment_masses = []
    for trial in results:
        thorax_masses.append(trial["thorax_mass"])
        trunk_segment_masses.append(trial["trunk_segments_masses"])

    # We use round to allow numerical differences
    # the test compares with 1g tolerance (i.e. 1e-3)
    thorax_masses = [round(m, 3) for m in thorax_masses]
    for trial in trunk_segment_masses:
        [round(m, 3) for m in trial]

    assert all_equal(thorax_masses)

    
    for idx in range(len(trunk_segment_masses[0])):
        assert([t[idx] for t in trunk_segment_masses])

    