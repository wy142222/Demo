a=[1,2,2]
try:
    if a>0:
        print("{}是正数".format(a))
    elif a==0:
        print("{}是0".format(a))
    else:
        print("{}是负数".format(a))

except:
    print("{}不是数字".format(a))
finally:
    print(a)