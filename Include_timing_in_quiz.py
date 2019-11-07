import time
option = 'global'
def answer():
    start = time.time()
    option = input("enter you choice:")
    end = time.time()  - start
    endtime = round(end)
    if endtime <= 7:
        print('safe')
    else:
        print('died')
answer()

if option <= '5':
    print('story')
else:
    print('no story')
