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
    

print("*****************")
names = ('akash','vikas','john','alex')
print('-'.join(names))

mydict = {'name':'akash','age': 26}
print(type(mydict))
print(mydict['name'])
# print(mydict(0))
d = {}
print(type(d))
d['a'] = 'one'
print(len(d))
print(d['a'])
d['a'] += 'two'
print(d)
print("*****************")
for i in mydict:
    print(i)
    print(mydict[i])
print("*****************")
for i in mydict.values():
    print(i)
    # print(mydict[i])
print("*****************")
for i in mydict.keys():
    print(i)
    # print(mydict[i])

print(mydict.keys())
print(mydict.values())
print(mydict.items())

print("*****************")
for i in mydict.items():
    print(i)

print("*****************")
for i in mydict.items():
    print(i[0],'->',i[1])
print("*****************")
ladies_purse = {'cards':['Amex','IcICI'], 'cash': 1800, 'candies': 3}
print(ladies_purse)
for key in ladies_purse.keys():
    # print(key)
    # print(ladies_purse[key])
    if(key == 'cards'):
        # print(ladies_purse[key])
        for val in ladies_purse[key]:
            # print(val)
            if val == 'IcICI':
                print(val[1])
print("*****************")
lad = {'cards':['Amex','IciCI'],'cash':1800}
s = lad['cards']
print(s)
print(s[1][1])
print("*****************")
print(ladies_purse.get('cards')[1][1])