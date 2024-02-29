import re

from pathlib import Path

from jinja2 import Template

try:
    import tomllib
except ImportError:
    import tomli as tomllib


tmplpath = Path(__file__).parent.absolute()

rootpath = tmplpath.parents[2]

with open(rootpath / "Body/AAUHuman/bm-parameters.toml", "rb") as fh:
    data = tomllib.load(fh)


def filterp(match):
    prog = re.compile(match)
    return {k: v for k, v in data["parameters"].items() if prog.match(k)}


bm_all = filterp(".*")
bm_leg = filterp("^BM_LEG")
bm_trunk = filterp("^BM_TRUNK")
bm_arm = filterp("^BM_ARM")
bm_scaling = filterp("^BM_SCALING")
bm_mannequin = filterp("^BM_MANNEQUIN_DRIVER")
bm_jointtype = filterp("^BM_JOINT_TYPE")

used_param = set().union(
    *[bm_leg, bm_trunk, bm_arm, bm_scaling, bm_mannequin, bm_jointtype]
)

bm_other = {k: bm_all[k] for k in sorted(set(bm_all) - used_param)}


targets = [
    ("Docs/bm_config/bm_constants.md", None, data),
    ("Docs/bm_config/bm_statements.md", None, data),
    ("Docs/bm_config/LegTable.csv", "bmtable.csv.jinja", bm_leg),
    ("Docs/bm_config/TrunkTable.csv", "bmtable.csv.jinja", bm_trunk),
    ("Docs/bm_config/ArmTable.csv", "bmtable.csv.jinja", bm_arm),
    ("Docs/bm_config/ScalingTable.csv", "bmtable.csv.jinja", bm_scaling),
    ("Docs/bm_config/MannequinTable.csv", "bmtable.csv.jinja", bm_mannequin),
    ("Docs/bm_config/JointTypeTable.csv", "bmtable.csv.jinja", bm_jointtype),
    ("Docs/bm_config/OtherTable.csv", "bmtable.csv.jinja", bm_other),
    ("Body/AAUHuman/BodyModels/GenericBodyModel/Ifdef_BM_param.any", None, data),
    ("Body/AAUHuman/BodyModels/GenericBodyModel/BodyModel.constants.any", None, data),
    ("Body/AAUHuman/BodyModels/GenericBodyModel/BodyModel.defaults.any", None, data),
    ("Body/AAUHuman/Documentation/BodyModel.parameters.any", None, data),
    ("Body/AAUHuman/BodyModels/GenericBodyModel/BodyModel.config_info.any", None, data),
    ("Body/AAUHuman/Documentation/bm_constants.py", None, data),
    ("Body/AAUHuman/BodyModels/GenericBodyModel/undef_BM_params.any", None, data),
]


for target, template, data in targets:
    target = rootpath / target
    if not template:
        template = target.name + ".jinja"
    template = tmplpath / template
    with open(template) as fh:
        tmpl = Template(fh.read())
    with open(target, "w") as fh:
        fh.write(tmpl.render(data=data))
