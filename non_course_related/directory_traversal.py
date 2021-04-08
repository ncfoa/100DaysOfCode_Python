import os
import fnmatch
import re
import json
import uuid

# Walk a directory path and sub-directories looking for image files and output it to JSON format.


path = "starting directory"  # should be in format of '/Users/username/picture_directory' on a Mac.
includes = ["*.jpg", "*.JPG"]  # include only jpeg files to walk a directory path for a particular file put it here.
excludes = ["*.CR2", ".DS_Store", ".localized", "*.lr*", ".idea"]  # ignore files of these types.
# transform glob patterns to regular expressions
includes = r'|'.join([fnmatch.translate(x) for x in includes])
excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

dirPath_dict: dict = dict()

for root, d_names, f_names in os.walk(path):

    # exclude/include files
    f_names = [f for f in f_names if not re.match(excludes, f)]
    f_names = [f for f in f_names if re.match(includes, f)]
    f_list = []
    for f in f_names:
        if "jpg" in f.lower():
            id_ = uuid.uuid4()
            name = root.replace(path, '').rstrip("/")
            print(f)
            url = "/albums" + "/" + name + "/" + f
            f_list_dict = {
                "id": id_.hex,
                "name": f,
                "imgUrl": url}
            f_list.append(f_list_dict)
        else:
            pass
    directory = {
        # "id": id.hex,
        "path": root,
        "images": f_list}

    if root not in dirPath_dict:
        dirPath_dict.update({root: directory})


jsonDir_dict = json.dumps(dirPath_dict)  # convert json output to dictionary
print(jsonDir_dict)