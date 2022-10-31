import os

pipout=os.popen("ps aux|grep 'zzl'")
res_list=pipout.read()
res_list=res_list.split('\n')
for res in res_list:
    if res.find("pycharm")!=-1:
        to_kill=res.split()[1]
        print(to_kill)
        os.system(f'kill {to_kill}')