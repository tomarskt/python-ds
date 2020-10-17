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

long_name=[]
names = ['akash','Alexander','Frederick', 'Jean', 'Murlidhar']
for name in names:
    if len(name)>6:
        long_name.append(name)
print(long_name)
# gen_names =
print([name for name in names if len(name)>6])

print([x**2 for x in range(10)])
x=10
y=20
print(x-y) if x>y else print(y-x)
print("*****************")
x = []
for x in range(10):
    y=x**2
    print(y)
print("*****************")

def greeting():
    print("*****************")
    print("hello...")
    print("welcome to data scirnce course")
    print("we have just started")
    print("end of function")
greeting()
greeting()

def greeting1(name):
    print("*****************")
    print("hello...",name)
    print("welcome to data scirnce course")
    print("we have just started")
    print("end of function")

greeting1("sudhir")

print("*****************")
def func(name, age):
    print(f"hi {name}")
    print(f'you will be {age+5} yrs old in 2025')

func("sudhir",40)

print("*****************")
def func2(name, age=25):
    print(f"hi {name}")
    print(f'you will be {age+5} yrs old in 2025')

func2("mohan",30)
func2("ganesh")

print("*****************")
def func3(name, age=25, ph='92853'):
    print(f"hi {name}")
    print(f'you will be {age+5} yrs old in 2025')
    print(ph)

func3('Alex',ph=8377, age=27)
print("*****************")
func3(name='sudhir',age = 20, ph=8377)

print("*****************")
func3(age = 20, ph=8377,name='raman')


print("*****************")
def func4(name, gender, city, age=25, ph='92853'):
    print(f"hi {name}")
    print(f'you will be {age+5} yrs old in 2025')
    print(ph)
    print(city)
    print(gender)

func4('Akash','M',ph='7366',city='Meerut')

print("*****************")
def func5(*details, age=25, ph='92853'):
    print(f"hi {details}")
    print(f'you will be {age+5} yrs old in 2025')
    print(ph)

func5('Akash','M','Meerut',ph='7366')

print("*****************")
def func6(*args, age=25, ph='92853'):
    print(f"hi {args}")
    print(f"hi {args[0]}")
    print(f'you will be {age+5} yrs old in 2025')
    print(ph)

func6('Akash','M','Meerut',ph='7366')