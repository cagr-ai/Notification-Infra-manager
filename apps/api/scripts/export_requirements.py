"""Write requirements.txt for Vercel from the Poetry virtualenv (pip freeze)."""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "requirements.txt"
    try:
        result = subprocess.run(
            ["poetry", "run", "pip", "freeze"],
            check=True,
            cwd=root,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        sys.stderr.write(f"Could not run `poetry run pip freeze`: {e}\n")
        sys.exit(1)

    lines = [
        line.strip()
        for line in result.stdout.splitlines()
        if line.strip() and not line.startswith("#")
    ]
    # Omit dev-only tools from the Vercel install surface
    lines = [line for line in lines if not line.lower().startswith("ruff")]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
