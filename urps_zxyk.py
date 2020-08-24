import os
import re
import time
import json
from urps_conf import *
from urps_outp import *
def urps_zdqk(http_main):
    os.system('cls')
    os.system('color 5f')
    print()
    urps_outs("zdqk")
    print()
    print("                         *请输入关键词，注意区分大小写以及中英文符号，请勿留空*")
    print()
    urps_outs(0)
    while 1:
        zdqk_inpu = input("[输入关键词]：")
        if len(zdqk_inpu) >= 1:
            break
        urps_outs('iner')
    print()
    post_data = {
        "searchtj": zdqk_inpu,
        "xq": 0,
        "jc": 0,
        "kclbdm": ""
    }
    try:
        zyxk_data = http_main.get(http_urls_zyxk)
        if zyxk_data.text.find("自由选课") != -1:
            print("")
            print("[获取到课表]：成功进入课表页面")
        zyxk_data = http_main.post(http_urls_kclb, post_data)
        os.system('cls')
    except:
        urps_outs('nete')
        urps_outs("back")
        return -2
    else:
        pass
    zyxk_tabs = json.loads(zyxk_data.text)
    zyxk_list = json.loads(zyxk_tabs['rwRxkZlList'])
    zyxk_nums = 0
    for zyxk_loop in zyxk_list:
        if zyxk_nums%40==0:
            if zyxk_nums!=0:
                print()
                urps_outs('next')
                input()
                os.system('cls')
            print()
            urps_outs(1)
            print()
        zyxk_nums += 1
        urps_oupt(zyxk_loop,zyxk_nums)

    if zyxk_nums == 0:
        urps_outs(-1)
        return -1
    urps_outs(0)
    print()
    zyxk_fatp = json.loads(zyxk_tabs['yxkclist'])
    zyxk_fxid = zyxk_fatp[0]['programPlanNumber']
    print("               *请输入左侧序号，可以输入多个编号，用单个空格隔开，输入no或exit返回*")
    print()
    urps_outs(0)
    zyxk_wait=[]
    zyxk_flgs=0
    zyxk_numc=0
    while zyxk_flgs==0:
        print()
        zyxk_choi = input("[请输入编号]：")
        if len(zyxk_choi) >= 1:
            if 'exit' in zyxk_choi or 'n' in zyxk_choi:
                return 1
            zyxk_inpt=zyxk_choi.split()
            zyxk_flgs = 1
            for zyxk_xzid in zyxk_inpt:
                try:
                    zyxk_nump = int(zyxk_xzid)
                    if zyxk_nump in range(1, zyxk_nums + 1):
                        zyxk_wait.append(zyxk_nump)
                        zyxk_numc=zyxk_numc+1
                except:
                    urps_outs('iner')
                    zyxk_flgs = 0
                    continue
        else:
            urps_outs('iner')
    zyxk_dat1 = []
    zyxk_dat2 = []
    zyxk_dat3 = []
    zyxk_dat4 = []
    zyxk_nums = 0
    print("")
    print("[选中的课程]：将监听下列课程课余量：")
    urps_outs(0)
    for zyxk_loop in zyxk_list:
        zyxk_nums += 1
        for zyxk_appd in zyxk_wait:
            if zyxk_nums == zyxk_appd:
                urps_oupt(zyxk_loop, zyxk_nums)
                print()
                zyxk_dat1.append(zyxk_loop['kcm'])
                zyxk_dat2.append(zyxk_loop['jasm'])
                zyxk_dat3.append(zyxk_loop['skjs'])
                zyxk_dat4.append(zyxk_loop['kxh'])
    urps_outs(0)
    print("")
    print("[刷新的间隔]：输入刷新间隔，表示每隔几秒检测一次，建议2~3秒，输入no或者exit返回主菜单")
    print()
    while 1:
        zyxk_tima = input("[请输入间隔]：")
        if len(zyxk_tima) >= 1:
            if 'exit' in zyxk_tima or 'n' in zyxk_tima:
                return 1
            if bool(re.search('[a-z]', zyxk_tima)):
                urps_outs('iner')
                continue
            if int(zyxk_tima) > 0:
                zyxk_time = int(zyxk_tima)
                break
        urps_outs('iner')
    os.system('cls')
    os.system('color 8f')
    zyxk_flag = 0
    urps_outs('zzqk')
    print()
    print()
    print()
    urps_outs(1)
    zyxk_coun = 0
    global zyxk_lass
    zyxk_lass = time.time()
    zyxk_begi = time.time()
    while zyxk_flag == 0:
        zyxk_coun = zyxk_coun+1
        os.system('color 8f')
        time.sleep(zyxk_time - 1)
        try:
            zyxk_datr = http_main.get(http_urls_zyxk)
        except:
            urps_outs('nete')
            continue
        try:
            zyxk_data = http_main.post(http_urls_kclb, post_data)
        except:
            urps_outs('nete')
            continue
        if zyxk_coun%5==0:
            os.system('cls')
            if zyxk_datr.status_code==200:
                zyxk_nets = '200-正常'
            else:
                zyxk_nets = str(zyxk_datr.status_code)+'-错误'
            zyxk_allt = str((time.time()-zyxk_begi)//3600)+"时"+str(((time.time()-zyxk_begi)%3600)//60)+"分"+str(((time.time()-zyxk_begi)%60//1))+"秒"
            zyxk_lxzq = str(int((time.time()-zyxk_lass)*200))
            zyxk_lass = time.time()
            urps_outs('zzqk')
            print()
            print(" 当前次数："+str(zyxk_coun),
                  " 网络状态："+zyxk_nets,
                  " 总共耗时："+zyxk_allt,
                   "轮询速度："+str(zyxk_lxzq)+"ms/次",
                  " 设定速度："+str(zyxk_time)+"s/次")
            print()
            urps_outs(1)
        zyxk_tabs = json.loads(zyxk_data.text)
        zyxk_list = json.loads(zyxk_tabs['rwRxkZlList'])
        zyxk_nums = 0
        for zyxk_loop in zyxk_list:
            zyxk_nums += 1
            for zyxk_tttp in range(0,zyxk_numc):
                if zyxk_dat1[zyxk_tttp] == zyxk_loop['kcm'] \
                        and zyxk_dat2[zyxk_tttp] == zyxk_loop['jasm'] \
                        and zyxk_dat4[zyxk_tttp] == zyxk_loop['kxh']  \
                        and zyxk_dat3[zyxk_tttp] == zyxk_loop['skjs']:
                    urps_oupt(zyxk_loop, zyxk_nums)
                    if int(zyxk_loop['bkskyl']) > 0:
                        zxyk_name = ""
                        for i in range(0, len(zyxk_loop['kcm'])):
                            zxyk_name += str(int((hex(ord(zyxk_loop['kcm'][i])).zfill(4)), 16)) + ","
                        zxyk_temp = zyxk_datr.text.find('id="tokenValue"')
                        zxyk_toke = zyxk_datr.text[zxyk_temp + 23:zxyk_temp + 55]
                        zxyk_post = {
                            "dealType": 5,
                            "kcIds": zyxk_loop['kch'] + "@" + zyxk_loop['kxh'] + "@" + zyxk_loop['zxjxjhh'],
                            "kcms": zxyk_name,
                            "fajhh": zyxk_fxid,
                            "sj": "0_0",
                            "searchtj": zdqk_inpu,
                            "kclbdm": "",
                            "inputCode": "",
                            "tokenValue": zxyk_toke
                        }
                        zyxk_data = http_main.post(http_urls_post, zxyk_post)
                        os.system('cls')
                        if zyxk_data.text.find("ok") != -1:
                            urps_outs('succ')
                        else:
                            urps_outs('fail')
                            time.sleep(5)
                            zyxk_flag = 0
                            os.system('cls')
                            break
                        print(zyxk_data.text)
                        zyxk_flag = 1
                        break
    urps_outs('back')
