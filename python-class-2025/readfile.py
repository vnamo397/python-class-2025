#mode r means read only
f = open("demo.txt", "r")

for line in f:
    print(line.strip())#strip() - Remove leading/trailing whitespace

#f.close()

with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

#mode "a" mans append (adding new content to the end of the file)
with open("demo.txt", "a") as f:
    f.write("\nThis is a new line added to the file.")

with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

#mode "w" means write (overwrite the file)
with open("demo.txt", "w") as f:
    f.write("This file has been overwritten.\n")
    f.write("All previous content is lost.\n")

import os

if os.path.exists("demo2.txt"):
    os.remove("demo2.txt")
    print("File deleted successfully.")
else:
    print("demo2.txt does not exist.")
