import bpy
import numpy as np

from utils import *

if __name__ == "__main__":
    
    clearScene()
    clearKeyFrames()

    points = getPointData(10000)
    path = findPath(points)

    