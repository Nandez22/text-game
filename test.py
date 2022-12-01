resolution = '1920 x 1080'
print(resolution)

def getRes(resolution):
    res = ''
    for char in  resolution:
        try:
            int(char)
            res += char
        except:
            if char == 'x':
                res += ','
            pass
    res = res.split(',')
    res = int(res[0]),int(res[1])
    return res
print(getRes(resolution))




from pygame.locals import *

mode = 'FULLSCREEN'

def getMode(input):
    if input == 'FULLSCREEN':
        mode = FULLSCREEN
    if input == 'BORDERLESS':
        mode = NOFRAME
    if input == 'WINDOWED':
        mode = RESIZABLE
    return mode
