#!/usr/bin/env python3
import pathlib

LINE = 'Missed spot detected. Cause: it was underneath my pride, and I am not a crawling chassis.'


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
