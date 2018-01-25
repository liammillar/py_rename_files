import os
def rename_files():

    # (1) Get file names from a folder
    test_path = r"C:\Python27\apps\test"
    file_list = os.listdir(test_path)
    print (file_list)
    saved_path = os.getcwd()
    os.chdir(test_path)
    
    # (2) for each file, rename filename
    
    for file_name in file_list:
       os.rename(file_name,file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
rename_files()
