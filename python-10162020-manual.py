print("hello world")
lst=[2,4,5]
# print(lst*2)
lst.extend('python')
lst.append('NEW')
print(lst)
files=['first.py','second','third.py','4th','fifth','1.py']
print(files)

for file in files:
    if file.endswith('py'):
        print(file)
print("*****************")
for file in files:
    if file[len(file)-3:] == '.py':
        print(file)
names=[]
print("*****************")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
print("*****************")
tp = (2,'four',5,'p','y','t','h','o','n','NEW')
print(type(tp))
print(tp[0])
print(tp.count(2))
print(tp.index(2))
print(tp.count(5))
print(tp.index(5))
s=''
for ele in tp:
    s = s+str(ele)
    print(s)
print("*****************")
# ss=''
# print(''.join(tp))    
    
mydict = {'name':'akash','age': 26}
print(type(mydict))
print(mydict['name'])
print("*****************")
names = ('akash','vikas','john','alex')
print('-'.join(names))