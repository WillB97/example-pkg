#!/usr/bin/env python3
"""Get a setuptools-scm style version string for the current git repository."""

import re
import subprocess
from dataclasses import dataclass


@dataclass
class VersionParts:
    """The parts of a version string."""

    major: int
    minor: int
    patch: int
    distance: int
    hash: str


def get_version() -> str:
    """Get the version string."""
    version = get_git_version()
    if version.distance == 0:
        return f"{version.major}.{version.minor}.{version.patch}"

    return f"{version.major}.{version.minor}.{version.patch + 1}.dev{version.distance}"


def get_git_version() -> VersionParts:
    """Get the version parts from git."""
    git_version = subprocess.check_output(
        ["git", "describe", "--tags", "--always", "--long"], text=True
    )
    version_parts = re.fullmatch(r"(.+)-(\d+)-(g[a-z0-9]+)\n", git_version)
    if not version_parts:
        # The git repo has no tags, count the number of commits in the repo
        num_commits = int(
            subprocess.check_output(["git", "rev-list", "HEAD", "--count"], text=True)
        )
        return VersionParts(0, 0, 0, num_commits, git_version)

    tag_ver, tag_distance, commit = version_parts.groups()

    tag_parts = re.fullmatch(r"(\d+).(\d+).(\d+)", tag_ver)
    if not tag_parts:
        raise ValueError(f"Tag {tag_ver} is not in the valid format")
    return VersionParts(
        int(tag_parts[1]), int(tag_parts[2]), int(tag_parts[3]), int(tag_distance), commit
    )


def main():
    """Print the version string."""
    version = get_version()
    print(version)


if __name__ == "__main__":
    (main())
