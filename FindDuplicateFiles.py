import os, sys
import hashlib
from collections import defaultdict
from datetime import datetime

def file_hash(path, block_size=65536):
    hasher = hashlib.md5()
    try:
        with open(path, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                hasher.update(block)
    except Exception as e:
        return None
    return hasher.hexdigest()

def find_duplicates(parent_dir):
    files_by_name = defaultdict(list)
    files_by_hash = defaultdict(list)
    f1 = open('D:\\Eliz\\test\\DupFilesDiffContent.txt','w')
    f2 = open('D:\\Eliz\\test\\DupFilesSameContent.txt','w')
    
    print(f" find_duplicates in {parent_dir}")
    for root, _, files in os.walk(parent_dir):
        for name in files:
            filepath = os.path.join(root, name)
            print(f"Filepath: {filepath}")
            files_by_name[name].append(filepath)
            h = file_hash(filepath)
            if h:
                files_by_hash[h].append(filepath)

    print("Duplicate files (same content):", file=f2)
    for h, paths in files_by_hash.items():
        if len(paths) > 1:
            print(f"Hash: {h}", file=f2)
            for p in paths:
                print(f"  {p}", file=f2)
            print()

    print("Files with same name but different content:", file=f1)
    for name, paths in files_by_name.items():
        if len(paths) > 1:
            hashes = [file_hash(p) for p in paths]
            if len(set(hashes)) > 1:
                print(f"Filename: {name}", file=f1)
                for p in paths:
                    try:
                        mtime = os.path.getmtime(p)
                    except Exception:
                        mtime = "Unknown"
                    #print(f"  Filename: {name} {p} | Last Modified: {mtime} | Hash: {file_hash(p)}", file=f)
                    dt_object = datetime.fromtimestamp(mtime)

                    # Format the datetime object into the desired string format
                    formatted_date_time = dt_object.strftime("%d %m %Y %H %M %S")

                    #print(f"Original mtime timestamp: {mtime}", file=f)
                    #print(f"Formatted date and time: {formatted_date_time}", file=f)
                    print(f"  Filename: {p} | Last Modified: {formatted_date_time} | Hash: {file_hash(p)}", file=f1)
                    print()

if __name__ == "__main__":
    parent_dir = input("Enter parent directory: ")
    find_duplicates(parent_dir)