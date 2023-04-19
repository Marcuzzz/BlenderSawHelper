import bpy
import time
import math
import numpy as np

# from bpy import data

bl_info = {
    "name": "MySawHelper",
    "description": "MySawHelper",
    "author": "Marc Otten",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "category": "Scripts",
    "location": "Scripts > MySawHelper",
}


def show_popup_message(title, message):
    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title=title, icon='ERROR')

def bprint(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")       

def setViewport():
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            for space in area.spaces: 
                if space.type == 'VIEW_3D':
                    space.shading.type = 'MATERIAL'

def createPlank(name,scale,color,x =0, y = 0, z = 0, makematerial = True, center = False):
    
    if makematerial:
        mat = bpy.data.materials.new(name=name+"_material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        principled_bsdf = nodes.get("Principled BSDF")
        if principled_bsdf is not None:
            principled_bsdf.inputs["Base Color"].default_value = color  # set the color to red
    
    if not center:
        x = -(scale[0]/2) + x
        y = -(scale[1]/2) + y
    else:
        x = 0 + x
        y = 0 + y
            
    # Add a new cube mesh
    mesh = bpy.ops.mesh.primitive_cube_add(
        size=1,
        enter_editmode=False,
        align='WORLD',
        location=(x, y, z),
        scale=scale,
    )
    
    if makematerial:
        bpy.context.active_object.data.materials.append(mat)
    bpy.context.active_object.name = name
    
    return bpy.context.active_object


def createOtherPlanks(mainplank,plank_dims,cut,colors,coll,depth=0.018):
    x, y = 0, 0

    savey = 0

    for a,plank_dim in enumerate(plank_dims):

        abort = False
        # Check if the plank can fit horizontally
        if plank_dim[0] > mainplank[0] or plank_dim[1] > mainplank[1]:
            abort = True

        if not abort:
            if x + plank_dim[0] <= mainplank[0]:
                if x > 0:
                    x += cut

                plank = createPlank("a_" + str(a),(plank_dim[0],plank_dim[1],depth),tuple(colors[a]), x = -x, y = -y, z = 0)
                removefrom = plank.users_collection
                coll.objects.link(plank)
                removefrom[0].objects.unlink(plank)
                x += plank_dim[0]
                
                print(x,y,'added hor')

                savey = plank_dim[1] + cut
            # Check if the plank can fit vertically
            elif y + plank_dim[1] <= mainplank[1]:
                x = 0

                if savey > 0:
                    y += savey
                    savey = 0
                else:
                    y += plank_dim[1] + cut

                plank = createPlank("a_" + str(a),(plank_dim[0],plank_dim[1],depth),tuple(colors[a]), x = -x, y = -y, z = 0)
                removefrom = plank.users_collection
                coll.objects.link(plank)
                removefrom[0].objects.unlink(plank)
                x += plank_dim[0]
                print(x,y,'added ver')
            else:
                print(f"we need another plaat for this {plank_dim}")
                abort = True
            
        if abort:
            print(f"Can't fit plank with dimensions {plank_dim}")


def initBoundries(width,length,height):
    
    #coll = bpy.ops.collection.create(name  = "MyTestCollection")
    #bpy.context.scene.collection.children.link(bpy.data.collections["MyTestCollection"])
    coll = bpy.data.collections.new(name  = "SawExampleCollection")
    scene_collection = bpy.context.scene.collection
    scene_collection.children.link(coll)
    
    
    #create some random colors
    colors_without_alpha = np.round(np.random.rand(2, 3),1)
    colors = np.column_stack((colors_without_alpha, np.ones(colors_without_alpha.shape[0])))
    
    #ref rect
    blength = math.floor(length)+1
    bwidth = math.floor(width)+1
    plank = createPlank('plank01',(blength,bwidth,height),tuple(colors[0]),z = -(height*2))
    removefrom = plank.users_collection
    coll.objects.link(plank)
    removefrom[0].objects.unlink(plank)
    
    #bpy.data.collections['Collection'].objects.unlink(plank)
    
    plank = createPlank('plank02',(length,width,height),tuple(colors[1]),z = -(height))
    removefrom = plank.users_collection
    coll.objects.link(plank)
    removefrom[0].objects.unlink(plank)
    setViewport()
    
    
    return coll  


def createPlanks(length,width,height,cut,name):
    
    bprint("Running createPlanks...")
#     length = 2.44
#     width = 1.22
#     height = 0.018
#     cut = 0.006
    
    coll = initBoundries(width,length,height)
  
    mainplank = [length, width]
    
    # Get a list of all cube objects in the scene
    cubes = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH' and obj.name.startswith(name)]
    
    #sort cubes by dimensions
    cubes_sorted = sorted(cubes, key=lambda cube: max(cube.dimensions), reverse=True)
    
    plank_dims = []
        
    for a, cube in enumerate(cubes_sorted):
        x, y, z = cube.dimensions
        dimensions = [round(dim, 3) for dim in [x, y, z]]
        dimensions_sorted = sorted(dimensions, reverse=True)
        
        #sort by biggest side
        largest, middle, smallest = dimensions_sorted
        
        b = a + 1
        print(f"Plank '{b}': {largest} m x {middle} m x {smallest} m")
        
        #planks to be cut
        plank_dims.append([largest,middle])
    
    
    #sort by y    
    plank_dims = sorted(plank_dims, key=lambda x: x[1],reverse=True)
    print(plank_dims)
    
    #create some random colors
    colors_without_alpha = np.random.rand(len(plank_dims), 3)
    colors = np.column_stack((colors_without_alpha, np.ones(colors_without_alpha.shape[0])))
    
    
    createOtherPlanks(mainplank,plank_dims,cut,colors,coll,depth = height)


    #To run this:
    #myModule = bpy.data.texts[0].as_module(); myModule.createPlanks();

    # example createPlanks...    
    #    length = 1.00
    #    width = 0.80        
    #    createPlank(
    #                "test03", 
    #                (length,width,0),
    #                (1,0,0,0), 
    #                z = 0, 
    #                makematerial = False,
    #                center = True
    #                )
    


class MySawHelper_Props(bpy.types.PropertyGroup):
    length: bpy.props.FloatProperty(name="length", default=2.44)
    width: bpy.props.FloatProperty(name="width", default=1.22)
    height: bpy.props.FloatProperty(name="height", default=0.018)
    cut: bpy.props.FloatProperty(name="cut", default=0.006)
    objname: bpy.props.StringProperty(name="objname", default="Cube")


class MySawHelper_custom_menu(bpy.types.Panel):
    bl_idname = "SCRIPTS_PT_mysawhelper"
    bl_label = "Saw helper"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Saw helper"
    
#     length = 2.44
#     width = 1.22
#     height = 0.018
#     cut = 0.006
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.my_props
        layout.prop(props, "length")
        layout.prop(props, "width")
        layout.prop(props, "height")
        layout.prop(props, "cut")
        layout.prop(props, "objname")
        layout.separator()
        layout.operator("object.mysawhelper_operator", text="Create Saw Example")

class MySawHelper_Operator(bpy.types.Operator):
    bl_idname = "object.mysawhelper_operator"
    bl_label = "MySawHelper"
    bl_description = "MySawHelper"

    def execute(self, context):
        bprint("Running MySawHelper...")
        props = context.scene.my_props
        bprint( str(props.length) + ' - ' +  str(props.width) + ' - ' + str(props.height) + ' - ' + str(props.cut) + ' - ' + str(props.objname) )
        try:
            createPlanks(props.length,props.width,props.height,props.cut,props.objname)
            show_popup_message("MySawHelper", "Finished")
        except Exception as e:
            bprint("Error:", e)
        return {'FINISHED'}


classes = [
    MySawHelper_Operator,
    MySawHelper_custom_menu,
    MySawHelper_Props
]




def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.my_props = bpy.props.PointerProperty(type=MySawHelper_Props)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
