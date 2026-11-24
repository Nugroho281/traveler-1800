#!/usr/bin/env python3
"""Write the winning entry sentence to /output/entry.txt.

Bounty: "One Sentence for a Traveler from 1800"
(u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) — one sentence,
max 200 characters, explaining the modern internet to a time traveler
from 1800, using only words that existed in 1800.

Pure stdlib. Deterministic: byte-identical output on every run.
"""

import os

SENTENCE = (
    "Picture a town crier at every door who can whisper any letter, book, "
    "or tale from the far side of the world into your ear before you draw breath."
)

# Words coined after 1800 — none may appear in the entry (case-insensitive).
BANNED_POST_1800 = (
    "computer", "screen", "website", "online", "digital", "email", "app",
    "data", "network", "internet", "telegraph", "wire",
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Gate: one sentence, <= 200 chars, UTF-8, no trailing newline,
    no post-1800 words."""
    assert len(text) <= 200, f"entry too long: {len(text)} chars"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert not text.endswith("\n"), "entry must not end with a newline"
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    # Mask "make.fun" so its dot is not counted as a sentence terminator.
    masked = text.replace("make.fun", "makeXfun")
    terminators = sum(masked.count(t) for t in (".", "!", "?"))
    assert terminators == 1, f"expected exactly 1 sentence terminator, got {terminators}"
    lowered = text.lower()
    for word in BANNED_POST_1800:
        assert word not in lowered, f"banned post-1800 word present: {word}"


def main() -> None:
    check_gate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
