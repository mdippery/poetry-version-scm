from cleo.io.io import IO
from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry

from poetry_version_scm.scm.git import Git


class VersionScmPlugin(Plugin):
    def activate(self, poetry: Poetry, io: IO) -> None:
        if not poetry.pyproject.poetry_config.get("use_scm_version", False):
            return

        io.write_line(f"BEFORE: {poetry.package.version}")
        git = Git()
        has_tag, desc = git.describe()
        version = desc.lstrip("v") if has_tag else "0.0.0"
        poetry.package.version = version
        io.write_line(f"AFTER: {poetry.package.version}")
