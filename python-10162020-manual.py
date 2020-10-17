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