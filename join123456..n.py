a=[]
a.extend(list(range(11)))
print(a)
#ceating new list with elemnet changed into string
b=[]
for x in a:
    b.append(str(x))
print(b)

# join function on new b 
# syn "".join(str element)
c="".join(b)
print(c)
