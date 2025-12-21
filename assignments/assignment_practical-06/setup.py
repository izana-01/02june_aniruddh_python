import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError:
        print("Command failed:", command)
        sys.exit(1)

def main():
    project_name = "myproject"
    app_name = "myapp"

    # 1
    print("Creating virtual environment...")
    run_command("python -m venv venv")

    # 2
    if os.name == "nt":
        activate = "venv\\Scripts\\activate"
    else:
        activate = "source venv/bin/activate"

    print("Installing Django and required packages...")
    run_command(
        f"{activate} && pip install django djangorestframework requests"
    )
    # 3
    print("Creating Django project...")
    run_command(f"{activate} && django-admin startproject {project_name}")

    os.chdir(project_name)

    # 4
    print("Creating Django app...")
    run_command(f"{activate} && python manage.py startapp {app_name}")

    print("Setup completed successfully.")
    print("Activate the virtual environment and run:")
    print("python manage.py runserver")

if __name__ == "__main__":
    main()
