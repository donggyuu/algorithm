import time

# --------------------------------------------------
# START : Setting your own
# --------------------------------------------------
heartSpeed = 0.5 # second
heartShape = '*' # character that consist of heart

inputNameMessage = 'What is your name?: '
greetingMessage = 'Happy birthday ' # Happy birthday donggyu!
yourMessage = 'If the sun were to rise in the west, my love would be unchanged forever'
# --------------------------------------------------
# END : Setting your own
# --------------------------------------------------


# --------------------------------------------------
def makeHeart(heartShape, heartSpeed):
    print('\n')

    # upper heart
    for i in range(4, 10, 2):
        for j in range(10-i+1):
            print(" ", end='')
        for j in range(i*2+1):
            print(heartShape, end='')
        for j in range((10-i+1)*2):
            print(" ", end='')
        for j in range(i*2+1):
            print(heartShape, end='')
        print('', sep='\n')
        time.sleep(heartSpeed)

    # lower heart
    for i in range(20, -2, -2):
        for j in range(22-i+1):
            print(" ", end='')
        for j in range(i*2-1):
            print(heartShape, end='')
        print('', sep='\n')
        time.sleep(heartSpeed)

    return

def getMessage(greetingMessage, yourMessage, heartSpeed):
    time.sleep(heartSpeed)
    print(greetingMessage + inputName)
    time.sleep(heartSpeed*2)
    print('', sep='\n')
    print(yourMessage)
    time.sleep(heartSpeed*2)

inputName = input(inputNameMessage)
makeHeart(heartShape, heartSpeed)
getMessage(greetingMessage, yourMessage, heartSpeed)

print('\n')