def copy(file1, file2):
    with open(file1, 'r') as f1:
        content = f1.read()

    with open(file2, 'w') as f2:
        f2.write(content)

copy(r"C:\Users\HUAWEI\Desktop\coding\pp2\lab 6\dir-and-files\example3.txt", r"C:\Users\HUAWEI\Desktop\coding\pp2\lab 6\dir-and-files\example4.txt")
