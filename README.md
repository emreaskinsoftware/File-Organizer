# Advanced File Organizer Utility

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

This project is a powerful and flexible Python script designed to automate the process of cleaning and organizing directories. It intelligently sorts files into designated folders based on their extensions and cleans up junk files, helping you maintain a tidy workspace, especially in cluttered folders like "Downloads".

## Key Features

-   **Rule-Based Sorting:** Uses a Python dictionary to define which file extensions go into which folders, making the rules easy to read and modify.
-   **Junk File Removal:** Deletes files with specified extensions (e.g., `.log`, `.tmp`, `.bak`) to free up space.
-   **Automatic Folder Creation:** If a destination folder for a file type doesn't exist, the script creates it automatically.
-   **Zero Dependencies:** Runs using only Python's standard libraries (`os`, `shutil`), so no installation of external packages is required.
-   **Safe Operations:** Reports a summary of actions taken and handles potential errors during file deletion.

## Getting Started

Follow these steps to get the script up and running on your local machine.

### Prerequisites

-   Python 3.6 or higher.

### Installation & Configuration

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KULLANICI-ADIN/REPO-ADIN.git](https://github.com/KULLANICI-ADIN/REPO-ADIN.git)
    cd REPO-ADIN
    ```
2.  **Configure the Rules in `main.py`:**
    -   Set the `path` variable to the absolute path of the directory you want to organize.
        ```python
        path = "C:/Users/YourUser/Downloads"
        ```
    -   Modify the `move_ex` dictionary to customize the sorting rules. The key is the file extension, and the value is the name of the destination folder.
        ```python
        move_ex = {
            ".pdf": "Documents",
            ".png": "Images",
            ".jpg": "Images"
        }
        ```
    -   Update the `remove_ex` list with any file extensions you want to permanently delete.
        ```python
        remove_ex = [".log", ".tmp"]
        ```

3.  **Run the script from your terminal:**
    ```bash
    python main.py
    ```
    The script will organize the files and print a summary of how many files were processed.

## Future Improvements

-   [ ] Implement a command-line interface (CLI) using `argparse` to pass the directory path as an argument instead of hard-coding it.
-   [ ] Read configuration from an external file (e.g., `config.json`).
-   [ ] Add logging to record all file operations (moved, deleted, errors).
