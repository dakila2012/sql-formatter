#!/usr/bin/env python3
import argparse
import sys
import sqlparse

def main():
    parser = argparse.ArgumentParser(
        description="CLI SQL formatter using sqlparse.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --help
  echo "SELECT * FROM users WHERE id=1;" | %(prog)s
  %(prog)s input.sql -o output.sql
        """,
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default=None,
        help="Input SQL file (default: stdin)",
    )
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--reindent",
        dest="reindent",
        action="store_true",
        help="Reindent the SQL (default: True)",
    )
    group.add_argument(
        "--no-reindent",
        dest="reindent",
        action="store_false",
        help="Do not reindent the SQL",
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s 0.1.0"
    )
    args = parser.parse_args()
    args.reindent = args.reindent if args.reindent is not None else True

    if args.input_file:
        try:
            with open(args.input_file, "r", encoding="utf-8") as f:
                sql = f.read()
        except OSError as e:
            print(f"Error reading input file '{args.input_file}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        sql = sys.stdin.read()

    if not sql.strip():
        print("Error: No SQL input provided.", file=sys.stderr)
        sys.exit(1)

    formatted = sqlparse.format(sql, reindent=args.reindent)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(formatted)
        except OSError as e:
            print(f"Error writing output file '{args.output}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        sys.stdout.write(formatted)

if __name__ == "__main__":
    main()
