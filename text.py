import os
root_path = os.getcwd()
offsize = len(root_path.split("\\"))
print(offsize)
for root,files,dir in os.walk(root_path):
	current_dir = root.split("\\")
	indent_level = len(current_dir) - offsize
	print(indent_level*"\t",root.split("\\")[-1])
	#print(root.split("\\")[-1])