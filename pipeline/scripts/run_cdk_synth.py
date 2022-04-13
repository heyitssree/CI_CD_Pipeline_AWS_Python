#!/usr/bin/env python
"""Script to run CDK synth for producing cloudformation template."""
import argparse
import os
import subprocess

from script_utils import get_path_for_directory


def main() -> None:
    """Invoke 'cdk synth' shell command."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, default='dev')
    os.chdir(get_path_for_directory("cdk"))
    subprocess.run(
        f'npx cdk synth --context env={parser.parse_args().env}',
        shell=True,
        stderr=subprocess.STDOUT,
        check=True
    )


if __name__ == "__main__":
    main()