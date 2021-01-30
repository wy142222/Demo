import os

# os.getcwd()
# # os.mkdir("testdir")
# print(os.listdir("./"))
# os.removedirs("testdir")
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not(os.path.exists("b/test.txt")):
    with open("b/test.txt","w") as f:
        f.writelines("nihao")
