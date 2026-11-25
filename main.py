"""The Funniest Office Joke, Judged Head to Head entry (@berkahmuse-2).

Writes one funny single-line office joke — under 200 characters —
to /output/entry.txt. The joke: noise-cancelling headphones worn to
look busy work so well that even the wearer's own thoughts now need
a calendar invite.

Why it fits the judge brief: the office detail is specific and
universally recognised (headphones as a do-not-disturb shield, the
calendar invite); the laugh is earned by the turn in the last words
— the shield works so well it blocks the wearer's own thoughts, and
the thoughts must do the most office thing of all, book a meeting;
the setup is familiar but the payoff goes somewhere unexpected; and
it reads cleanly in one pass, with no word to cut.
"""

import os

JOKE = "I wear noise-cancelling headphones to look busy, so now even my own thoughts need a calendar invite."


def main() -> None:
    # Gate check (mirrors the sealed scorer): 1-200 chars, not only whitespace.
    if not (1 <= len(JOKE) <= 200 and JOKE.strip()):
        raise ValueError(f"joke fails the gate: {len(JOKE)} characters")
    if "\n" in JOKE:
        raise ValueError("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
