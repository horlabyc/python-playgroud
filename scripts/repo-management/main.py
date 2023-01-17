import os
from glob import glob

def isDirectory(dir):
  if "." in dir: return False
  else: return True

directories = filter(isDirectory, glob("*"))
for idx, dir in enumerate(directories):
  print(f'Processing => {dir}')
  os.system(f'cd {dir}; git checkout master; git pull')
  print(f'Done => {dir}')
  print("=======================")
print("Done with all repos...")