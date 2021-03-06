import bpy
import sys
import math
# import csv
import json


argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  # --> ['example', 'args', '123']

class JLCWatch(object) :

	def __init__(self):
		
		# row = []
		# f = open(argv[1], 'rt')
		# try:
		# 	reader = csv.reader(f)
		# 	next(reader)
		# 	for row in reader:
		# 		print(row)
		# finally:
		# 	f.close()

		# print(row[0])
		parsed_json = ""

		with open(argv[1], 'rt', encoding='ISO-8859-15') as fp:
			parsed_json = json.load(fp)
			
		print(parsed_json['cam']['x'])

		obj_name = 'Camera'
		obj = bpy.data.objects[obj_name] # bpy.types.Camera
		bpy.data.objects[obj_name].select = True
		obj.location.x = 0
		# be carefull axis y and z are swapped 
		obj.location.y = -6 # float(row[3])
		obj.location.z = 0
		
		obj_name = 'Base'
		base = bpy.data.objects[obj_name]
		bpy.context.scene.objects.active = bpy.data.objects[obj_name]
		bpy.data.objects[obj_name].select = True
		bpy.data.objects[obj_name].rotation_mode = 'XYZ'
		base.location.x = parsed_json['cam']['x']
		# be carefull axis y and z are swapped 
		base.location.y = parsed_json['cam']['z'] # float(row[3])
		base.location.z = parsed_json['cam']['y']
		bpy.data.objects[obj_name].rotation_euler = (math.radians(float(parsed_json['cam']['eulerX'])),math.radians(float(parsed_json['cam']['eulerZ'])),math.radians(180-float(parsed_json['cam']['eulerY']))) #(0,(2.0 * math.pi / 12.0) * int(row[0]),0)

		obj_name = 'minutes'
		minute = bpy.data.objects[obj_name]
		bpy.context.scene.objects.active = bpy.data.objects[obj_name]
		bpy.data.objects[obj_name].select = True
		bpy.data.objects[obj_name].rotation_mode = 'XYZ'
		bpy.data.objects[obj_name].rotation_euler = (0,(2.0 * math.pi / 60.0) * int(parsed_json['minutes']),0)

		obj_name = 'hours'
		hour = bpy.data.objects[obj_name]
		bpy.context.scene.objects.active = bpy.data.objects[obj_name]
		bpy.data.objects[obj_name].select = True
		bpy.data.objects[obj_name].rotation_mode = 'XYZ'
		bpy.data.objects[obj_name].rotation_euler = (0,(2.0 * math.pi / 12.0) * int(parsed_json['hours']),0)

		scene = bpy.context.scene
		scene.camera.data.angle = math.radians(70.0)
		fp = scene.render.filepath
		scene.render.image_settings.file_format = 'PNG' 
		scene.render.filepath = argv[0]
		bpy.ops.render.render(write_still=True)
		# bpy.ops.export_scene.obj(filepath=argv[0]+".obj", filter_glob="*.obj;*.mtl")
		cbpy.ops.wm.save_as_mainfile(filepath=argv[0]+'.blend')
		scene.render.filepath = fp
		return

def main():
	Watch = JLCWatch()
	return

if __name__ == '__main__':
	main()