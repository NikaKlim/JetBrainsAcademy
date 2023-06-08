
import os
import sys


def check_args():
    args = sys.argv
    if len(args) == 1:
        print("Directory is not specified")
        sys.exit(0)
    return args[1]


def get_fileformat():
    print("Enter file format:")
    ff = input()
    print()
    return ff


def issortingorder_asc():
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    print()
    while True:
        print("Enter a sorting option:")
        sort_no = int(input())
        if sort_no == 1 or sort_no == 2:
            if sort_no == 1:
                return True
            else:
                return False
        else:
            print()
            print("Wrong option")
            print()


def files_size(arrange, fyl_format):
    files_dic = {}
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if fyl_format in file:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size in files_dic.keys():
                    files_ls = files_dic.get(file_size)
                    files_ls.append(file_path)
                    files_dic.update({file_size: files_ls})
                else:
                    files_dic.update({file_size: [file_path]})
    size_ls = list(files_dic.keys())
    size_ls.sort(reverse=arrange)
    for size in size_ls:
        print(size, " bytes")
        files = files_dic.get(size)
        for file in files:
            print(file)
    return files_dic


if __name__ == '__main__':
    root_dir = check_args()
    file_format = "."+get_fileformat()
    sort_order = issortingorder_asc()
    os.chdir(str(root_dir))
    size_dic = files_size(arrange=sort_order, fyl_format=file_format)
