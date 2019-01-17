class Rectangle():
    def __init__(self, width_=0, height_=0):
        self._width = width_
        self._height = height_

    @property
    def width(self):
        #变量名不与方法名重复，改为true_width，下同
        return self._width

    @property
    def height(self):
        return self._height

s = Rectangle()
#与方法名一致
# s.width = 1024
# s.height = 768

#因为使用了@property为私有属性(width和height，注意不是_width和_height; 即相当时单独又定义了一些新私有属性)，所以不能按上面方式赋值(写)，只可读,如下：
print(s.width,s.height)