"""Script to run cfn lint  checks."""
import subprocess

from script_utils import get_path_for_directory


def main() -> None:
    """Invoke 'cfn-lint' shell commandd."""
    path_to_cft = get_path_for_directory("cdk.out")
    subprocess.run(f"""cfn-lint --verbose {path_to_cft}/*template.json --ignore-checks W""", shell=True, check=True)


if __name__ == "__main__":
    main()