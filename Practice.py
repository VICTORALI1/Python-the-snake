import os

from datetime import datetime

nums = [1, 2, 3, 4, 5]

'''def intro(**data):
    print("\nData type of argument:", type(data))
    for key, value in data.items():
        print("{} : {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)'''

'''def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(leap_year(2100))'''
'''print(os.getcwd())

os.makedirs('OS-DEMO-2/Sub-Dir-1')
print(os.listdir())'''

# os.chdir('/home/investor/Desktop/Documents')

# print(os.getcwd())
# print(os.listdir())
# time=os.stat('firebase2').st_mtime
# print(datetime.fromtimestamp(time))

'''for dirpath,dirname,filename in os.walk('/home/investor/Desktop/Documents'):
    print('dirpath :', dirpath)
    print('name : ', dirname)
    print('filename: ', filename)
    print()'''
# print(os.environ.get('HOME'))


# Reading and writing to a file
'''print(os.listdir())
f = open("Presly's Resume..odt", 'r')
print(f.mode)
f.close()'''

with open('My Cv.txt', 'r') as rf:
    with open('Cover Letter.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
