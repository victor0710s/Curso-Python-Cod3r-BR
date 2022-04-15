#! python
file = open('people.csv')
data = file.read()
file.close()
for register in data.splitlines():
    print('Name: {}, Age: {}'.format(*register.split(',')))
