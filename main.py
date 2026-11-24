"""One-Sentence Absurd Invention Pitch entry.

Writes a single-sentence pitch (max 220 characters) to /output/entry.txt.
Deterministic: the sentence is a fixed string, so every run produces
byte-identical output.
"""

import os

SENTENCE = (
    "Meet the Sock Sleuth: a washing machine that tracks down your missing "
    "sock, interrogates the lint trap, and returns it with a signed "
    "confession and a formal apology."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 220, "pitch must be 1-220 characters"
    assert SENTENCE.count(".") == 1, "pitch must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the sentence and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
