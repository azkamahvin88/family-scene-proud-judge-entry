# family-scene-proud-judge-entry (Python 3.13, standard library only)
# Writes one fixed family scene — a small domestic moment about a child
# learning what "proud" means — to /output/entry.txt.
# Deterministic: a fixed string, no randomness, no network, no time.
# Gate: UTF-8 text, 1 to 280 characters, at least one non-whitespace char.
# This entry: 192 characters, one line.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "My son asked what 'proud' means, so I pointed at Mom, eyes shining "
    "as he read his first sentence aloud. 'That,' I said. 'That's proud.' "
    "He puffed out his chest like he'd just won the Olympics."
)

def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    # Bytes, not text mode: text mode would write the platform's line ends
    # and its default encoding.
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))

if __name__ == "__main__":
    main()
