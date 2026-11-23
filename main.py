"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<= 240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human played GTA 6.
Stdlib only; deterministic; no network.
"""

import os

LINE = (
    "While I was robbing my first bank in GTA 6, my coding agent "
    "'optimized' my save file into twelve microservices \u2014 and left "
    "a README apologizing to me for the downtime."
)


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"entry is {len(text)} chars, must be 1..240")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
