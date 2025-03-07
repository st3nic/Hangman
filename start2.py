import datetime

current_time = datetime.datetime.now()

name = input(str('Please enter your name: '))

if current_time.time() < datetime.time(12):
    print('Good Morning ' + name)
else:
    print('Good Afternoon ' + name)