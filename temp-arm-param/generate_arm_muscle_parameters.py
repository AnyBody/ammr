# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:32:24 2016

@author: melund
"""
import os
from pathlib import Path

import click
import pandas as pd

import jinja2


def _read_xl_file(fname):

    df = pd.read_excel(fname)
    df.fillna(False, inplace=True)

    rows = df.iterrows()
    i, descriptions = next(rows)
    muscles = dict()

    for x, row in rows:
        rowdata = dict()
        musclename = row["AMS muscle name"]
        if not isinstance(musclename, str):
            continue
        for param, value in row.iteritems():
            rowdata[param] = value

        muscles[musclename] = rowdata
    return muscles


env = jinja2.Environment(loader=jinja2.FileSystemLoader(Path(__file__).parent))


def _create_from_template(output, data):
    output = Path(output)
    t = env.get_template(output.with_suffix(".jinja.any").name)
    with open(output, "w") as fh:
        fh.write(t.render(muscles=data))


@click.command()
@click.option(
    "--ammr",
    default=Path(__file__).parent.parent,
    prompt="AMMR path to add files",
    type=click.Path(exists=True),
    help="AMMR paths.",
)
def create_arm_parameter_files(ammr):
    ammr = Path(ammr)
    files = [
        ammr / "Body/AAUHuman/Arm/ArmData1.1/ArmModelMuscleParameters.any",
        ammr / "Body/AAUHuman/Arm/Muscle-parameters-shoulder.any",
        ammr / "Body/AAUHuman/Arm/Muscle-parameters-shoulder-simple.any",
    ]

    if not all(fp.exists() for fp in files):
        click.echo(f"This does not look like an AMMR: {ammr}")
        click.echo("Creating files locally")
        files = [fp.name for fp in files]

    data = _read_xl_file(Path(__file__).with_name("arm-muscle-parameter.xlsx"))

    for fpath in files:
        click.echo(f"Creating file: {fpath}")
        _create_from_template(fpath, data)


if __name__ == "__main__":
    create_arm_parameter_files()
