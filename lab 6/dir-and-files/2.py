import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"The path exist.")
    else:
        print(f"The path exists.")

    if os.access(path, os.R_OK):
        print("Read access: Yes")
    else:
        print("Read access: No")

    if os.access(path, os.W_OK):
        print("Write access: Yes")
    else:
        print("Write access: No")

    if os.access(path, os.X_OK):
        print("Execute access: Yes")
    else:
        print("Execute access: No")

check_path_access(r"C:\Users\HUAWEI\Desktop\study\certificates\Coursera FFDJZNXQ4H5U.pdf")
print()
check_path_access(r"C:\Users\HUAWEI\Desktop\study\Coursera FFDJZNXQ4H5U.pdf")
