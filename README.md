# Biological Motion Files Generator and Viewer
-- generate and view biological motion txt files from mp4 video files  
Example (gif files below created manually) (**lag due to** large gif sizes, slightly different fps between the gif files, and slightly different starting times) (check sample outputs here: https://github.com/AnthonyAndroulakis/BiologicalMotion/tree/master/sampletests):     
<img src="https://github.com/AnthonyAndroulakis/BiologicalMotion/blob/master/sampletests/sample.gif" width="400" height="790">
<img src="https://github.com/AnthonyAndroulakis/BiologicalMotion/blob/master/sampletests/sampleoutputexample.gif" width="400" height="790">  
The gifs above and the data in https://github.com/AnthonyAndroulakis/BiologicalMotion/tree/master/sampletests are of myself. Do not use these examples for your own purposes (blogs, posts, etc.) without written permission from me.    
> Implements 3D human single-pose estimation. 
> credits go to the following repositories (scroll to the bottom for references):
> - https://github.com/facebookresearch/VideoPose3D
> - https://github.com/zh-plus/video-to-pose3D
> - https://github.com/MVIG-SJTU/AlphaPose  

> compiled/coded by Anthony Androulakis and Ryan Joseph

## Quickstart:
1) To Download this Code: either use the command   
`git clone https://github.com/AnthonyAndroulakis/BiologicalMotion.git`   
or press the "Clone or Download" button and click "Download ZIP" in the dropdown menu
2) To Check and Install Dependencies: `python3 checkdependencies.py` #if *All requirements met.* is **NOT** printed, then manually install the needed requirements (will be printed)
3) place a video with 1 person moving about in the outputs folder
4) To Generate Biological Motion txt Files: `python3 -c "import vid2txt; vid2txt.main('filename.mp4')"` where filename is your video file name
5) get generated biological motion txt file from the txtbiomotion folder
6) To View Biological Motion txt File:     
`python3 ViewBiologicalMotion/bmread.py txtbiomotion/filename.txt` where filename is your biological motion txt file

## Requirements:
On a Linux system, run the following command to check/install the below dependencies (installs everything automatically except CUDA, python3, pip3, and pytorch):      
`python3 checkdependencies.py`    
1. Environment
   - Linux system
   - Python > 3.6 distribution
2. Dependencies
   - ffmpeg
   - mediainfo
   - Python Modules:
      - [Pytorch (CUDA ≥ 9.2)](https://pytorch.org/)
      - [torchsample](https://github.com/MVIG-SJTU/AlphaPose/issues/71#issuecomment-398616495)
      - tqdm
      - torchvision
      - tkinter
      - pillow
      - scipy
      - pandas
      - h5py
      - visdom
      - nibabel
      - opencv-python
      - matplotlib
   - Alphapose
       - Download **duc_se.pth** from [Dropbox](https://www.dropbox.com/s/4khz6uub9x5sgdt/duc_se.pth),
         and place it in `./joints_detectors/Alphapose/models/sppe`
       - Download **yolov3-spp.weights** from [Dropbox](https://www.dropbox.com/s/slpy8xczqw6g29p/yolov3-spp.weights),
         and place it in `./joints_detectors/Alphapose/models/yolo`
      
Facebook's [pretrained_h36m_cpn.bin model](https://dl.fbaipublicfiles.com/video-pose-3d/pretrained_h36m_detectron_coco.bin) has already been placed in the `./checkpoint` folder.   

## How to generate Biological Motion txt files (~55 seconds converting time for a 20 second long video file):   
1) place your video in the outputs folder   
2) `python3 -c "import vid2txt; vid2txt.main('filename.mp4')"` where filename is your video file name   
3) the json output from videopose will be located in the jsonoutput folder (folder created automatically)  
4) the biological motion text file will be located in the txtbiomotion folder (folder created automatically) 

## How to view Biological Motion txt files:
`python3 ViewBiologicalMotion/bmread.py txtbiomotion/filename.txt`           
If you wish to change the viewing dimensions or fps, edit the bmread.py file in the ViewBiologicalMotion folder.

## Format of Biological Motion txt files (improved format: duration (ms) on 3rd line for accurate fps when viewing):
```
dotsPerFrame
numberOfFrames
duration
x (1st joint, 1st frame)
y (1st joint, 1st frame)
x (2nd joint, 1st frame)
y (2nd joint, 1st frame)
x (3rd joint, 1st frame)
y (3rd joint, 1st frame)
.
.
.
x (nth joint, 1st frame)
y (nth joint, 1st frame)
x (1st joint, 2nd frame)
y (1st joint, 2nd frame)
x (2nd joint, 2nd frame)
y (2nd joint, 2nd frame)
.
.
.
x (nth joint, nth frame)
y (nth joint, nth frame)
```

## Joint Numbers:
<img src="https://github.com/AnthonyAndroulakis/BiologicalMotion/blob/master/sampletests/numberedjoints.png" width="172" height="394">

## References to code implemented in this project:
@inproceedings{pavllo:videopose3d:2019,     
&nbsp;&nbsp;&nbsp;&nbsp;title={3D human pose estimation in video with temporal convolutions and semi-supervised training},     
&nbsp;&nbsp;&nbsp;&nbsp;author={Pavllo, Dario and Feichtenhofer, Christoph and Grangier, David and Auli, Michael},      
&nbsp;&nbsp;&nbsp;&nbsp;booktitle={Conference on Computer Vision and Pattern Recognition (CVPR)},      
&nbsp;&nbsp;&nbsp;&nbsp;year={2019}      
}     
    
https://<i></i>github.com/zh-plus/video-to-pose3D      
    
@inproceedings{fang2017rmpe,      
&nbsp;&nbsp;&nbsp;&nbsp;title={{RMPE}: Regional Multi-person Pose Estimation},      
&nbsp;&nbsp;&nbsp;&nbsp;author={Fang, Hao-Shu and Xie, Shuqin and Tai, Yu-Wing and Lu, Cewu},      
&nbsp;&nbsp;&nbsp;&nbsp;booktitle={ICCV},      
&nbsp;&nbsp;&nbsp;&nbsp;year={2017}      
}          
    
@inproceedings{xiu2018poseflow,      
&nbsp;&nbsp;&nbsp;&nbsp;title = {{Pose Flow}: Efficient Online Pose Tracking},      
&nbsp;&nbsp;&nbsp;&nbsp;author = {Xiu, Yuliang and Li, Jiefeng and Wang, Haoyu and Fang, Yinghong and Lu, Cewu},      
&nbsp;&nbsp;&nbsp;&nbsp;booktitle={BMVC},      
&nbsp;&nbsp;&nbsp;&nbsp;year = {2018}      
}          

## Links to licenses of code implemented in this project:
facebookresearch: VideoPose3D: https://github.com/facebookresearch/VideoPose3D/blob/master/LICENSE      
zh-plus: video-to-pose3D: https://github.com/zh-plus/video-to-pose3D/blob/master/LICENSE      
MVIG-SJTU: AlphaPose: https://github.com/MVIG-SJTU/AlphaPose/blob/master/LICENSE      

