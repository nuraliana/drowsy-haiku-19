"""Write the haiku entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only.
"""

import os
from pathlib import Path

HAIKU = """Midnight, the counter
holds one more than I left it
no one touched the code
"""


def main() -> None:
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
