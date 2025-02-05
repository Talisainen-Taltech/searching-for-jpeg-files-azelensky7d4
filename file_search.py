import os
import binascii
from io import BytesIO
import requests
import zipfile
import shutil

# Delete dir and all its contents if exists
shutil.rmtree("./random_files", ignore_errors=True)
# Download zip file
ans = requests.get("https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip")
# Extract files from zip
zip = zipfile.ZipFile(BytesIO(ans.content))
zip.extractall(".")

# JPEG extension list 'ffd8ffe0'
ext = ['ffd8']
for file in os.listdir("./random_files/"):
    with open("./random_files/" + file, "rb") as f:
        hex_digest = binascii.hexlify(f.read())
        if str(hex_digest[0:4])[2:-1] in ext:
            os.rename(f"./random_files/{str(file)}", f"./random_files/jpeg{str(file[4:])}.jpeg")
        else:
            os.remove(f"./random_files/{str(file)}")
