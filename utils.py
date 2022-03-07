import bpy
import numpy as np

#################################### ANIMATION

def clearScene():
    pass

def clearKeyFrames():
    pass



#################################### DATA PROCESSING

# creates n 3d points bounded to a cubic plot size
# if it exists, only samples points within a sampling mesh's boundary
# [I] n, integer
# [O] arr, np.ndarray (n, 3)
def getPointData(n):
    pass

# [I] points, np.ndarray (n, 3)
# [O] path, np.ndarray (n), series of indices by which to define a path
def findPath(points):
    pass

def BFS(points):
    pass

def DFS(points):
    pass