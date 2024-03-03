import os

def checkExistence(path):
    if os.path.exists(path):
        print('path exist')
    else:
        print('the path does not exist')


checkExistence(r"C:\Users\HUAWEI\Desktop\study\certificates\Coursera FFDJZNXQ4H5U.pdf") # real path
checkExistence(r"C:\Users\HUAWEI\Desktop\study\Coursera FFDJZNXQ4H5U.pdf") # does not exist

