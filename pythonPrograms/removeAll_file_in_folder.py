import os
import shutil

for root, dirs, files in os.walk('E:\\abc'):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))