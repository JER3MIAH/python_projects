# copyfile() => This copies contents of a file
# copy() => This does what the above does + destination can be a directory
# copy2() => does what copy() does + it copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("C:\\users\\hp\\desktop\\trial.txt", "copy.txt")  # source, destination
shutil.copyfile("C:\\users\\hp\\desktop\\trial.txt", "C:\\users\\hp\\desktop\\copy.txt")  # including the destination

