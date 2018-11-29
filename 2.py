import os
root_path = os.getcwd()
offset = len(root_path.split("\\"))
#print(root_path)
for root,dirs,files in os.walk(root_path):
	current_dir = root
	#print(root)
	path_list = current_dir.split("\\")
	indent_level = len(path_list) - offset
#	print("\t"*indent_level,"\\",path_list[-1])
	for f in files:
		file_path = root+"\\"+os.path.splitext(f)[0]
		print(file_path)