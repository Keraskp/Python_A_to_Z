from threading import *
class Hello(Thread):
    def run(self):
        for i in range(500):
            print('Hello')
            
class Hi(Thread):
    def run(self):
        for i in range(500):
            print('Hi')
            
#Now if we want to create threads, we have to use start() method, it will internally call run()
t1 = Hello()
t2 = Hi()

t1.start()
t2.start()