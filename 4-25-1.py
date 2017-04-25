#! usr/bin/env python3
#coding: utf-8
class Animal(object) :
    def run(self) :
        print("Animal is runing...")

class Dog(Animal) :
    def run(self) :
        print("Dog is running...")
class Cat(Animal) :
    def run(self) :
        pass // 覆盖了原来的run但是又pass了，所以cat的run什么也不会输出2333

def run_twice(animal) :
    animal.run()
    animal.run()
a = Animal()
b =  Dog()
c = Cat()
a.run()
b.run()
c.run()
print(isinstance(a,Animal))
print(isinstance(b,Animal))
print(isinstance(c,Cat))
run_twice(a)
run_twice(b)
run_twice(c)
