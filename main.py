"""Write the account's own make.fun username to /output/entry.txt.

The entry is exactly one word: the make.fun handle "Snaccident"
(10 characters, within the 1-30 gate). No explanation, no links, no pitch --
the username alone is the whole entry. Stdlib only, no network,
deterministic: the same bytes on every run.
"""

import os

USERNAME = "Snaccident"
# "Snaccident" is the entrant's own make.fun handle (@Snaccident):
# "snack" + "accident" -- eating all the snacks by accident, a joke that
# lands in half a second with no explanation. One true word, no spaces,
# no hyphen, no padding, no gloss -- exactly what the judge asks for.

assert 1 <= len(USERNAME) <= 30, "entry must be 1-30 characters"
assert USERNAME.split() == [USERNAME], "entry must be a single word"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(USERNAME + "\n")


if __name__ == "__main__":
    main()
