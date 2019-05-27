#!/usr/bin/env python


import os
import zipfile
import shutil

try:
 shutil.make_archive('E:\\abc\\x','zip','C:\\Users\\user\\Documents\\Scanned Documents\\images')

 zip_ref = zipfile.ZipFile('E:\\abc\\x.zip', 'r')
 zip_ref.extractall('E:\\abc\\x')
except  Exception:
    print("file not found exception")
finally:
    zip_ref.close()
    os.remove("E:\\abc\\x.zip")


