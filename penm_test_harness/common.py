import json
from constants import *
import os
import shutil


class CommonFunctions():
    def read_file(self, file_name):
        with open(file_name, 'r') as f_obj:
            data =  f_obj.read()
            if file_name.endswith("json"):
                return json.loads(data)
            return data

    def write_file(self, file_name, content, mode="w+"):
        try:
            print("Writing content into file {0} ...".format(file_name))
            with open(file_name, mode) as f_obj:
                if file_name.endswith(".json"):
                    f_obj.write(json.dumps(content, indent=4))
                else:
                    f_obj.write(content)
        except Exception as e:
            print("Failed to write data into file with error {0}..".format(e))

    def backup_file(self, source):
        dest = bkp_dir
        backup_file = os.path.join(dest, os.path.basename(source))
        if os.path.exists(source):
            self.copy_files(source, backup_file)

    def create_dir_path(self, f_path):
        path = os.path.dirname(f_path)
        if not os.path.exists(path):
            #os.system('mkdir -p {0}'.format(os.path.dirname(path)))
            os.makedirs(path)

    def copy_files(self, source, dest):
        try:
            #print("copying {0} to {1}...".format(source, dest))
            self.create_dir_path(dest)
            shutil.copy(source, dest)
            os.chmod(dest, 0o777)
        except Exception as e:
            print("Failed to copy files with error {0}..".format(e))

    def create_dirs(self, directories):
        try:
            print("Creating directories {0}...".format(directories))
            for dir_ in directories:
                dir_name = os.path.join(base_dir, dir_)
                if not os.path.isdir(dir_name):
                    os.makedirs(dir_name)
        except Exception as e:
            print("Failed to create backup dir {0} " \
                "with error {1}".format(dir_name, e))

    def create_release_note_files_and_update_checksum(self):
        try:
            rel_data = self.read_file(release_note)
        except Exception as e:
            print("Reading relasenote file {0} failed with error {1}".format(release_note, e))
        for data in rel_data["deliverables"]:
            directory = data["functionalDesignation"].split(" ")[0]
            if directory.startswith("RHEL"):
                file_name = os.path.join(base_dir, "RHEL", data["filename"])
                if not os.path.isfile(file_name):
                    self.write_file(file_name, "")
        self.update_checksum_of_release_note(rel_data, base_dir)

    def update_checksum_of_release_note(self, rel_data, base_dir):
        print("Upating checksum of releasenote file...")
        checksum_map = {}
        dirs = ["ENM", "LITP", "RHEL"]
        for dir_ in dirs:
            for file_ in os.listdir(os.path.join(base_dir, dir_)):
                if file_.endswith(".iso"):
                    data = os.popen("md5sum {0}".format(os.path.join(base_dir, dir_, file_)))
                    data = data.read().strip().split(" ")
                    checksum_map[os.path.basename(data[-1])] = data[0].strip()
        for count, data in enumerate(rel_data["deliverables"]):
            if checksum_map.get(data["filename"]):
                rel_data["deliverables"][count]["checksum"] = checksum_map[data["filename"]]
            if data["productNumber"] == "CXP9036738":
                rel_data["deliverables"][count]["rstate"] = "R1V01"
        self.write_file(release_note, rel_data)

    def print_line(self):
        print("-" * 100)

    def os_execute_command(self, cmd):
        os.system(cmd)