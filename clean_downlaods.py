import os
import shutil

# Dictionary mapping file extensions to their respective categories (e.g., Images, Documents, etc.)
file_categories = {
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',
    '.svg': 'Images',

    # Documents
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.odt': 'Documents',
    '.rtf': 'Documents',

    # Spreadsheets
    '.xls': 'Spreadsheets',
    '.xlsx': 'Spreadsheets',
    '.csv': 'Spreadsheets',

    # Presentations
    '.ppt': 'Presentations',
    '.pptx': 'Presentations',

    # Videos
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.flv': 'Videos',

    # Music/Audio
    '.mp3': 'Music',
    '.wav': 'Music',
    '.flac': 'Music',
    '.aac': 'Music',

    # Compressed files
    '.zip': 'Compressed',
    '.rar': 'Compressed',
    '.7z': 'Compressed',
    '.tar': 'Compressed',
    '.gz': 'Compressed',

    # Code files
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
    '.php': 'Code',

    # Executable files
    '.exe': 'Executables',
    '.msi': 'Executables',

    # Other common file types
    '.iso': 'Disk Images',
    '.dmg': 'Disk Images',
    '.xml': 'XML Files'
}

# Specify the path to the Downloads directory
path = "C://Users/saadm//Downloads"

# List all items in the specified directory
dir_list = os.listdir(path)

# Filter out the items to get only the files (exclude directories)
files = [item for item in dir_list if os.path.isfile(os.path.join(path, item))]

# Iterate over each file in the directory
for file in files:
    # Get the file name and extension
    file_name = file
    file_extension = os.path.splitext(file_name)[1]

    # Check if the file extension exists in the file_categories dictionary
    if file_extension in file_categories:
        # Get the category (e.g., Images, Documents) based on the file extension
        category = file_categories[file_extension]

        # Create the full folder path where the file should be moved (Downloads/Category)
        file_folder_path = os.path.join(path, category)

        # Create the category folder if it doesn't exist
        os.makedirs(file_folder_path, exist_ok=True)

        # Define the destination path for moving the file to the appropriate category folder
        destination_path = os.path.join(file_folder_path, file)

        # Define the source path for the current file
        source_path = os.path.join(path, file)

        # Move the file from the source path to the destination path (organized by category)
        shutil.move(source_path, destination_path)
