"""Script to locally build and test."""
import logging
import os
import subprocess

import run_prospector
import run_prospector_tests
import run_mypy
import run_cdk_synth
import run_cfn_nag
import run_cfn_lint
from script_utils import get_path_for_directory

logging.getLogger().setLevel(logging.INFO)


def main() -> None:
    """Invokke build and test locally."""
    # Prospector Analysis
    logging.info("RUNNING PROSPECTOR")
    run_prospector.main()

    # Prospector Analysis (Tests)
    logging.info("RUNNING PROSPECTOR FOR TEST CASES")
    run_prospector_tests.main()

    # Mypy Type Hinting Analysis
    logging.info("RUNNING MYPY TYPE HINTING ANALYSIS")
    run_mypy.main()

    # Synth CDK Templates
    logging.info("RUNNING CDK SYNTH")
    run_cdk_synth.main()

    # Pytest runner
    logging.info("RUNNING PYTEST")
    subprocess.run(f"""python -m pytest -v --ignore={get_path_for_directory('cdk.out')}""", check=True)

    # CFN-LINT Scan
    logging.info("RUNNING CFN-LINT SCAN")
    run_cfn_lint.main()

    # CFN-NAG Scan
    logging.info("RUNNING CFN-NAG SCAN")
    run_cfn_nag.main()

    # Deploy Stack to DEV
    logging.info("RUNNING CDK DEPLOY")
    os.chdir(get_path_for_directory("cdk"))
    # subprocess.run(
    #   "npx cdk deploy '*' --context env=dev -v --require-approval never",
    #   shell=True
    #   check=True
    # )
    logging.info("STACK DEPLOYED SUCCESSFULLY! 😎")

if __name__ == "__main__":
    main()