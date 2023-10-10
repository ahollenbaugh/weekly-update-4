with open("lesson4_folderexample.txt") as file:
    paths = file.readlines() # spits out a list of paths

fixed_paths = {} 
# key = OLD path
# value = list that resembles something like this: ["FIXED"/"OK!", NEW path (if applicable)]

for path in paths:
    if path == "\n": # ignore newline chars in the list
        pass
    else:
        new_path = path.replace(" ", "") # bye bye spaces
        if(path == new_path):
            # Nothing changed, this path is ok!
            fixed_paths[path] = ["OK!"]
        else:
            # Note that the path was fixed, and be sure to include the new path in the list
            fixed_paths[path] = ["FIXED", new_path]

# Console output
i = 1
for key in fixed_paths:
    print()
    print(f"{i}. ", end="")
    if fixed_paths[key][0] == 'FIXED':
        print(f"{key.rstrip()} | {fixed_paths[key][0]}: {fixed_paths[key][1]}")
    else:
        print(f"{key.rstrip()} | {fixed_paths[key][0]}")
    print()
    i += 1