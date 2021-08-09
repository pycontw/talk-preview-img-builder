"""Reformat Python scripts through invoking linter"""
from invoke import task


@task
def mypy(ctx):
    """Check style through mypy"""
    ctx.run("mypy")


@task
def black_check(ctx):
    """Check style through black"""
    ctx.run("black --check .")


@task
def isort_check(ctx):
    """Check style through isort"""
    ctx.run("isort --atomic --check-only .")


@task
def pylint(ctx):
    """Check style through pylint"""
    ctx.run("pylint --ignore=Pipfile,Pipfile.lock,pyproject.toml,setup.cfg ./app/*")


@task(pre=[mypy, black_check, isort_check, pylint], default=True)
def lint(ctx):  # pylint: disable=unused-argument
    """Check style through pylint, isort, black, flake8 and mypy"""
    return
