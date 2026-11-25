"""Copy the one-line horoscope in entry.txt next to this script, byte for
byte, into $MAKEFUN_OUTPUT_DIR/entry.txt (mode 0644).

Stdlib only. No temp file is used: the output is written directly so the
grader sees exactly the shipped bytes.
"""

import os


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        raise SystemExit(f"cannot read entry.txt: {exc}") from exc
    if not data.strip():
        raise SystemExit("entry.txt is empty")
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "wb") as f:
        f.write(data)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
