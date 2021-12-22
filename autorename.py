import os

path = 'C:/Users/aliif/OneDrive - anngg/Documents/KULIAH-UGM/semester-1/praktikum pemrograman/kodingan-semua/ngoding-all'

files = os.listdir(path)

awal = 0

for index, file in enumerate(files):
    awal = awal + 1
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(awal), '.py'])))