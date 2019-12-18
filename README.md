# Biological Motion Files Generator and Viewer
generate and view biological motion txt files from mp4 video files  
Example (slight lag due to GitHub loading 1st gif separately from loading 2nd gif file):     
Input video file (converted to gif): <img src="https://github.com/AnthonyAndroulakis/BiologicalMotion/blob/master/sampletests/sample.gif" width="400" height="790">       
Output tkinker   (converted to gif):
<img src="https://github.com/AnthonyAndroulakis/BiologicalMotion/blob/master/sampletests/sampleoutputexample.gif" width="400" height="790">     
> Implements 3D human single-pose estimation. 
> credits go to the following repositories (scroll to the bottom for references):
> - https://github.com/facebookresearch/VideoPose3D
> - https://github.com/zh-plus/video-to-pose3D
> - https://github.com/MVIG-SJTU/AlphaPose  

> compiled/coded by Anthony Androulakis and Ryan Joseph

## Requirements:
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
      
The models have already been placed in their respective folders.   

## How to generate Biological Motion txt files (~1 minute for a 4 second long video file):   
1) place your video in the outputs folder   
2) `python3 -c "import vid2txt; vid2txt.main('filename.mp4')"` where filename is your video file name   
3) the json output from videopose will be located in the jsonoutput folder (folder created automatically)  
4) the biological motion text file will be located in the txtbiomotion folder (folder created automatically) 

## How to view Biological Motion txt files:
`python3 ViewBiologicalMotion/bmread.py txtbiomotion/filename.txt `         
If you wish to change the viewing dimensions or fps, edit the bmread.py file in the ViewBiologicalMotion folder.

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

