'''
Determine whether a point lies to the left or right of a line usinf cross product.

If cross_product is negtative:
    point lies to right
elif cross_product is positive:
    point lies to left
else:
    point lies on line

Practical usecase of this can be seen in maps to check whether user has to take left or right turn to reach a given point

'''
import locale

from Python_DS.Maths import Cross_product as cp



def point_location(point, line_point1, line_point2):
    point= adjust_point(point, line_point1)
    line_point2= adjust_point(line_point2,line_point1)

    result= cp.cross_product(line_point2,point)
    if result<0:
        print "Point lies to the RIGHT of the line"
    elif result>0:
        print "Point lies to the LEFT of the line"
    else:
        print "Point lies on the line"

def adjust_point(point1,base_point):
    return cp.Point(point1.x-base_point.x,point1.y-base_point.y)


if __name__ == '__main__':
    line_point1= cp.Point(-30,10)
    line_point2= cp.Point(30,-15)

    p1 = cp.Point(15,28)
    p2 = cp.Point(-50,-100)
    p3 = cp.Point(0,0)
    # print adjust_point(line_point2,line_point1)

    point_location(p1, line_point1,line_point2)
    point_location(p2, line_point1,line_point2)
    point_location(p3, line_point1,line_point2)
    point_location(line_point1,line_point1,line_point2)
