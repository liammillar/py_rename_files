import os
def rename_files():

    # (1) Get file names from a folder
    file_list = os.listdir(r"C:\Python27\apps\test")
    print (file_list)
    # (2) for each file, rename filename

rename_files()
