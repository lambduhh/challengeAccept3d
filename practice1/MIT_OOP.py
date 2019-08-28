# Object Oriented Programming a lecture from Dr. Ana from MIT avalible under Creative Commons on Youtube

# creating a class and defining it's type
# an object that defines a point in an (x,y) plane


class Coordinate(object):  # class definition, Name/type (class parent)
    def __init__(self, x, y):  # create an instance of object to initialize data attributes
        self.x = x  # self is a parameter/ place holder for any instance
        self.y = y  # 2 data attributes of every Coordinate object

    def distance(self, other):  # a method to find distance
        x_diff_sq = (self.x - other.x) ** 2  # use dot notation to access data
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):  # str returns str - makes print(c) return actual useful info
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Fraction(object):
    def __init__(self, num, denom):  # num and denum are integers
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denum = denom

    def __str__(self):  # returns a str representation
        return str(self.num) + "." + str(self.denum)

    def __add__(self, other):  # returns a new fraction representation of added fractions
        top = self.num * other.denum + self.denum * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)  # a new object that is of the same class as Fraction

    def __float__(self):  # returns float value of fraction
        return self.num / self.denum


# if you want to use special operators such as add,sub,eq,len etc you need to indicate
# in your class

if __name__ == '__main__':
    c = Coordinate(3, 4)  # how to USE the method
    zero = Coordinate(0, 0)
    print(c.distance(zero))  # conventional way
    #   (obj to call method on.METHOD(parameters to pass to method))
    print(Coordinate.distance(c, zero))  # same as above
    #   (name of class.METHOD(self=c, other=zero)
    print(c)  # before adding __str__ this results in uninformative print statement
    print(type(c))  # asks for TYPE of object instance
    print(isinstance(c, Coordinate))  # checks if an object is a Coordinate

    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b  # bc we added the __add__ method on Fraction, it creates a Fraction object
    print(c)
