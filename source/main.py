import utils
import os
from render.interface import create_repo


def main():
    set_up = ask_all_questions()
    os.mkdir(set_up["name"])
    create_repo(set_up)


# Create and run Bash
    # Create project folder
    # Create Venv
    # Install flake8
    # Install pytest
    # Create requirements.txt
    # Initialise git
    # Install pytest watch
    # Install precommit hooks
# Create README
# Create gitignore


def ask_all_questions():

    project_name = utils.ask_question("name:")
    venv = utils.ask_yes_no_question("Initialise a virtual environment?")
    flake = utils.ask_yes_no_question("Do you want flake8 linting enabled?")
    pytest = utils.ask_yes_no_question("Do you want pytest to be installed?")
    git = utils.ask_yes_no_question("Do you want to initialise a git repo?")
    readme = utils.ask_yes_no_question("Do you want to initialise a README?")

    return {
        "name": project_name,
        "venv": venv,
        "flake": flake,
        "pytest": pytest,
        "readme": readme,
        "git": git
    }


if __name__ == "__main__":
    main()
