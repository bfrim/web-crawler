import os


def check_directory(dir_name):
	'''Checks if a directory exist and returns a Boolean value. True if it does, False if not.'''
	if os.path.isdir(dir_name):
		return True
	return False

def create_directory(dir_name):
	'''Creates a directory, returns True if it did, False if it did not'''
	if os.path.exists(dir_name):
		return False
	else:
		os.makedirs(dir_name)
		return True

def create_file(dir_name, file_name, contents,):
	'''Creates a file, accepts only a list as input in contents parameter, returns True if it worked, False if it did not'''
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

def create_file_dict(dir_name, file_name, contents,):
	'''Creates a file, accepts only a list as input in contents parameter, returns True if it worked, False if it did not'''
	if os.path.isdir(dir_name):
		for i in contents:
			file_path = os.path.join(dir_name, i+file_name)
			if not os.path.exists(file_path):			
				fileout = open(file_path, "w")
				fileout.write(str(contents[i])+"\n")
				fileout.close()
	else:
		return False

def create_file_dict_list(dir_name, file_name, contents,):
	'''Creates a file, accepts only a list as input in contents parameter, returns True if it worked, False if it did not'''
	if os.path.isdir(dir_name):
		for i in contents:
			file_path = os.path.join(dir_name, i+file_name)
			if not os.path.exists(file_path):			
				fileout = open(file_path, "w")
				for j in contents[i]:
					fileout.write(str(j)+"\n")
				fileout.close()
	else:
		return False

def append_file(dir_name, file_name, contents):
	'''Appends to existing file, accepts only a string value as input in contents parameter, returns True if it worked, False if it did not'''    
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
	'''Lists files in directory, returns a list of files in directory'''
	result = []
	if os.path.isdir(dir_name):
		files = os.listdir(dir_name)
		for file in files:
			result.append(file)
	return result

def check_file(dir_name, file_name):
	'''Checks if file exists'''
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.isfile(file_path):
			return True
	return False

def read_file(dir_name, file_name):
	'''Reads a file, returns a LIST of all lines in file'''
	result = []
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.isfile(file_path):
			filein = open(file_path, "r")
			for i in filein:
				result.append(i.strip())
			filein.close()
		else:
			return False
	return result


def delete_file(dir_name, file_name):
	'''Deletes file'''
	if os.path.isdir(dir_name):
		file_path = os.path.join(dir_name, file_name)
		if os.path.isfile(file_path):
			os.remove(file_path)
			return True
	return False

def delete_directory(dir_name):
	'''Deletes directory and all it's files'''
	if os.path.isdir(dir_name):
		files = os.listdir(dir_name)
		for file in files:
			os.remove(os.path.join(dir_name, file))
		os.rmdir(dir_name)
		return True
	else:
		return False

