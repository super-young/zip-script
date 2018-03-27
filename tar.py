import fire
import os,subprocess
import time
def zip(path,note=False):
    path  = os.path.realpath(path)
    date = time.strftime("%Y-%m-%d")
    t = time.strftime("%H-%M-%S")
    targetDirName = path.split('/')[-1]

    tagNum = 0
    for entry in os.scandir(os.path.dirname(path)):
        if entry.name.startswith(targetDirName+"-"+date):
            tagWithExt = entry.name.split("-")[-1]
            tag = tagWithExt.split(".")[0]
            tagNum = int(tag[1:])
    tagNum +=1
    tag = "v"+str(tagNum)
    name = "{}-{}-{}.zip".format(path.split('/')[-1],date+"-"+t,tag)
  
    command = "zip -r "+name +" "+format(path.split('/')[-1])

    p = subprocess.run(command.split(" "),cwd=os.path.dirname(path))
if __name__ == '__main__':
    fire.Fire()