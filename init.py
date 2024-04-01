"""Create tree of folders and files in ROOT_DIR"""
import os


FOLDERS = ["strings", "lists", "nums"]
FILES = ["easy.py", "medium.py", "hard.py"]


def create_files(
    folders: list[str], files: list[str], root_dir: str | None = None
) -> None:
    """
    Create files with names from FILES and corresponding
    extensions from FORMATS in each of the FOLDERS
    in the working directory.

    :type folders: List[int] -- folder names
    :type files: List[int] -- file names
    :type root_dir: str | None -- working directory (default None)

    Example repository structure after applying with the specified parameters:

    folders = ['dir1', 'dir2']
    files = ['main.py', 'README.md']
    root_dir = 'example'

    TREE:
    example
    ├── dir1
    │   ├── README.md
    │   └── main.py
    └── dir2
        ├── README.md
        └── main.py

    """
    root_dir = os.path.join(os.getcwd(), root_dir) if root_dir else os.getcwd()
    for path in folders:
        os.makedirs(os.path.join(root_dir, path))
        for file in files:
            file_path = os.path.join(root_dir, path, file)
            with open(file_path, "w", encoding="utf-8"):
                pass


if __name__ == "__main__":
    create_files(folders=FOLDERS, files=FILES, root_dir="solutions")
