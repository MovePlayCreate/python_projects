# with open("/Users/patrick/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("../Users/patrick/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("../../../Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)