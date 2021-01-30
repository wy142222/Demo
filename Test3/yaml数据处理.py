import yaml

# print(yaml.load("""
# - a
# - b
# - c
# - d
# """,Loader=yaml.FullLoader))
# print(yaml.load("""
# a: 1
# b: 2
# c: 3
# """,Loader=yaml.FullLoader))
#load将yaml格式转化成python格式
# yl=yaml.load(open("demo.yml"),Loader=yaml.FullLoader)
# print(yl)
#dump将python格式转化成yaml格式
# print(yaml.dump([1, 2, 3]))
# print(yaml.dump({"a":1,"b":"b1"}))
lt=[1,3,5,{"a":"a1"},["b1","b2","b3"]]
with open("demo1.yml","w") as f:
    yaml.dump(data=lt,stream=f)



