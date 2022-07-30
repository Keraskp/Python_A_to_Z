#!/usr/bin/python3
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(0.5)
class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(0.5)

t1 = Hello()
t2 = Hi()

# t1.run() #Hello printed 5 times
# t2.run() #Hi printed 5 times

#To use Threads in classes, we must use higher level thread API
# After the classes are declared as derived classes of class Thread

# t1.start() #Call start method, it internally calls run() method
# sleep(0.2) #sleep between them make sures that there are no collisions
# t2.start()
# print('Bye') #Bye is printed in between because there are 3 threads working parallely

#After we create thread using start() method, we have three Threads :
#1. Main Thread
#2. t1
#3. t2

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()


#join() function halts main() Thread.
print('Bye')