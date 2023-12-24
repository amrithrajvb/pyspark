# import threading
#
# from threading import *
#
# from time import sleep
#
#
# def print_cube(num):
#     # function to print cube of given num
#     print("Cube: {}".format(num * num * num))
#
#
# def print_square(num):
#     # function to print square of given num
#     print("Square: {}".format(num * num))
#
#
# if __name__ == "__main__":
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(20,))
#
#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()
#
#     # wait until thread 1 is completely executed
#     t1.join()
#     # wait until thread 2 is completely executed
#     t2.join()
#
#     # both threads completely executed
#     print("Done!")


# class cases

# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("hai")
#             sleep(1)
#
#
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("halo")
#             sleep(1)
#
# t1=A()
# t2=B()
# t1.start()
# t2.start()



# import threading
# import time
#
# def print_numbers():
#     for i in range(1,6):
#         print("Printing number {}".format(i))
#         time.sleep(1)
#
# def print_letters():
#     for i in "covid":
#         print("print letters {}".format(i))
#         time.sleep(1)
#
# t1=threading.Thread(target=print_numbers)
# t2=threading.Thread(target=print_letters)
# t1.start()
# t2.start()
# t1.join()
# t2.join()



import unittest

class Test_new(unittest.TestCase):

    def sums(self,num1,num2):
        return num1+num2

    def setUp(self):
        print("start")
        self.a=20
        self.b=30

    def test_case1(self):
        print("hai")
        result=self.sums(self.a,self.b)
        self.assertEqual(result,self.a+self.b)

    def test_case2(self):
        print("hai")


if __name__=="__main__":
    unittest.main()
