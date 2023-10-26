from abc import ABC, abstractmethod

class Shape(ABC):
    def shape(self, name):
        self.name = name
    
    @abstractmethod
    def cal_area(self):
           pass

class Circle(Shape):
    def cal_area(self,radius):
     self.radius = radius
     area = 3.14 * (self.radius*self.radius)
     print(f'The area of a circle is: {area}')

class Rectangle(Shape):
     def cal_area(self,length,width):
         self.length = length
         self.width = width
         rectangle_area = self.width*self.length
         print(f'The area of a rectangle is: {rectangle_area}')


class Triangle(Shape):
    def cal_area(self,base,height):
        self.base = base
        self.height = height
        triangle_area = 0.5 * base * height
        print(f'The area of the triangle is: {triangle_area}')
print('..........Calculations of the circle.......')        
cir1 =  Circle()
cir1.cal_area(int(input('Enter the radius : ')))
cir1.name = input('Enter the circle name: ')
print(f'CircleName: {cir1.name}')
print('============================================')
print('..........Calculations of the Recatangle...........')
rect1 = Rectangle()
rect1.cal_area(
    int(input('Enter the length: ')),
    int(input('Enter the width: '))
)
rect1.name = input('Enter the  rectangle name: ')
print(f'RectangleName: {rect1.name}')
print('=================================================')
print('.............Calculations of the Triangle........')
tria1 = Triangle()
tria1.cal_area(
    int(input('Enter the triangle base value: ')),
    int(input('Enter the triangle height: '))
)
tria1.name = input('Enter the triangle name: ')
print(f'TriangleName: {tria1.name}')
#cir1.cal_area(10.0)
# print(cir1.area)