def add(a,b):
	return a+b

a = 1
b = 2
c = add(a,b)
with open("./result.txt","w",encoding="utf8") as f:
    f.write("{}+{}={}".format(a,b,c))