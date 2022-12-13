import re
import time
import json
from Modules.showLists import *


class AutoCourseGrabbing:
    def __init__(self, in_http):
        self.http = in_http
        self.data = {}
        self.time = 0
        self.fxid = 0
        self.numc = {}

    def config(self):
        urps_outs('zdqk')
        print("[刷新的间隔]：输入刷新间隔，表示每隔几秒检测一次，建议2~3秒，输入no或者exit返回主菜单")
        print()
        urps_outs(0)
        while 1:
            print()
            addles_tima = input("[请输入间隔]：")
            if len(addles_tima) >= 1:
                if 'exit' in addles_tima or 'n' in addles_tima:
                    return 1
                if bool(re.search('[a-z]', addles_tima)):
                    urps_outs('iner')
                    continue
                if int(addles_tima) > 0:
                    self.time = int(addles_tima)
                    break
            urps_outs('iner')
            return 0

    def begins(self):
        os.system('cls')
        os.system('color 9f')
        # urps_outs('zzqk')
        # urps_outs(1)
        if len(self.data) == 0:
            urps_outs('zdqk')
            print()
            print("[尚未添加课程]:请先添加课程，然后再重新开始抢课！！！")
            print()
            urps_outs('back')
            return -1
        addles_coun = 0
        addles_lass = time.time()
        addles_begi = time.time()
        addles_datr = 0
        addles_flag = 0
        while addles_flag == 0:
            # ------------------------------------------------------------------------
            if addles_coun % 5 == 0:
                os.system('cls')
                if addles_datr == 0:
                    addles_nets = '000-未知'
                elif addles_datr.status_code == 200:
                    addles_nets = '200-正常'
                else:
                    addles_nets = str(addles_datr.status_code) + '-错误'
                addles_allt = str((time.time() - addles_begi) // 3600) + "时" + str(
                    ((time.time() - addles_begi) % 3600) // 60) + "分" + str(
                    ((time.time() - addles_begi) % 60 // 1)) + "秒"
                addles_lxzq = str(int((time.time() - addles_lass) * 200))
                addles_lass = time.time()
                urps_outs('zzqk')
                print()
                print(" 当前次数：" + str(addles_coun),
                      " 网络状态：" + addles_nets,
                      " 总共耗时：" + addles_allt,
                      " 轮询速度：" + str(addles_lxzq) + "ms/次",
                      " 设定速度：" + str(self.time) + "s/次")
                print()
                print(" CTRL-C 停止抢课并返回上一层 CTRL-Z 强制停止当前脚本 CTRL-D 结束输入内容 ALT+F4 强制结束并关闭程序")
                print()
                urps_outs(1)
            # ------------------------------------------------------------------------
            addles_coun = addles_coun + 1
            time.sleep(self.time - 1)
            try:
                addles_datr = self.http.get(http_urls_zyxk)
            except requests.exceptions.ConnectionError:
                urps_outs('nete')
                continue
            try:
                for addles_name in self.data:
                    addles_post = {
                        "searchtj": addles_name,
                        "xq": 0,
                        "jc": 0,
                        "kclbdm": ""
                    }
                    addles_data = self.http.post(http_urls_kclb, addles_post)
                    addles_tabs = json.loads(addles_data.text)
                    addles_list = json.loads(addles_tabs['rwRxkZlList'])
                    addles_nums = 0
                    for addles_loop in addles_list:
                        addles_nums += 1
                        for addles_tttp in range(0, self.numc[addles_name]):
                            if 1 == 1 and self.data[addles_name]['dat1'][addles_tttp] == addles_loop['kcm']  \
                                      and self.data[addles_name]['dat2'][addles_tttp] == addles_loop['jasm'] \
                                      and self.data[addles_name]['dat4'][addles_tttp] == addles_loop['kxh']  \
                                      and self.data[addles_name]['dat3'][addles_tttp] == addles_loop['skjs']:
                                classShow(addles_loop, addles_nums)
                                # ----------------------------------------------------------------------------------
                                if int(addles_loop['bkskyl']) > 0:
                                    zxyk_name = ""
                                    for i in range(0, len(addles_loop['kcm'])):
                                        zxyk_name += str(int((hex(ord(addles_loop['kcm'][i])).zfill(4)), 16)) + ","
                                    zxyk_temp = addles_datr.text.find('id="tokenValue"')
                                    zxyk_toke = addles_datr.text[zxyk_temp + 23:zxyk_temp + 55]
                                    zxyk_post = {
                                        "dealType": 5,
                                        "kcIds":   addles_loop['kch']
                                                 + "@"
                                                 + addles_loop['kxh']
                                                 + "@"
                                                 + addles_loop['zxjxjhh'],
                                        "kcms": zxyk_name,
                                        "fajhh": self.fxid,
                                        "sj": "0_0",
                                        "searchtj": addles_name,
                                        "kclbdm": "",
                                        "inputCode": "",
                                        "tokenValue": zxyk_toke
                                    }
                                    try:
                                        addles_data = self.http.post(http_urls_post, zxyk_post)
                                    except requests.exceptions.ConnectionError:
                                        urps_outs('nete')
                                        continue
                                    if addles_data.text.find("ok") != -1:
                                        urps_outs('succ')
                                        self.data.pop(addles_name)
                                    else:
                                        urps_outs('fail')
                                        time.sleep(5)
                                        addles_flag = 0
                                        os.system('cls')
                                        break
                                    if len(self.data) <= 0:
                                        addles_flag = 1
                                        break
                                    print('[系统返回内容]:', addles_data.text)
                        if len(self.data) <= 0:
                            addles_flag = 1
                            break
                    if len(self.data) <= 0:
                        addles_flag = 1
                        break
                if len(self.data) <= 0:
                    addles_flag = 1
                    break
            except KeyboardInterrupt:
                os.system('cls')
                return -1
            except requests.exceptions.ConnectionError:
                urps_outs('nete')
                continue
        urps_outs('back')

    def addles(self):
        os.system('cls')
        os.system('color 5f')
        urps_outs("zdqk")
        print("                         *请输入关键词，注意区分大小写以及中英文符号，请勿留空*")
        print()
        urps_outs(0)
        while 1:
            print()
            addles_inpu = input("[输入关键词]：")
            if len(addles_inpu) >= 1:
                break
            urps_outs('iner')
        addles_data = {
            "searchtj": addles_inpu,
            "xq": 0,
            "jc": 0,
            "kclbdm": ""
        }
        try:
            addles_retu = self.http.get(http_urls_zyxk)
            if addles_retu.text.find("自由选课") != -1:
                print()
                print("[成功获取课表]：成功进入课表页面，正在读取教务处课表列表，请耐心等待")
                addles_retu = self.http.post(http_urls_kclb, addles_data)
            else:
                print()
                print("[无法进入页面]：当前非选课阶段，或者教务处网站挂了，或者你的网络不行")
                print()
                urps_outs("back")
                return -3
            os.system('cls')
        except requests.exceptions.ConnectionError:
            urps_outs('nete')
            urps_outs("back")
            return -2
        addles_tabs = json.loads(addles_retu.text)
        if type(addles_tabs['rwRxkZlList']) is str:
            addles_list = json.loads(addles_tabs['rwRxkZlList'])
        elif type(addles_tabs['rwRxkZlList']) is list:
            addles_list = addles_tabs['rwRxkZlList']
        else:
            urps_outs('nete')
            urps_outs("back")
            return -2
        addles_nums = 0
        for addles_loop in addles_list:
            if addles_nums % 40 == 0:
                if addles_nums != 0:
                    print()
                    urps_outs('next')
                    input()
                    os.system('cls')
                print()
                urps_outs(1)
                print()
            addles_nums += 1
            classShow(addles_loop, addles_nums)
        if addles_nums == 0:
            urps_outs(-1)
            return -1
        urps_outs(0)
        print()
        print("               *请输入左侧序号，可以输入多个编号，用单个空格隔开，输入no或exit返回*")
        print()
        urps_outs(0)
        addles_fatp = json.loads(addles_tabs['yxkclist'])
        self.fxid = addles_fatp[0]['programPlanNumber']
        addles_wait = []
        addles_flgs = 0
        addles_numc = 0
        while addles_flgs == 0:
            print()
            addles_choi = input("[请输入编号]：")
            if len(addles_choi) >= 1:
                if 'exit' in addles_choi or 'n' in addles_choi:
                    return 1
                addles_inpt = addles_choi.split()
                addles_flgs = 1
                for addles_xzid in addles_inpt:
                    try:
                        addles_nump = int(addles_xzid)
                        if addles_nump in range(1, addles_nums + 1):
                            addles_wait.append(addles_nump)
                            addles_numc = addles_numc + 1
                    except ValueError or IOError:
                        urps_outs('iner')
                        addles_flgs = 0
                        continue
            else:
                urps_outs('iner')
        addles_nums = 0

        print("")
        print("[选中的课程]：将监听下列课程课余量：")
        urps_outs(0)
        addles_tpdt = {
            'dat1': [],
            'dat2': [],
            'dat3': [],
            'dat4': [],
        }
        for addles_loop in addles_list:
            addles_nums += 1
            for addles_appd in addles_wait:
                if addles_nums == addles_appd:
                    classShow(addles_loop, addles_nums)
                    print()
                    addles_tpdt['dat1'].append(addles_loop['kcm'])
                    addles_tpdt['dat2'].append(addles_loop['jasm'])
                    addles_tpdt['dat3'].append(addles_loop['skjs'])
                    addles_tpdt['dat4'].append(addles_loop['kxh'])
        self.data[addles_inpu] = addles_tpdt
        self.numc[addles_inpu] = addles_numc
        urps_outs(0)
        print("成功将课程添加进列表")
        urps_outs('back')
        return 0

    def delles(self):
        pass

    def showall(self):
        pass


def urps_zdqk(zdqk_main):
    # 抢课菜单选择----------------------------------------
    os.system('cls')
    qkcd_data = AutoCourseGrabbing(zdqk_main)
    while 1:
        os.system('cls')
        urps_outs('zdqk')
        urps_outs('qkcd')
        qkcd_choi = input("[请输入选项]：")
        if len(qkcd_choi) >= 1:
            if 'exit' in qkcd_choi or 'n' in qkcd_choi:
                return 1
            try:
                qkcd_nump = int(qkcd_choi)
                if qkcd_nump == 5:
                    return 0
                elif qkcd_nump == 1:
                    qkcd_data.addles()
                elif qkcd_nump == 2:
                    qkcd_data.showall()
                elif qkcd_nump == 3:
                    qkcd_data.delles()
                elif qkcd_nump == 4:
                    qkcd_data.config()
                    qkcd_data.begins()
            except ValueError:
                urps_outs('iner')
                continue
        else:
            urps_outs('iner')
    # ----------------------------------------------------
    urps_outs('back')
