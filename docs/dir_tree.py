from pathlib import Path


def generate_tree(directory: Path, prefix: str = "", depth: int = 0, max_depth: int = None, exclude: list = None, depth_dict: dict = None):
    """
    Recursively generates a tree-like structure for a given directory.

    :param directory: The base directory (Path object)
    :param prefix: The prefix string for formatting
    :param depth: Current depth in the directory tree
    :param max_depth: Maximum depth to traverse (None for unlimited)
    :param exclude: List of directory names to exclude
    :param depth_dict: Dictionary mapping directory names to their respective max depths
    """
    if depth_dict is None:
        depth_dict = {}

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
            # Determine the max depth for this directory
            entry_max_depth = depth_dict.get(entry.name, max_depth)
            extension = "    " if i == len(entries) - 1 else "│   "
            tree_str += generate_tree(entry, prefix +
                                      extension, depth + 1, entry_max_depth, exclude, depth_dict)

    return tree_str


# Set the directory path
base_path = Path.cwd()  # Uses the current working directory

# Directories to exclude
exclude_dirs = ['.venv', '__pycache__', '.git', 'wandb', ]

# Maximum depth to traverse
max_depth = 4  # Change this value to set the desired depth

# Dictionary mapping directory names to their respective max depths
depth_dict = {
    'data': 4,
    # Add more directories and their depths as needed
}

# Generate the tree structure
tree_output = generate_tree(
    base_path, max_depth=max_depth, exclude=exclude_dirs, depth_dict=depth_dict)

# Save the tree output to a Markdown file
with open("docs/DirectoryTree.md", "w", encoding="utf-8") as file:
    file.write("# Directory tree to run the project\n\n")
    file.write(f"{base_path.name}\n")
    file.write("```\n")  # Add opening triple backticks
    file.write(tree_output)
    file.write("```\n")  # Add closing triple backticks

# Print the tree structure
print(base_path.name)
print(tree_output)
