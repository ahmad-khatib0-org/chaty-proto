import os

root_dir = "gen/python"

for dirpath, dirnames, filenames in os.walk(root_dir):
  init_path = os.path.join(dirpath, "__init__.py")
  if not os.path.exists(init_path):
    open(init_path, "a").close()
