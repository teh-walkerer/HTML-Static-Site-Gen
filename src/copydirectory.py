import os
import shutil

# This function copies all contents from a source directory into a destination
# In this case, static to public
# It deletes contents of the destination (public) to ensure the copy is clean
# It logs the path of each file copies

def recursive_copy(source_dir, destination_dir):

    # With shutil.rmtree, delete content of the destination directory, if it exists. 
    # It must be wiped before we can transfer the contents of the source directory.
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    # Create the destination directory
    os.mkdir(destination_dir)
    
    # Copy items from source directory into destination directory
    # before copying, verify if the item is a file or a directory.
    # If a file, copy into destination directory
    # If a directory, make it a directory in the destination directory
    # and recursively copy into that subdirectory
    for item in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, item)):
            shutil.copy(os.path.join(source_dir, item), destination_dir)
            print(f"Copied file: {os.path.join(source_dir, item)} to {destination_dir}")
        else: 
            os.mkdir(os.path.join(destination_dir, item))
            recursive_copy(os.path.join(source_dir, item), os.path.join(destination_dir, item))

