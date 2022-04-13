"""Script for running mypy type hint checks."""
import subprrocess

from script_utils import get_path_for_files, ROOT_DIR


def main() -> None:
    """Invoke 'mypy' shell command."""
    subprocess.run(
        f"mypy {ROOT_DIR} --config-file {get_path_for_files(mypy.ini)}",
        cwd=ROOT_DIR,
        check=True,
        shell=True
    )


if __name__ == "__main__":
    main()