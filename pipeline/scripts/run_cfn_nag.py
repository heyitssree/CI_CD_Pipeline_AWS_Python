"""Scripts for running cfn_nag security checks."""
import subprocess
from configparser import ConfigParser, ExtendedInterpolation

from script_utils import get_path_for_directory, get_path_for_file

def main() -> None:
    """Invoke 'cfn_nag_scan' shell command."""
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(get_path_for_file('config.ini'))

    path_to_stacks = get_path_for_directory('cdk.out')
    template_file = f"""{config['global']['app-id']}.template.json"""
    subprocess.run(
        f"""cfn_nag_scan --input-path {path_to_stacks}/{template_file} """
        f"""--blacklist-path {get_path_for_file('.cfnnagrc')}""",
        shell=True,
        check=True
    )


if __name__ == "__main__":
    main()