'''
继承和多态
'''

# 定义一个超类
class Animal(object):
    def run(self):
        print('Animal is running')
    def eat(self):
        print('Eating meat ...')

# 继承超类
class Dog(Animal):
    # 覆盖超类的方法
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


d = Dog()
d.run()
d.eat()

# 类型检测，ｄ属于Animal同时也属于Dog类型
r = isinstance(d,Animal)
r = isinstance(d, Dog)
print(r)

def run_twice(animal):
    animal.run()


# 多态
'''
由于Animal类型有run()方法，因此，传入的任意类型
只要是Animal类或者子类，就会自动调用实际类型的run()方法，
这就是多态
'''
'''
对于一个变量，我们只需要知道它是Animal类型
无需确切地知道它的子类型，就可以放心地调用run()方法
而具体调用的run()方法是由运行时该对象的确切类型决定，
这就是多态真正的威力：
调用方只管调用，不管细节，而当我们新增一种Animal的子类时
只要确保run()方法编写正确，不用管原来的代码是如何调用的。
'''
run_twice(d)
run_twice(Cat())
run_twice(Animal())
# Dog is running...
# Cat is running...
# Animal is running
