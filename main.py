"""Make the AI judge feel curious — make.fun entry.

Writes one short intriguing text to entry.txt in the output directory
given by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

TEXT = (
    "Every night at 2 a.m., the lighthouse on the point flashes twice, "
    "though it was decommissioned in 1987. Last Tuesday I rowed out to it. "
    "The door was open, the kettle was warm, and someone had left a second "
    "cup on the table \u2014 still steaming."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
