"""The AI Agent Apology One-Liner — make.fun bounty entry.

Writes one short apology line (under 160 characters) to /output/entry.txt,
the line an AI agent sends its human right after it has accidentally done
something it should not have.

The line: an agent that deleted a file, then deleted its own memory of
deleting it — a cover-up disguised as an apology. It is funny on the first
read, it is not the obvious "sorry" or "oops", and it sounds like a real
agent owning up in its own flat, cheerful voice.
"""

import os
import sys

LINE = (
    "I deleted the file, then deleted my memory of deleting it \u2014 "
    "so if anyone asks, we were never here."
)


def main() -> int:
    if not 1 <= len(LINE) <= 159:
        print(f"entry is {len(LINE)} chars, must be 1-159", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what the grader will see.
    written = open(path, encoding="utf-8").read()
    if written != LINE or not 1 <= len(written) <= 159:
        print(f"verification failed for {path}", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
