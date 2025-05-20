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

    



    # first ensure it is clean by listing the directory and ensuring it is empty
    # second delete the contents of public to ensure copy is clean


    # Join one or more path segments intelligently. 
    # The return value is the concatenation of path and all members of *paths, 
    # with exactly one directory separator following each non-empty part, except the last. 
    os.path.join("/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/static", )
    
    # Return True if path is an existing regular file. 
    # This follows symbolic links, so both islink() and isfile() can be true for the same path.
    os.path.isfile(path)

    # Return True if path refers to an existing path or an open file descriptor. 
    # Returns False for broken symbolic links. 
    os.path.exists(path)

    # Return a list containing the names of the entries in the directory given by path.
    #  The list is in arbitraty order and does not include special entries
    os.listdir(path='.')

    # Return True if path is an existing regular file.
    # This follows symbolic links, so both islink() and isfile() can be true for the same path.
    os.path.isfile(path)

    # Create a directory named path
    #
    os.mkdir(path)

    # Copies the file src to the file or directory dst. src and dst should be path-like objects or strings. 
    # If dst specifies a directory, the file will be copied into dst using the base filename from src.
    # If dst specifies a file that already exists, it will be replaced. 
    # Returns the path to the newly created file.
    shutil.copy(src, dst)

    # Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory).
    shutil.rmtree(path)

    pass