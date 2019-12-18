#vid2txt.py, convert a video of a human into a txt biomotion file using videopose3D AI and json file reading
#how to run: import vid2txt; vid2txt.main('test.mp4')
#test.mp4 must already be in the outputs folder
#only .mp4 video files accepted, using ffmpeg to convert .mov to .mp4 if necessary
#anthony androulakis, dec 16, 2019
import os
import json
import videopose

def getpredictions(videofile):
    videopose.makepredictions(videofile)
    videofilename = videofile[:-4]
    cmddel1 = 'rm outputs/alpha_pose_'+videofilename+'.mp4'
    cmddel2 = 'rm -f outputs/alpha_pose_'+videofilename+'/'+videofilename+'.npz'
    cmddel3 = 'rm -rf outputs/alpha_pose_'+videofilename+'/vis'
    cmddel4 = 'rm -f outputs/'+videofilename+'_3d_output.npy'
    cmdrename1 = 'mv outputs/alpha_pose_'+videofilename+'/alphapose-results.json jsonoutput/'+videofilename+'.json'
    cmddel5 = 'rm -rf outputs/alpha_pose_'+videofilename
    cmddel6 = 'rm -f outputs/test_3d_output.npy'
    #the order of deletion/renaming below matters
    os.system(cmddel1)
    os.system(cmddel2)
    os.system(cmddel3)
    os.system(cmddel4)
    os.system(cmdrename1)
    os.system(cmddel5)
    os.system(cmddel6)

def json2txt(videofile):
    videofilename = videofile[:-4]
    poseread=json.load(open('jsonoutput/'+videofilename+'.json'))
    #frameOne = [i for j, i in enumerate(poseread[0]['keypoints']) if (j+1)%3] #first frame, x,y
    numpoints = int(len([i for j, i in enumerate(poseread[0]['keypoints']) if (j+1)%3])/2)-4 #just looks at the first frame, -4 because I removed 4 points
    n = len(poseread)
    allframeslist=[]
    for k in range(n):
        data = [round(i) for j, i in enumerate(poseread[k]['keypoints']) if (j+1)%3]
        del data[2:10] #remove left eye,ear and right eye,ear
        allframeslist.extend(data)

    allframeslist = [z/(max(allframeslist)-min(allframeslist)) for z in allframeslist] #normalize data to make it between 0 and 1
    allframeslist = [round(700*q) for q in allframeslist] #put in range of 700, change this maybe idk, rounded instead of casted to int

    duration = os.popen('mediainfo --Inform="Video;%Duration%" outputs/'+videofile).read()
    allframeslist.insert(0, duration) #insert duration at beginning
    allframeslist.insert(0, n) #insert numberFrames before duration
    allframeslist.insert(0, numpoints) #insert dotNumber before numberFrames

    allframeslist = [str(e) for e in allframeslist]

    allframesstring = '\n'.join(allframeslist)

    open('txtbiomotion/'+videofilename+'.txt', "w").write(allframesstring)

def main(videofile):
    cmdmakefolder1 = 'mkdir -p txtbiomotion'
    cmdmakefolder2 = 'mkdir -p jsonoutput'
    os.system(cmdmakefolder1)
    os.system(cmdmakefolder2)
    getpredictions(videofile)
    json2txt(videofile)
    print("Your bio motion txt file for "+videofile+" has been generated.")
