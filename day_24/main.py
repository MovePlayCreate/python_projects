# with open("/Users/patrick/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("../Users/patrick/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("../../../Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
    
# test this to see if it worked later.
# written while in a Lyft to Boise airport
with open("../../../Desktop/my_file.txt", mode="w") as data_file:
    data_file.write("working?") 
    