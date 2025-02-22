# How many lines of code?

A versatile Python script I got carried away writing that counts lines of code in a directory for specified file extensions. It recursively scans a given directory (or, by default, the directory where the script is located) and sums up the lines of code. It can also treat each subfolder as a separate project and optionally ignore subdirectories with zero lines.

## Features

- **Extension filtering:** Counts only files with specified extensions.  
  *Default extensions:* `.py, .js, .java, .c, .cpp, .cs, .php, .ts, .rb, .swift, .go, .kt, .r, .m, .h, .scala, .sh, .dart, .rs, .ps1`
- **Handles multiple projects in one parent directory:** Optionally treats each subdirectory as a separate project and outputs individual line counts.
- **Ignore zero-line folders:** Optionally skips printing folders with zero lines of code.

## Usage

### Basic

Count lines in the current directory (using the default extensions):

```bash
python loc.py
```

### Specify a Directory and Extensions

Count lines in a specific directory for given file extensions (e.g., `.cpp`, `.py`, `.swift`):

```bash
python loc.py --dir /path/to/code --extensions .cpp .py .swift
```

### Multiple Project Mode

Treat each subdirectory as a separate project:

```bash
python loc.py --multiple
```

### Ignore Zero-Line Folders

To omit subdirectories with zero lines:

```bash
python loc.py --ignore-zero
```

### Combined Example

Count only `.py` files in a specified directory, treating each subdirectory as a separate project and ignoring those with zero lines:

```bash
python loc.py --dir /path/to/code --extensions .py --multiple --ignore-zero
```

## Command-line Arguments

- `--dir`:  
  The directory to scan. Defaults to the directory where the script resides if not provided.
  
- `--extensions`:  
  A list of file extensions to count (e.g., `.swift .py .cpp`).  
  *Default:* 20 common programming language file extensions.
  
- `--multiple`:  
  Treat each subdirectory as a separate project and output line counts for each.
  
- `--ignore-zero`:  
  Omit printing any subdirectory that has zero lines of code.

## Example Output

In multiple project mode, output might look like:

```
Memex: 1945
InstructGPT: 2022
Grand Total (all subfolders): 3967
```

If the `--ignore-zero` flag is set, folders with zero lines won’t be printed.
