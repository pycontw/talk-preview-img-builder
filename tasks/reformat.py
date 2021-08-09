"""Reformat Python scripts through invoking reformatting tool"""
from invoke import task


@task
def black(ctx):
    """Reformat Python scripts through black"""
    ctx.run("black .")


@task
def isort(ctx):
    """Reformat Python scripts through isort"""
    ctx.run("isort --atomic .")


@task(pre=[isort, black], default=True)
def reformat(ctx):  # pylint: disable=unused-argument
    """Reformat Python scripts through black and isort"""
    return
