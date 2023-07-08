import os
import sys

def main():
    argv = sys.argv
    if len(sys.argv) != 4:
        print("Provide arguments: filepath, extension to remove, extension to compare to")
        print("Exiting")
        exit(1)
    folder = argv[1]
    extensionRem = argv[2].lower()
    extensionComp = argv[3].lower()
    print("Going through " + folder)
    print("Removing all files with extension '." + extensionRem + "' that have same name as files with extension '." + extensionComp + "'")
    files = get_files(folder)
    removing = get_delete(files, extensionRem, extensionComp)
    print("found {} files".format(len(removing)))
    print("removing: ", removing)
    print("okay? 'y' / 'n'")
    userInput = input()
    if userInput == "y":
        print("removing files")
        remove_files(removing, folder)
    else:
        print("not removing files, exiting")
        exit()


def get_files(folder):
    res = []
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            res.append(filename)
    return res

def get_delete(files, extension_remove, extension_compare):
    file_map = {}
    remove = []
    for file in files:
        splitext = os.path.splitext(os.path.basename(file))
        name = splitext[0].lower()
        extension = splitext[1].lower()[1:]
        if extension == extension_remove:
            if name in file_map:
                file_map.pop(name)
                remove.append(file)
            else:
                file_map[name] = extension

        elif extension == extension_compare:
            file_map[name] = extension

    return remove

def remove_files(filenames, base_path):
    for filename in filenames:
        path = os.path.join(base_path, filename)
        os.remove(path)

if __name__ == "__main__":
    main()
