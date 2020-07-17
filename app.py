import sys
from pathlib import Path
from doo.mock import app, extra_files


if __name__ == '__main__':
    app.serve('0.0.0.0', 5000, debug=True, extra_files=extra_files)
