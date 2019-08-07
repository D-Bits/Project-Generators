from subprocess import call
from os import chdir, mkdir


def create_root():

    dir_name = input("Enter a name for the project base dir: ")

    mkdir(dir_name)
    chdir(dir_name)

    """Create virtualenv w/ Pipenv, and install packages"""
    # Make sure pip is up-to-date
    call(['python', '-m', 'pip', 'install', '--upgrade pip'])
    # Install pipenv, if it is not already installed
    call(['pip', 'install', 'pipenv'])
    call(['pipenv', 'install', 'django'])

    # Ask the user if they also want to install DRF
    drf = input('Would you also like to install Django REST Framework (y/n)?: ')
    if drf == 'y':
        call(['pipenv', 'install', 'djangorestframework'])
    elif drf == 'n':
        pass
    else:
        raise Exception('Invalid value entered.')
    
    # Prompt the user to specify what DBMS they want to use
    db_pkg = input('Specify a database connector (ex:"psycopg2", "mysqlclient", etc): ')
    if not db_pkg:
        raise Exception('Must specify a db connector!')
    call(['pipenv', 'install', db_pkg])

    open('README.md', 'a')

    # Add a "tasks.py" file to the base dir to automate execute of manage.py tasks
    open('tasks.py', 'a')


""" Prompt the user for a project name, then
Run the django-admin startproject cmd  """
def start_project():
    
    proj_name = input("Enter a project name: ")

    # Throw an exception is proj_name is null
    if not proj_name:
        raise Exception('Project name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)

    call(['django-admin', 'startproject', proj_name])

    chdir(proj_name)


"""
Initialize empty git repo, then add + commit all project files
"""
def git():

    chdir('..')
    chdir('..')
    call(['git', 'init'])
    call(['git', 'add', '-A'])
    call(['git', 'commit', '-m', 'initial commit'])

    # Ask the user if they want to do a 'git remote' configuration
    git_remote = input('Would you also like to do a git remote configuration(y/n)?: ')

    if git_remote == "y":
        remote_url = input('Enter the URL of your remote repository: ')
        call(['git', 'remote', 'add', 'origin', remote_url])
    elif git_remote == "n":
        pass
    else:
        input("Invalid value entered. Press enter to exit.")


# Add an app to the project
def create_app():

        app_name = input("Enter a name for your first Django project app: ")

        # Throw an exception is app_name is null
        if not app_name:
            raise Exception('App name cannot be null!')

        call(['django-admin', 'startapp', app_name])

    
def django_main():

    create_root()
    start_project()
    create_app()
    git()
        