import os

pipout=os.popen("ps aux|grep 'train_zzl_yolov5'")
res_list=pipout.read()
res_list=res_list.split('\n')
for res in res_list:
    if len(res.split())>2:
        to_kill=res.split()[1]
        print(to_kill)
        os.system(f'kill {to_kill}')