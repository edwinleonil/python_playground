from pathlib import Path


def generate_tree(directory: Path, prefix: str = "", depth: int = 0, max_depth: int = None, exclude: list = None):
    """
    Recursively generates a tree-like structure for a given directory.

    :param directory: The base directory (Path object)
    :param prefix: The prefix string for formatting
    :param depth: Current depth in the directory tree
    :param max_depth: Maximum depth to traverse (None for unlimited)
    :param exclude: List of directory names to exclude
    """
    if max_depth is not None and depth >= max_depth:
        return ""

    if exclude is None:
        exclude = []

    entries = sorted(directory.iterdir(), key=lambda e: (
        not e.is_dir(), e.name))  # Sort: Directories first
    tree_str = ""

    for i, entry in enumerate(entries):
        if entry.name in exclude:
            continue

        connector = "└── " if i == len(entries) - 1 else "├── "
        tree_str += f"{prefix}{connector}{entry.name}\n"

        if entry.is_dir():  # Recursively process directories
            extension = "    " if i == len(entries) - 1 else "│   "
            tree_str += generate_tree(entry, prefix +
                                      extension, depth + 1, max_depth, exclude)

    return tree_str


# Set the directory path
base_path = Path.cwd()  # Uses the current working directory

# Directories to exclude
exclude_dirs = ['.venv', 'data', '__pycache__', '.git']

# Generate and print the tree structure
print(base_path.name)
print(generate_tree(base_path, exclude=exclude_dirs))
