# sql-formatter

A production-ready CLI SQL formatter built with `sqlparse` for parsing and formatting SQL queries. It supports input from stdin or files, output to stdout or files, and configurable reindenting (enabled by default). Structured as a `src` package with `argparse` for a clean, user-friendly interface including help, version, and examples.

## Installation

bash
git clone <repository-url>
cd sql-formatter
pip install sqlparse
Make executable (optional):
bash
chmod +x src/main.py
## Usage

Run with `python src/main.py` (or `./src/main.py` if executable).

bash
# Show help
python src/main.py --help

# Format SQL from stdin
echo "SELECT * FROM users WHERE id=1;" | python src/main.py

# Format input file to output file
python src/main.py input.sql -o output.sql

# Disable reindenting
python src/main.py input.sql --no-reindent -o output.sql

# Show version
python src/main.py --version
## Features

- Format SQL from stdin or input file (UTF-8)
- Output to stdout or specified file
- Reindent SQL (default: enabled; use `--reindent` or `--no-reindent`)
- Error handling for file I/O and empty input
- Built-in examples and version info via `--help` and `--version`

## Dependencies

- `sqlparse` (external)
- `argparse`, `sys` (Python stdlib)

## Contributing

Contributions welcome! No tests implemented yet.

## License

MIT