#!/usr/local/bin/python3

from collections import defaultdict

import argparse
import os
import sys
import time
import shutil

parser = argparse.ArgumentParser(prog='Photocopier', usage='%(prog)s [options]')
parser.add_argument('--source', type=str, required=True)
parser.add_argument('--target', type=str, required=True)

args = parser.parse_args(sys.argv[1:len(sys.argv)])

generated_file_struct = defaultdict(list)

files_number = 0
for filename in os.listdir(args.source):
    full_path = args.source + "/" + filename
    new_dir_name = time.strftime("%d.%m.%Y", time.localtime(os.path.getmtime(full_path)))

    files_number = files_number + 1
    generated_file_struct[new_dir_name].append(filename)

files_counter = 0
for item in generated_file_struct:
    print("---{0}".format(item))
    new_dir_name = args.target + "/" + item
    try:
        os.stat(new_dir_name)
    except:
        os.mkdir(new_dir_name)

    for filename in generated_file_struct[item]:
        files_counter = files_counter + 1
        source = "{0}/{1}".format(args.source, filename)
        target = "{0}/".format(new_dir_name)

        print("[{0:.2f}%]".format(files_counter / (files_number / 100.0)))
        shutil.copy2(source, target)
