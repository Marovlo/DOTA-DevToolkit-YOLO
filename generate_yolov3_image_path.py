import os
import shutil
image_size=300

trainsplit_path=rf'/data/hatim/zzl/1dota/{str(image_size)}trainsplit/'
valsplit_path=rf'/data/hatim/zzl/1dota/{str(image_size)}valsplit/'

target_image_path=r'/data/hatim/zzl/PyTorch-YOLOv3-master/data/custom/images/'
target_label_path=r'/data/hatim/zzl/PyTorch-YOLOv3-master/data/custom/labels/'
shutil.rmtree(target_image_path)
shutil.rmtree(target_label_path)
os.mkdir(target_image_path)
os.mkdir(target_label_path)

with open(f'/data/hatim/zzl/PyTorch-YOLOv3-master/data/custom/train.txt','w')as f:
    trainsplit_image_path=trainsplit_path+'images/'
    count = 0
    total= len(os.listdir(trainsplit_image_path))
    for file in os.listdir(trainsplit_image_path):
        if count%100==0:
            print('train images copying',count,total)
        count+=1
        shutil.copy(trainsplit_image_path+file,target_image_path+file)
        f.write(target_image_path+file+'\n')
    trainsplit_label_path = trainsplit_path+'yolo_label/'
    count=0
    for file in os.listdir(trainsplit_label_path):
        if count % 100==0:
            print('train label copying',count,total)
        count+=1
        shutil.copy(trainsplit_label_path+file,target_label_path+file)

with open(f'/data/hatim/zzl/PyTorch-YOLOv3-master/data/custom/valid.txt','w')as f:
    valsplit_image_path=valsplit_path+'images/'
    total = len(os.listdir(valsplit_image_path))
    count = 0
    for file in os.listdir(valsplit_image_path):
        if count % 100==0:
            print('val image copying',count,total)
        count+=1
        shutil.copy(valsplit_image_path+file,target_image_path+file)
        f.write(target_image_path+file+'\n')
    valsplit_label_path=valsplit_path+'yolo_label/'
    count=0
    for file in os.listdir(valsplit_label_path):
        if count % 100==0:
            print('val label copying',count,total)
        count+=1
        shutil.copy(valsplit_label_path+file,target_label_path+file)
