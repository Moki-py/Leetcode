import os


FOLDERS = ["strings", "lists", "nums"]
FILES = ["easy.py", "medium.py", "hard.py"]


def create_tree(ROOT_DIR: str | None = None):
    """Create tree of folders and files in ROOT_DIR"""
    # ROOT_DIR =
    # os.path.join(os.getcwd(), ROOT_DIR) if ROOT_DIR else os.getcwd()
    pass


def create_files(
    FOLDERS: list[str], FILES: list[str], ROOT_DIR: str | None = None
) -> None:
    """
    Создает файлы с названиями из FILES и соответствующим расширением из FORMATS
    в каждой из папок FOLDERS в рабочей директории

    :type FOLDERS: List[int] -- названия папок
    :type FILES: List[int] -- названия файлов
    :type ROOT_DIR: str | None -- рабочая директория(default None)

    Пример строения репозитория после применения с указанными параметрами:

    FOLDERS = ['dir1', 'dir2']
    FILES = ['main.py', 'README.md']
    ROOT_DIR = 'example'

    TREE:
    example
    ├── dir1
    │   ├── README.md
    │   └── main.py
    └── dir2
        ├── README.md
        └── main.py

    """
    ROOT_DIR = os.path.join(os.getcwd(), ROOT_DIR) if ROOT_DIR else os.getcwd()
    for PATH in FOLDERS:
        os.makedirs(os.path.join(ROOT_DIR, PATH))
        for FILE in FILES:
            with open(f"{os.path.join(ROOT_DIR, PATH)}/{FILE}", "w") as f:
                pass


if __name__ == "__main__":
    create_files(FOLDERS=FOLDERS, FILES=FILES, ROOT_DIR="solutions")
