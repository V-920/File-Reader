# File Reader

A simple Python command-line application that allows users to read and display the contents of text files by providing a directory path and filename.

## Features

- **Directory Navigation:** Navigate to a specified directory using Python's `os` module.
- **File Reading:** Open and read text files.
- **Content Display:** Display the entire contents of a file directly in the terminal.
- **Error Handling:** Handles common errors, including:
  - `FileNotFoundError` – When the specified directory or file doesn't exist.
  - `PermissionError` – When the program doesn't have permission to access a file.
- **Continuous Execution:** Allows users to read multiple files without restarting the program.

## Technologies Used

- Python 3
- `os` module
- Exception Handling (`try-except`)
- File Handling (`open()`)

## How to Run

1. Clone this repository:

   ```bash
   git clone github.com/V-920/File-Reader
   ```

2. Navigate to the project directory:

   ```bash
   cd File-Reader
   ```

3. Run the Python file:

   ```bash
   python "File Reader.py"
   ```

4. Enter the directory path when prompted.
5. Enter the filename you want to read.
---

*Built as part of my Python programming journey.*
