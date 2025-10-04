import os
import filecmp

def compare_directories(dir1, dir2):
    # Compare the directories
    comparison = filecmp.dircmp(dir1, dir2)

    # Check if there are any differences
    if comparison.left_only or comparison.right_only or comparison.diff_files or comparison.funny_files:
        print("Directories are NOT the same.")
        if comparison.left_only:
            print("Only in", dir1, ":", comparison.left_only)
        if comparison.right_only:
            print("Only in", dir2, ":", comparison.right_only)
        if comparison.diff_files:
            print("Files differ:", comparison.diff_files)
        if comparison.funny_files:
            print("Problem comparing:", comparison.funny_files)
        return False
    else:
        # Recursively check subdirectories
        for subdir in comparison.common_dirs:
            subdir1 = os.path.join(dir1, subdir)
            subdir2 = os.path.join(dir2, subdir)
            if not compare_directories(subdir1, subdir2):
                return False
        print("Directories are the same.")
        return True


dir1 = input("Enter directory1: ")
dir2 = input("Enter directory2: ")
print (f"Comparing {dir1} and {dir2}")
compare_directories(dir1, dir2)
