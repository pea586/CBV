from django.test import TestCase

# Create your tests here.

class Animal:
    def __init__(self, name, age, func):
        self.name = name
        self.age = age
        # self.sleep()
        f = getattr(self, func)
        f()
    def sleep(self):
        print('睡觉。。。')

    def eat(self):
        print('吃东西')

class Dog(Animal):
    def wangwang(self):
        print('旺旺叫')

    def sleep(self):
        print('趴着睡')

xiaohua = Dog('xiaohua', 7, 'sleep')


