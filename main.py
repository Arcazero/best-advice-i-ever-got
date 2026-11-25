"""Best Advice I Ever Got — make.fun entry.

Writes one sentence — the best advice the writer ever received —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set),
exactly as the program/v1 harness expects. No input files, no
network, no randomness: the same sentence every run.
"""

import os

SENTENCE = (
    "My father said a man who cannot say sorry will spend his life "
    "being right and alone, and I have watched him prove it both ways."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # Read it back and verify the file holds exactly the sentence.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == SENTENCE, "entry.txt does not match SENTENCE"
    print(f"Wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()
