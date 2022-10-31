import os
import shutil
split_size=1024

train_split=rf'/data/hatim/zzl/1dota/{split_size}trainsplit/'
val_split=rf'/data/hatim/zzl/1dota/{split_size}valsplit/'

train_image_path=train_split+'images/'
train_label_path=train_split+'yolo_label/'
val_image_path=val_split+'images/'
val_label_path=val_split+'yolo_label/'

target_image_path=rf'/data/hatim/zzl/1dota/yolov5_target/images/'
target_label_path=rf'/data/hatim/zzl/1dota/yolov5_target/labels/'
print('deleting origin')
if os.path.exists(target_image_path):
    shutil.rmtree(target_image_path)
    shutil.rmtree(target_label_path)
os.mkdir(target_label_path)
os.mkdir(target_image_path)

os.mkdir(target_label_path+'train/')
os.mkdir(target_label_path+'val/')
os.mkdir(target_image_path+'train/')
os.mkdir(target_image_path+'val/')

print('copying train image')
for file in os.listdir(train_image_path):
    #print(file,train_image_path+file,target_image_path+'train/'+file)
    shutil.copy(train_image_path+file,target_image_path+'train/'+file)
print('copying train label')
for file in os.listdir(train_label_path):
    shutil.copy(train_label_path+file,target_label_path+'train/'+file)
print('copying val image')
for file in os.listdir(val_image_path):
    shutil.copy(val_image_path+file,target_image_path+'val/'+file)
print('copy val label')
for file in os.listdir(val_label_path):
    shutil.copy(val_label_path+file,target_label_path+'val/'+file)

