def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
result = add_10(3)
print result
print create_adder(123)(123)

print (lambda x: x > 2)(3)

import math
print dir(math)

import time
import thread
def timer(no, interval):
    cnt = 0
    while cnt<10:
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())
        time.sleep(interval)
        cnt+=1
    thread.exit_thread()

def test():
    thread.start_new_thread(timer, (1,1))
    thread.start_new_thread(timer, (2,2))

if __name__=='__main__':
    test()