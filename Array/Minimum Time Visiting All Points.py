# Time complexity O(n)
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        total=0
        for i in range(len(points)-1):
            x1,y1=points[i]
            x2,y2=points[i+1]
            dx=abs(x2-x1)
            dy=abs(y2-y1) 
            total+=max(dx,dy)  
        return total
