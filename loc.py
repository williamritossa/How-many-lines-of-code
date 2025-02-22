#!/usr/bin/env python3

"""
- Scans a given directory (or the script's directory by default)
- Recursively walks subdirectories and sums lines of code
- Optionally treat each subfolder as a separate project (with an individual count)
- Optionally only search certain file extensions (e.g., .swift, .cpp, .py, etc.)
- Optional ignoring of folders/subprojects that have zero total lines

Usage Examples:
  python loc.py
     -> Counts .swift files in the same directory (no subproject breakdown).

  python loc.py --dir /path/to/code --extensions .cpp .py .swift
     -> Counts .cpp, .py, and .swift files in the specified directory

  python loc.py --multiple
     -> Each subdirectory is treated as a separate project, printing line counts separately

  python loc.py --dir /path/to/code --extensions .py --multiple
     -> Same logic, but only .py files, each subdirectory printed separately

  python loc.py --ignore-zero
     -> Omits any subproject/folder that has zero lines
"""

import os
import sys
import argparse

def count_lines_in_files(directory: str, extensions: set[str]) -> int:
    """
    Recursively count lines in all files within 'directory' whose extensions match the given 'extensions' set
    Returns the total number of lines :)
    """
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions is None or any(file.endswith(ext) for ext in extensions):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        total_lines += sum(1 for _ in f)
                except Exception as e:
                    print(f"Could not read {full_path}: {e}", file=sys.stderr)
    return total_lines


def main():
    parser = argparse.ArgumentParser(
        description="Count lines of code in a directory for specific file extensions."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=None,
        help="The directory to scan. Defaults to the script's own directory."
    )
    parser.add_argument(
        "--extensions",
        nargs="+",
        default=[
            ".py",
            ".js",
            ".java",
            ".c",
            ".cpp",
            ".cs",
            ".php",
            ".ts",
            ".rb",
            ".swift",
            ".go",
            ".kt",
            ".r",
            ".m",
            ".h",
            ".scala",
            ".sh",
            ".dart",
            ".rs",
            ".ps1"    
        ],
        help="List of file extensions to count (e.g. .swift .py .cpp). Defaults to 20 most common languages"
    )
    parser.add_argument(
        "--multiple",
        action="store_true",
        help="Treat each subdirectory as a separate project and output line counts per folder."
    )
    parser.add_argument(
        "--ignore-zero",
        action="store_true",
        help="If set, omit printing any folder that has zero lines of code."
    )

    args = parser.parse_args()

    # Determine directory to scan
    if args.dir is not None:
        target_dir = os.path.abspath(args.dir)
    else:
        target_dir = os.path.dirname(os.path.abspath(__file__))

    extensions_set = set(args.extensions) if args.extensions is not None else None

    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory.")
        sys.exit(1)

    # If --multiple is set, treat each subfolder as a separate project
    if args.multiple:
        grand_total = 0
        # Iterate over each entry in target_dir
        for entry in sorted(os.listdir(target_dir)):
            path = os.path.join(target_dir, entry)
            if os.path.isdir(path) and not entry.startswith('.'):
                # Count lines in this subfolder
                lines = count_lines_in_files(path, extensions_set)
                if lines > 0 or not args.ignore_zero:
                    print(f"{entry}: {lines}")
                grand_total += lines
        print(f"\nGrand Total (all subfolders): {grand_total}")
    else:
        # Single project mode: count lines in the entire directory
        lines = count_lines_in_files(target_dir, extensions_set)
        print(f"Directory: {target_dir}")
        print(f"Extensions: {', '.join(extensions_set)}")
        print(f"Total lines of code: {lines}")


if __name__ == "__main__":
    main()
