import os

# Define the folder structure
folders = [
    "data/raw", 
    "data/processed",
    "notebooks",
    "src",
    "reports"
]

files = {
    "README.md": "# Brent Oil Task 1\n\nThis repository contains the workflow and model understanding for analyzing Brent oil price changes.",
    "requirements.txt": "pandas\nmatplotlib\nruptures\njupyter",
    "notebooks/01_data_exploration.ipynb": "",
    "src/data_loader.py": "# Script for loading and preprocessing data",
    "src/eda.py": "# Script for EDA & visualization"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file, content in files.items():
    with open(file, "w") as f:
        f.write(content)

print("Folder structure and files created successfully!")