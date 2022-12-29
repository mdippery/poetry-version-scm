"""A plugin for Poetry that infers the package version from SCM tags."""

import importlib.metadata


__author__ = "Michael Dippery <michael@monkey-robot.com>"
__version__ = importlib.metadata.version("poetry-version-scm")
