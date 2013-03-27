import time


def lots_of_second(second):
    t1 = time.time()
    for i in range(0, second):
        print(i)
    t2 = time.time()
    print('it took %s seconds' % (t2 - t1))


lots_of_second(100000)