'''
Find cross product of 2 points in a 2-D plane
Here point is a tuple denoting (x,y) coordinates
'''

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def cross_product(point1,point2):
    return point1.x*point2.y-point1.y*point2.x


def area_triangle(p1,p2):
    #assuming 1 point at origin
    return abs(cross_product(p1,p2))/2

if __name__ == '__main__':
    p1= Point(5,10)
    p2= Point(2,2)

    print cross_product(p1,p2)

    print area_triangle(p1,p2)
