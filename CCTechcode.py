class Point:
	def __init__(self, xloc, yloc):
		self.x = xloc
		self.y = yloc
		
	def values(self):
		return (self.x, self.y)

    
class Polygon:
	def __init__(self, pointlist):
		self.edges = set() #set of all edges
		self.fill_edges(pointlist)
	
	def add_edge(self, v1, v2):
		temptup = (v1, v2) #makes the edge a tuple so its easier to pass into a set
		self.edges.add(temptup)
	
	def fill_edges(self, pointlist): #connects points with edges in order of entry
		for item in range(len(pointlist)-1):
			self.add_edge(pointlist[item], pointlist[item+1])
			self.add_edge(pointlist[-1], pointlist[0])


def turn(A, B, C):
	N = (C.y - A.y) * (B.x - A.x)
	M = (B.y - A.y) * (C.x - A.x)
	if N > M:
		return 1 #counterclockwise rotation through A-B-C
	if M > N:
		return -1 #clockwise rotation
	return 0 # no rotation (duplicate points)
	
def checkintersect(A, B, C, D): #lines are A-B and C-D
	return (turn(A, C, D) != turn(B, C, D)) and (turn(A, B, C) != turn(A, B, D))

def checkbounds(polygon, point, refpoint=Point(0, 0)): #default refpoint set to (0, 0)
	# ####### refpoint must be outside of the polygon
	count_intersects = 0
	for edge in polygon.edges:
		# print(edge[0].values(), edge[1].values()) #shows edges for debug
		
		#two point objects from the polygon then two to test
		intersected = checkintersect(edge[0], edge[1], point, refpoint)
		count_intersects = count_intersects + intersected
		
	return count_intersects
		
def inregion(intercepts):
	if (intercepts % 2 == 1): #modular division to check if the value is odd or even
		print("inside region")
	else:
		print("outside region")
        
        
def main():
	point1 = Point(53.531170, -113.492482)
	point2 = Point(53.558731, -113.508459)
	point3 = Point(53.558765, -113.535575)
	point4 = Point(53.541528, -113.535824)
    
	testx = float(input('x value: '))
	testy = float(input('y value: '))
	
	testpoint = Point(testx, testy)
	intercepts = checkbounds(poly, testpoint)
	print('Intercepts: ', intercepts)
	inregion(intercepts)