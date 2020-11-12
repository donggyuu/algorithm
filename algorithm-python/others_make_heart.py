import time

def makeHeart():
    print('\n')

    # upper heart
    for i in range(4, 10, 2):
        for j in range(10-i+1):
            print(" ", end='')
        for j in range(i*2+1):
            print("*", end='')
        for j in range((10-i+1)*2):
            print(" ", end='')
        for j in range(i*2+1):
            print("*", end='')
        print('', sep='\n')
        #time.sleep(0.5)

    # lower heart
    for i in range(20, -2, -2):
        for j in range(22-i+1):
            print(" ", end='')
        for j in range(i*2-1):
            print("*", end='')
        print('', sep='\n')
        #time.sleep(0.5)

print(makeHeart())
