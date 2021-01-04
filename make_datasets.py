import os
import shutil
from pathlib import Path


os.makedirs('d:\\dataset\\train\\flawed')
os.makedirs('d:\\dataset\\train\\flawless')
os.makedirs('d:\\dataset\\test\\flawed')
os.makedirs('d:\\dataset\\test\\flawless')

def find_label_txt(path, result):
    if list(path.glot('*.txt')):
        result.extend(list(path.glot('*.txt')))
        return
