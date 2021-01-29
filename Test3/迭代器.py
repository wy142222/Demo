# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象print (next(it))   # 输出迭代器的下一个元素
# print (next(it))
# print(it)
# for i in it:
#     print(i)
# print (next(it))
# a=[1,2,3,"a"]
# b=(4,"a",3)
# c={7,555,355}
# d={"name":"lili","sex":"f"}
#
# e=d["name"]
# print(e)
# f="name is {2}".format(*a)
# print(f)
file=open("/Users/wangyue/Desktop/测试.txt","w",)
list02 = ["11","test","hehe","44","55\n"]
tuple01 = ("wwsf1","tgagst","gagaghe","44","ga5\n")
dict1={"ww":"ee","aa":"22\n"}

file.writelines(list02)
file.writelines(tuple01)
file.writelines(dict1.values())
file.close()
file1=open("/Users/wangyue/Desktop/测试.txt","r",)
# while True:
#     f1 = file1.readlines()
#     if f1:
#         print(f1,end="")
#     else:
#         break
f1=file1.readlines()
for i in f1:
    print(i,end="")
# while(file1.readline()):
#     print(file1.readline())

