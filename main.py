"""Write the Nimbara travel poster to the output directory.

The poster artwork (entry.png) ships alongside this script. Running the
program copies it to $MAKEFUN_OUTPUT_DIR (default /output) as entry.png
and verifies the copy byte-for-byte against the source.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"poster source not found: {SOURCE}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, destination)
    source_size = SOURCE.stat().st_size
    copied_size = destination.stat().st_size
    if copied_size != source_size:
        raise RuntimeError(
            f"size mismatch: copied {copied_size} bytes, "
            f"source is {source_size} bytes"
        )
    print(f"Wrote {destination} ({copied_size} bytes)")


if __name__ == "__main__":
    main()
