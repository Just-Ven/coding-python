# example стоит на рабочем столе
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
    print(line_count)

count_lines(r"C:\Users\HUAWEI\Desktop\example.txt")