"""One-line out-of-office entry for make.fun.

A single out-of-office auto-reply, one line long (103 chars).
The joke: my AI cover has read every email twice and is now
asking for a raise -- the replacement outranks the replaced.
"""

from pathlib import Path

LINE = "Out of office: my AI is covering my inbox. It has read every email twice and is now asking for a raise."
ENTRY_PATH = Path("/output/entry.txt")
MAX_LEN = 200


def check_len(text: str) -> str:
    """Return *text* unchanged when it fits the cap, else raise."""
    if len(text) > MAX_LEN:
        raise ValueError("line over the cap")
    return text


def save_line(path: Path, text: str) -> None:
    """Write *text* to *path* exactly as given."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    text = check_len(LINE)
    save_line(ENTRY_PATH, text)
    saved = ENTRY_PATH.read_text(encoding="utf-8")
    assert saved == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
