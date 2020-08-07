# data = open("새파일.txt", "r")
#
# for str in data.readlines():
#     print(str, end="")
# data.close()


with open("새파일.txt", 'r') as file:
    for str in file.readlines():
        print(str, end="")