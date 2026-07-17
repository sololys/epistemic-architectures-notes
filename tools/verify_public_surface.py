#!/usr/bin/env python3
"""Fail-closed verifier for a bounded public export repository."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / ".github" / "public-paths.txt"
MAX_FILE_BYTES = 512 * 1024
DISALLOWED_SUFFIXES = {
    ".7z", ".bin", ".docx", ".env", ".gz", ".ipynb", ".key", ".kdbx",
    ".p12", ".pdf", ".pem", ".pfx", ".pptx", ".rar", ".tar", ".tgz",
    ".wasm", ".xlsx", ".zip",
}


def protected_repo_fragments() -> tuple[bytes, ...]:
    values = (
        "realiserings" + "grammatikk-artifact-family",
        "Poronesis" + "-lab",
        "Kjerne" + "-privat",
        "Gemini" + "-Core",
        "FASE" + "_SPEIL",
        "ky-rox" + "-finans-gate",
        "research-kernel" + "_viability",
        "docs-gko" + "_core_manifesto",
    )
    return tuple(value.lower().encode("utf-8") for value in values)


def credential_patterns() -> tuple[re.Pattern[bytes], ...]:
    return (
        re.compile(("-" * 5 + r"BEGIN [A-Z0-9 ]*PRIVATE KEY" + "-" * 5).encode()),
        re.compile(("AK" + r"IA[0-9A-Z]{16}").encode()),
        re.compile(("gh" + r"[pousr]_[A-Za-z0-9_]{20,}").encode()),
        re.compile(("sk" + r"-(?:proj-)?[A-Za-z0-9_-]{20,}").encode()),
        re.compile(("xo" + r"x[baprs]-[A-Za-z0-9-]{20,}").encode()),
    )


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def tracked_files() -> list[str]:
    raw = git("ls-files", "-z")
    return sorted(item.decode("utf-8") for item in raw.split(b"\0") if item)


def allowed_files() -> list[str]:
    return sorted(
        line.strip()
        for line in ALLOWLIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )


def classify_data(data: bytes) -> set[str]:
    lower = data.lower()
    findings: set[str] = set()
    if any(fragment in lower for fragment in protected_repo_fragments()):
        findings.add("PRIVATE_REPOSITORY_REFERENCE")
    if any(pattern.search(data) for pattern in credential_patterns()):
        findings.add("CREDENTIAL_MATERIAL")
    return findings


def main() -> int:
    findings: list[tuple[str, str]] = []
    tracked = tracked_files()
    allowed = allowed_files()

    findings.extend((path, "UNKNOWN_TRACKED_PATH") for path in sorted(set(tracked) - set(allowed)))
    findings.extend((path, "MISSING_REQUIRED_PATH") for path in sorted(set(allowed) - set(tracked)))

    for relative in tracked:
        path = ROOT / relative
        pure = PurePosixPath(relative)
        if path.is_symlink():
            findings.append((relative, "SYMLINK_PROHIBITED"))
            continue
        if pure.suffix.lower() in DISALLOWED_SUFFIXES or pure.name.lower().startswith(".env"):
            findings.append((relative, "ARCHIVE_BINARY_OR_SECRET_PATH"))
            continue
        if not path.is_file():
            continue
        data = path.read_bytes()
        if len(data) > MAX_FILE_BYTES:
            findings.append((relative, "FILE_SIZE_LIMIT"))
        if b"\0" in data:
            findings.append((relative, "BINARY_PAYLOAD"))
            continue
        findings.extend((relative, rule) for rule in classify_data(data))

    if findings:
        print("PUBLIC_IP_GATE=KILL")
        for path, rule in sorted(set(findings)):
            print(f"- {rule}: {path}")
        return 1

    print("PUBLIC_IP_GATE=PASS")
    print(f"TRACKED_FILES={len(tracked)}")
    print("SCOPE=EXACT_ALLOWLISTED_TREE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
