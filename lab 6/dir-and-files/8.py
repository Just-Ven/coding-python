import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.R_OK):
        os.remove(path)

delete_file(r"C:\Users\HUAWEI\Desktop\coding\pp2\lab 6\dir-and-files\example5.txt")
