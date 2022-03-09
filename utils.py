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
def getPointData(n, length=100, width=100, depth=100):
    points = np.random.rand(n, 3)
    points[:,0] = np.interp(points[:,0], [0,1], [-length // 2, length // 2])
    points[:,1] = np.interp(points[:,1], [0,1], [-width // 2, width // 2])
    points[:,2] = np.interp(points[:,1], [0,1], [-depth // 2, depth // 2])
    return points

# [I] points, np.ndarray (n, 3)
# [O] path, np.ndarray (n), series of indices by which to define a path
def findPath(points):
    return np.arange(len(points))

def BFS(points):
    pass

def DFS(points):
    pass