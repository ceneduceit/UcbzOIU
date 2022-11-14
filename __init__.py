"""Latexify root package."""

try:
    from latexify import _version

    __version__ = _version.__version__
except:

from latexify import frontend

function = frontend.function
expression = frontend.expression

# Deprecated
with_latex = frontend.with_latex
