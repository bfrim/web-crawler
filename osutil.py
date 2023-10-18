import os


def check_directory(dir_name):
	if os.path.isdir(dir_name):
		return True
	return False

def create_directory(dir_name):
	if os.path.exists(dir_name):
		return False
	else:
		os.makedirs(dir_name)
		return True

def create_file(dir_name, file_name, contents):
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if not os.path.exists(file_path):			
			fileout = open(file_path, "w")
			for i in contents:
				fileout.write(str(i)+"\n")
			fileout.close()
			return True
		else:
			return False
	else:
		return False

def append_file(dir_name, file_name, contents):
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.exists(file_path):			
			fileout = open(file_path, "a")
			fileout.write(str(contents) + "\n")
			fileout.close()
			return True
		else:
			return False
	else:
		return False

def list_directory(dir_name):
	result = []
	if os.path.isdir(dir_name):
		files = os.listdir(dir_name)
		for file in files:
			result.append(file)
	return result

def check_file(dir_name, file_name):
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.isfile(file_path):
			return True
	return False

def read_file(dir_name, file_name):
	result = []
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.isfile(file_path):
			filein = open(file_path, "r")
			for i in filein:
				result.append(i.strip())
			filein.close()
	return result

def delete_file(dir_name, file_name):
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.isfile(file_path):
			os.remove(file_path)
			return True
	return False

def delete_directory(dir_name):
	if os.path.isdir(dir_name):
		files = os.listdir(dir_name)
		for file in files:
			os.remove(os.path.join(dir_name, file))
		os.rmdir(dir_name)
		return True
	else:
		return False

