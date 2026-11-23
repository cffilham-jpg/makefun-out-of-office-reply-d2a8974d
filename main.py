"""Write one out-of-office auto-reply to entry.txt.

Standard library only. The grader runs as an unprivileged user in a
read-only directory, so the output directory comes from MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = "Out of office until Monday. A cron job is covering for me. It answered your email twice, cc'd your boss, and is demanding a vacation of its own."


def validate(text):
    """Gate the reply against the competition's gate rules.

    Raises SystemExit with a clear message when the text is empty or
    whitespace-only, contains a control character, or is outside the
    1..160 character range.
    """
    if not text or not text.strip():
        raise SystemExit("entry text is empty or whitespace-only")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise SystemExit("entry text contains a control character")
    if not 1 <= len(text) <= 160:
        raise SystemExit(
            "entry text must be 1..160 characters, got %d" % len(text)
        )


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s: %d characters" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
