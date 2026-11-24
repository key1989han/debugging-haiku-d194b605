import os
from pathlib import Path

poem = Path(__file__).with_name("haiku.txt").read_bytes()
output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
(output_dir / "entry.txt").write_bytes(poem)
