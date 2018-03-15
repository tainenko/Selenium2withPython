from time import sleep, ctime

def music(func,loop):
    for i in range(loop):
        print('I was lisstening to ',func,ctime())
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print('I was at the ',func,ctime())
        sleep(5)

if __name__=='__main__':
    music('愛情買賣',2)
    movie('阿凡達',2)
    print('all ned:',ctime())