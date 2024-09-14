DownloadWizard
DownloadWizard is a Python script designed to automatically organize files in your Downloads folder by sorting them into categorized folders based on file extensions. This tool helps keep your Downloads directory clean and tidy without manual effort.

Features
Automatic file organization: The script identifies files based on their extensions and moves them into appropriate categories such as:

Images (e.g., .jpg, .png)
Documents (e.g., .pdf, .docx)
Videos (e.g., .mp4, .mkv)
Music (e.g., .mp3, .wav)
Compressed files (e.g., .zip, .rar)
And more!
Simple to use: Just run the script and watch your Downloads folder get organized automatically.

Customizable: You can easily extend the file_categories dictionary to add more file types or create custom categories.

No folder handling: The tool focuses on files and does not move or organize folders.

Usage:
Clone the repository:
   git clone https://github.com/VoltSaad/DownloadWizard.git

Navigate to the project directory:
   cd DownloadWizard
   
Run the script:
   python download_sorter.py
   
* The script will automatically scan your Downloads folder and organize the files into categorized subfolders.

Installation
Requirements:
Python 3.x
No external dependencies (uses built-in Python libraries like os and shutil)
How it Works
The script scans your Downloads folder for files and sorts them into appropriate subfolders based on their file extensions. The mapping of file extensions to categories is stored in the file_categories dictionary, which you can customize to include additional file types or create new categories.

By default, the script organizes files into categories like "Images," "Documents," "Videos," "Music," etc. It does not move existing folders, leaving them in place.

Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. You can also open an issue if you have suggestions or encounter any bugs.

License
This project is licensed under the MIT License - see the LICENSE file for details.
