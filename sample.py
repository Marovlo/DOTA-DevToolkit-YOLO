import os
import random

split_size=300
sample_rate=60 #sample rate x means after sample x/100 data will remain
trainpath=rf'/data/hatim/zzl/1dota/{split_size}trainsplit'
valpath=rf'/data/hatim/zzl/1dota/{split_size}valsplit'
train_png_path=trainpath+'/images'
train_label_path=trainpath+'/labelTxt'
val_png_path=valpath+'/images'
val_label_path=valpath+'/labelTxt'

for png_name in os.listdir(train_png_path):
    is_delete=random.randint(0,100)
    if is_delete>sample_rate:
        file_name=png_name.split('.')[0]
        to_delete_png=train_png_path+'/'+file_name+'.png'
        to_delete_label=train_label_path+'/'+file_name+'.txt'
        os.remove(to_delete_png)
        os.remove(to_delete_label)

for png_name in os.listdir(val_png_path):
    is_delete=random.randint(0,100)
    if is_delete>sample_rate:
        file_name=png_name.split('.')[0]
        to_delete_png=val_png_path+'/'+file_name+'.png'
        to_delete_label=val_label_path+'/'+file_name+'.txt'
        os.remove(to_delete_png)
        os.remove(to_delete_label)

