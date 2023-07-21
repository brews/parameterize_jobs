
"""Top-level package for Parameterize Jobs."""

from parameterize_jobs._version import version as __version__
from parameterize_jobs.parameterize_jobs import (
    Component,
    ComponentSet,
    MultiComponentSet,
    Constant,
    ParallelComponentSet,
    expand_kwargs)

__author__ = """Michael Delgado"""
__email__ = 'delgado.michaelt@gmail.com'

_module_imports = (
    Component,
    ComponentSet,
    MultiComponentSet,
    Constant,
    ParallelComponentSet,
    expand_kwargs
)

__all__ = list(map(lambda x: x.__name__, _module_imports))
