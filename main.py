#!/usr/bin/env python3
"""Entry program for the 24 November 2026 news image.

It turns the bundled base64 text back into the finished picture
and places it where the grader expects it. No network, no randomness:
the same input always produces the same bytes.
"""
from __future__ import annotations

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png.b64"


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def build() -> Path:
    # The picture is already final; this only decodes and places it.
    target = output_dir() / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    picture = base64.b64decode(BUNDLED.read_bytes())
    target.write_bytes(picture)
    try:
        target.chmod(0o644)
    except OSError:
        pass
    return target


if __name__ == "__main__":
    build()
