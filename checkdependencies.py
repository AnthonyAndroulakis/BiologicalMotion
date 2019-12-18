#this file can be run with any python3 version
import os

os.system('mkdir -p outputs') #create outputs folder if it does not already exist
missingRequirements = []
#check CUDA existence and version
if os.path.isfile('/usr/local/cuda/version.txt') == False:
    print('CUDA is missing. Please install CUDA (version ≥ 9.2)')
    missingRequirements.append('CUDA')
elif float('.'.join(os.popen('cat /usr/local/cuda/version.txt').read()[:-1].split(' ')[2].split('.')[:2]))>=9.2 == False:
    print('CUDA version is too low. Please install CUDA (version ≥ 9.2)')
    missingRequirements.append('cudaVersionTooLow')
#check python3 existence and version
if 'not found' not in os.popen('type python3').read()[:-1]: #if python3 exists
    if int(''.join(os.popen('python3 --version').read()[:-1].split(' ')[1].split('.')[:2]))<=36: #if python3 version < = 3.6
        print("python3 version is less than or equal to 3.6. Due to multiple methods of installation existing for different computers, you must install python3 version≥3.6 yourself.")
        missingRequirements.append('pyVersionTooLow')
    if 'not found' in os.popen('type pip3').read()[:-1]: #if pip3 does not exist
        print("pip3 is missing. Due to multiple methods of installation existing for different computers, you must do this yourself.")
        missingRequirements.append('pip3')
    if int(''.join(os.popen('python3 --version').read()[:-1].split(' ')[1].split('.')[:2]))>36: #if python3 version > 3.6:
        #check python module existence
        #pytorch
        try:
            import torch
        except ModuleNotFoundError:
            print('pytorch module not found. Please install your cuda-specific version from here: https://pytorch.org/')
            missingRequirements.append('moduleTorch')
        #torchsample
        os.system('pip3 install -e git+https://github.com/ncullen93/torchsample.git#egg=torchsample')
        #tqdm
        try:
            import tqdm
        except ModuleNotFoundError:
            print('tqdm module not found. Installing now...')
            os.system('pip3 install tqdm')
        #torchvision
        try:
            import torchvision
        except ModuleNotFoundError:
            print('torchvision module not found. Installing now...')
            os.system('pip3 install torchvision')
        #tkinter
        try:
            import tkinter
        except ModuleNotFoundError:
            print('tkinter module not found. Installing now...')
            os.system('pip3 install tkinter')
        #pillow
        try:
            import PIL
        except ModuleNotFoundError:
            print('pillow module not found. Installing now...')
            os.system('pip3 install pillow')
        #scipy
        try:
            import scipy
        except ModuleNotFoundError:
            print('scipy module not found. Installing now...')
            os.system('pip3 install scipy')
        #pandas
        try:
            import pandas
        except ModuleNotFoundError:
            print('pandas module not found. Installing now...')
            os.system('pip3 install pandas')
        #h5py
        try:
            import h5py
        except ModuleNotFoundError:
            print('h5py module not found. Installing now...')
            os.system('pip3 install h5py')
        #visdom
        try:
            import visdom
        except ModuleNotFoundError:
            print('visdom module not found. Installing now...')
            os.system('pip3 install visdom')
        #nibabel
        try:
            import nibabel
        except ModuleNotFoundError:
            print('nibabel module not found. Installing now...')
            os.system('pip3 install nibabel')
        #opencv-python
        try:
            import cv2
        except ModuleNotFoundError:
            print('opencv-python module not found. Installing now...')
            os.system('pip3 install opencv-python')
        #matplotlib
        try:
            import matplotlib
        except ModuleNotFoundError:
            print('matplotlib module not found. Installing now...')
            os.system('pip3 install matplotlib')      
else:
    print("python3 is missing. Due to multiple methods of installation existing for different computers, you must do this yourself.")

#check package existence
if 'not found' in os.popen('type ffmpeg').read()[:-1]:
    installFfmpeg = input('ffmpeg is needed for this program but is not found on your computer, install it? (y/n) ').lower()
        if installFfmpeg == 'y':
            os.system('sudo apt-get install ffmpeg')
        else:
            ('ffmpeg is missing and needs to be installed')
            missingRequirements.append('ffmpeg')

if 'not found' in os.popen('type mediainfo').read()[:-1]:
    installMediainfo = input('mediainfo is needed for this program but is not found on your computer, install it? (y/n) ').lower()
        if installMediainfo == 'y':
            os.system('sudo apt install mediainfo')
        else:
            ('mediainfo is missing and needs to be installed')
            missingRequirements.append('mediainfo')

#get neural network models:
if os.path.isfile('./joints_detectors/Alphapose/models/sppe/duc_se.pth') == False:
    print('Alphapose duc_se.pth file not found, downloading now...')
    os.system('wget -O ./joints_detectors/Alphapose/models/sppe/duc_se.pth https://www.dropbox.com/s/4khz6uub9x5sgdt/duc_se.pth')
if os.path.isfile('./joints_detectors/Alphapose/models/yolo/yolov3-spp.weights') == False:
    print('Alphapose yolov3-spp.weights file not found, downloading now...')
    os.system('wget -O ./joints_detectors/Alphapose/models/yolo/yolov3-spp.weights https://www.dropbox.com/s/slpy8xczqw6g29p/yolov3-spp.weights')

#print missing requirements
if len(missingRequirements)>0:
    print("Please install the following missing requirements: "+", ".join(missingRequirements))
else:
    print("All requirements met.")
