import commands
import os


class FileUtil():

    @staticmethod
    def save_remove_first_line(file_abs_path, new_file_abs_path):
        header = ""
        out_file = open(new_file_abs_path, "w")
        with open(file_abs_path, "r") as input:
            input_data = input.readlines()
            index = 0
            for line in input_data:
                if index != 0:
                    out_file.write(line)
                else:
                    header = line
                index += 1
        out_file.close()
        return header

    @staticmethod
    def add_header_to_file(header_line, file_abs_path):
        with open(file_abs_path, 'r+') as fh:
            lines = fh.readlines()
            lines.insert(0,header_line)
            fh.seek(0)
            fh.writelines(lines)

    @staticmethod
    def coscmd_upload(file_abs_path):
        filename = (os.path.basename(file_abs_path))
        # cmd = "coscmd -b heai-seed-rec-service-dev-1256590953 upload " + file_abs_path + " seedrec/" + filename
        cmd = "cp awesome.db /tmp/featuredb"  # this will persist on Node disk
        status, output = commands.getstatusoutput(cmd)
        print(str(status) + " " + str(output))