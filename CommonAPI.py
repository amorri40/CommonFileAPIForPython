import hashlib
import os
import subprocess
import ntpath, json

def walk_directory(location_to_walk, function_to_run_on_each_file):
    for root, dirs, filenames in os.walk(location_to_walk):
        for f in filenames:
            function_to_run_on_each_file(os.path.join(root, f))

def get_contents_of_file(filename):
    file_contents = open(filename, 'r').read()
    return file_contents

def get_filename_of_path(path):
    return ntpath.basename(path)

def write_string_to_file(string, file_name):
    fo = open(file_name, "w+")
    fo.write(string)
    fo.close()

def get_command_output(command_to_run):
    result = subprocess.check_output(command_to_run, shell=True)
    return result

def get_hash(content):
    ochash = hashlib.sha256()
    ochash.update(content)
    return ochash.hexdigest();

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

def json_file_to_object(file_path):
    json_data=open(file_path).read()

    data = json.loads(json_data)
    return data
