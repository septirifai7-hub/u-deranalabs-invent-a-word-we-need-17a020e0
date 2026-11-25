"""Entry for "Invent a Word We Need" (make.fun).

"Scrollock" names the moment doomscrolling stops being a choice: you
look up, four hours of bad news have passed, and your own thumb has
had enough and filed for divorce.
"""

ENTRY = (
    "Doomlock (n.): the moment you realise you've read bad news for "
    "four hours and your thumb has filed for divorce."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
