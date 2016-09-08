import bpy
import sys
import math
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  # --> ['example', 'args', '123']

class JLCWatch(object) :

	def __init__(self):

		obj_name = 'Camera'
		obj = bpy.data.objects[obj_name] # bpy.types.Camera
		bpy.data.objects[obj_name].select = True
		obj.location.x = int(argv[3])
		# be carefull axis y and z are swapped 
		obj.location.y = -10.0
		obj.location.z = 0.0

		obj_name = 'hours'
		hour = bpy.data.objects[obj_name]
		bpy.context.scene.objects.active = bpy.data.objects[obj_name]
		bpy.data.objects[obj_name].select = True
		bpy.data.objects[obj_name].rotation_mode = 'XYZ'
		bpy.data.objects[obj_name].rotation_euler = (0,(2.0 * math.pi / 12.0) * int(argv[1]),0)

		obj_name = 'minutes'
		minute = bpy.data.objects[obj_name]
		bpy.context.scene.objects.active = bpy.data.objects[obj_name]
		bpy.data.objects[obj_name].select = True
		bpy.data.objects[obj_name].rotation_mode = 'XYZ'
		bpy.data.objects[obj_name].rotation_euler = (0,(2.0 * math.pi / 60.0) * int(argv[2]),0)

		scene = bpy.context.scene
		scene.camera.data.angle = 60*(math.pi/180.0)
		fp = scene.render.filepath
		scene.render.image_settings.file_format = 'PNG' 
		scene.render.filepath = argv[0]
		bpy.ops.render.render(write_still=True)
		# bpy.ops.export_scene.obj(filepath=argv[0]+".obj", filter_glob="*.obj;*.mtl")
		#cbpy.ops.wm.save_as_mainfile(filepath=argv[0]+'.blend')
		scene.render.filepath = fp
		return

def main():
	Watch = JLCWatch()
	return

if __name__ == '__main__':

  main()