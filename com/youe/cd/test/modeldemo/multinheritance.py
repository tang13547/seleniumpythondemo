class X():
    def f(self):
        print("x")

class A(X):
    def f(self):
        print("a")

    def extral(self):
            print("extral a")

class B(X):
    def f(self):
        print("b")

    def extral(self):
            print("extral b")

class C(A, B, X):
    def f(self):
        super(C, self).f()
        print("c")

#查找顺序MRO（MRO即method resolution order，用于判断子类调用的属性来自于哪个父类）
print(C.mro())

c = C()
c.f()
c.extral()