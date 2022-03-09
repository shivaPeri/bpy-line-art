import bpy
import numpy as np

#################################### ANIMATION

def clearScene():
    for obj in bpy.context.scene.objects:
        if obj.type in ['MESH']:
            if obj.name == 'Container':
                obj.select_set(False)
                continue
            obj.select_set(True)
        else:
            obj.select_set(False)
    bpy.ops.object.delete()

def clearKeyFrames():
    pass


#################################### NUMPY -> BPY UTILS

# [I] points, np.ndarray (n, 3)
# [I] path, np.ndarray (n), series of indices by which to define a path
# [O] obj, bpy object reference
def createSpline(path, points, name='spline'):

    bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.curve.subdivide(number_cuts=len(points) // 4)

    for i, p in enumerate(bpy.context.object.data.splines.active.points):
        try:
            p.co.x = points[path[i], 0]
            p.co.y = points[path[i], 1]
            p.co.z = points[path[i], 2]
        except:
            pass


    # for ind in path:
    #     # bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":points[ind] })
    #     bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":points[ind], "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


    # # make a new curve
    # crv = bpy.data.curves.new('crv', 'CURVE')
    # crv.dimensions = '3D'

    # # make a new spline in that curve
    # spline = crv.splines.new(type='BEZIER')
    # spline.points.add(len(path)-1)

    # # assign the point coordinates to the spline points
    # for p, ind in zip(spline.points, path):
    #     p.co = (points[ind])

    # make a new object with the curve
    # obj = bpy.data.objects.new(name, crv)
    # bpy.context.scene.collection.objects.link(obj)
    # return obj
    bpy.ops.object.mode_set(mode='OBJECT')

#################################### DATA PROCESSING

# creates n 3d points bounded to a cubic plot size
# if it exists, only samples points within a sampling mesh's boundary
# [I] n, integer
# [O] arr, np.ndarray (n, 3)
def getPointData(n, length=100, width=100, depth=100):
    points = np.random.rand(n, 3)
    points[:,0] = np.interp(points[:,0], [0,1], [-length // 2, length // 2])
    points[:,1] = np.interp(points[:,1], [0,1], [-width // 2, width // 2])
    points[:,2] = np.interp(points[:,2], [0,1], [-depth // 2, depth // 2])
    print(points)
    return points

# [I] points, np.ndarray (n, 3)
# [O] path, np.ndarray (n), series of indices by which to define a path
def findPath(points):
    return np.arange(len(points))

def BFS(points):
    pass

def DFS(points):
    pass

if __name__ == "__main__":
    
    # clearScene()
    # clearKeyFrames()

    points = getPointData(1000)
    path = findPath(points)

    curve = createSpline(path, points, 'test')
    curve.data.bevel_mode = 'ROUND'
    curve.data.bevel_depth = 1
    curve.data.use_fill_caps = True

    