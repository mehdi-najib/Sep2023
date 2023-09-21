a={}
print(type(a))
b=[]
print(type(b))
a["ali"]= '091212'
a['meiti']='0036'
a['taghi']='05565'
a['mamad']='65658'
a['reza']='0935'
del a['mamad']
b=a.get('ali')
a['naghi']='0817'
#print(a)
for i in a:
    print (i)
#print(b)