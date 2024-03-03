def write_list_to_file(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')

list = [1, 2, 3, 4, 5, 6]
write_list_to_file(r"C:\Users\HUAWEI\Desktop\coding\pp2\lab 6\dir-and-files\example2.txt", list)

f = open(r"C:\Users\HUAWEI\Desktop\coding\pp2\lab 6\dir-and-files\example2.txt", 'r')
print(f.read())