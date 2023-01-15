import os
import time

categories = {
  'Images': ['jpeg', 'jpg', 'png', 'svg'],
  'PDFs': ['pdf'],
  'Datasets': ['json'],
  'Documents': ['doc', 'docx', 'csv', 'xls', 'xlsx', 'json'],
  'Media': ['mp3', 'mp4', 'mov'],
  'Installables': ['dmg', 'pkg', 'tgz'],
  'Others': ['zip', 'src', 'webp', 'vsix'],
  'Applications': ['app']
}

download_directory = '/Users/sulaimanolaosebikan/Documents'

initial_files = os.listdir(download_directory)

def classify_file(filename):
  # Get file extension
  extension = filename.split('.')[-1]
  extension = extension.lower()
  # Clasify the file based on its extension

  for category, extensions in categories.items():
    if extension in extensions:
      src_path = os.path.join(download_directory, filename)
      dest_path = os.path.join(download_directory, category, filename)
      print(dest_path)
      os.rename(src_path, dest_path)
      print(f"Moved {filename} to {category}")

for category in ['Images', 'PDFs', 'Media', 'Datasets', 'Others', 'Documents', 'Applications']:
  os.makedirs(os.path.join(download_directory, category), exist_ok=True)

for file in initial_files:
  classify_file(file)

while True:
  time.sleep(5)
  current_files = os.listdir(download_directory)

  new_files = list(set(current_files) - set(initial_files))
  print(new_files)
  for file in new_files:
    classify_file(file)
