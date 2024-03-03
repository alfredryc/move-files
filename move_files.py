import glob 
import os 
import shutil 

source_directory = r"C:\Users\Lenovo\Downloads\\"
destination_directory = r"C:\Users\Lenovo\Downloads\\"

# Extension and destination
extension_destinations = {
    ".pdf": "pdf",
    ".docx": "docx",
    ".txt": "txt",
    ".xlsx": "excel",
    ".png": "png",
    ".jpg": "jpg",
    ".rar": "rar",
    ".zip": "zip",
    ".exe": "exe",
}    
    
def move():
    # Dictionary | extension | directory path 
    for extension, folder in extension_destinations.items():
        # find all files in the source path
        files = glob.glob(source_directory + f"*{extension}")

        # Iterates over each file found that has the current extension
        for file in files:
            # Gets the file name from the full file path
            file_name = os.path.basename(file)
            # Constructs the destination folder path using the destination folder 
            # and the specific folder name for the current extension.
            destination_folder = os.path.join(destination_directory, folder)

            # Check if the destination folder exists. If it doesn't exist, create it.
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            # Move the file to the constructed destination directory.
            shutil.move(file, os.path.join(destination_folder, file_name))
            print(f"Moved {extension} file:", file)

def main():
    move()

if __name__ == '__main__':
    main()
