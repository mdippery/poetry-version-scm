"""Interface to Git."""

import pathlib
import subprocess
import typing as t


PathLike = t.Union[str, pathlib.Path]


class Git:
    def __init__(self, root: PathLike = pathlib.Path(".")) -> None:
        self.root = pathlib.Path(root).absolute()
        if not self.root.name.endswith(".git"):
            self.root = self.root / ".git"

    def exec(self, *args: str) -> subprocess.CompletedProcess:
        args = ["git"] + list(args)
        env = {"GIT_DIR": str(self.root)}
        return subprocess.run(args, env=env, capture_output=True)

    def describe(self, pattern: str = "v*") -> t.Tuple[bool, str]:
        out = self.exec("describe", "--match", pattern)
        if out.returncode != 0:
            return False, out.stderr.decode("utf-8").strip()
        return True, out.stdout.decode("utf-8").strip()

    def __repr__(self) -> str:
        return f"Git(root={self.root!r})"
