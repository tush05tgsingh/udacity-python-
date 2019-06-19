import os
import string
def rename_files():
    #(1) get file names from folder
    file_list = os.listdir(r"/Users/tgsingh/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is" + saved_path)
    os.chdir(r"/Users/tgsingh/Downloads/prank")
    
    #(2) for each file, rename filename
    file_table=str.maketrans("0123456789","          ","0123456789")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(file_table))
    os.chdir(saved_path)
    
rename_files()    
