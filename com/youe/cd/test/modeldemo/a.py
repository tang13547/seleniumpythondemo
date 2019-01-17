class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


if __name__ == "__main__":
    a = A()

    print(a.foo(1))
    print(a.class_foo(2))
    print(a.static_foo(3))

    print("#################")

    #print(A.foo(1))    #不能这样使用
    print(A.class_foo(2))
    print(A.static_foo(3))