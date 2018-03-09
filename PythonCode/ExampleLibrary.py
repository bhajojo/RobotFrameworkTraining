class ExampleLibrary:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._counter = 0

    def count(self):
        self._counter += 1
        print self._counter

    def clear_counter(self):
        self._counter = 0

    def PrintHello(self):
        print "Hello World"

    def PrintHello1(self):
        print "Hello World"


    def PrintHello2(self):
        print "Hello World"

    def fib(self,n):  # write Fibonacci series up to n
        a, b = 0, 1
        while b < n:
            print b,
            a, b = b, a + b