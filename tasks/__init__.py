"""
Module that collects all tha available invoking commands
"""
from invoke import Collection

from tasks import lint, reformat

namespace = Collection(reformat, lint)
