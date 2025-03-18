import os

# Define the project structure as a dictionary
project_structure = {
    "src": ["components", "pipelines", "config", "utils"],
    "data": ["raw", "processed"],
    "experiments": [],
    "artifacts": [],
    "notebooks": [],
    "tests": [],
    "mlflow_tracking": [],
    "deployment": [],
    ".github/workflows": []
}

# List of required files
files_to_create = [
    "src/components/__init__.py",
    "src/pipelines/__init__.py",
    "src/config/__init__.py",
    "src/utils/__init__.py",
    "README.md",
    "requirements.txt",
    "setup.py",
    ".gitignore"
]

def create_folders():
    """Create project directories based on the defined structure."""
    for parent_folder, subfolders in project_structure.items():
        os.makedirs(parent_folder, exist_ok=True)
        for subfolder in subfolders:
            os.makedirs(os.path.join(parent_folder, subfolder), exist_ok=True)

def create_files():
    """Create required files if they don't already exist."""
    for file in files_to_create:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("")  # Create an empty file

def main():
    """Main function to create project structure and files."""
    create_folders()
    create_files()
    print("Project structure has been successfully created!")

if __name__ == "__main__":
    main()
