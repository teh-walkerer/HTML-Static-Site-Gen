import os
import shutil

# This function copies all contents from a source directory into a destination
# In this case, static to public
# It deletes contents of the destination (public) to ensure the copy is clean
# It logs the path of each file copies
print(os.listdir())
print(os.listdir("/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/src"))
for file in os.listdir("/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/src"):
    print(os.path.isfile(f"/home/munch/Projects/github.com/teh-walkerer/HTML-Static-Site-Gen/src/{file}"))
def recursive_copy():

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