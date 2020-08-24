import os
import json
from urps_conf import *
def urps_xkjg():
    os.system('cls')
    os.system('color 2f')
    print()
    print("----------------------------------------------选课结果-----------------------------------------------")
    xkjg_data = http_main.get(http_urls_xkl1)
    xkjg_data = http_main.get(http_urls_xkl2)
    print("[获取状态码]：", xkjg_data.status_code, "(此处200为正常)")
    print("-----------------------------------------------------------------------------------------------------")
    print("属性 方式  教师名        周数        星期        时间         课程名")
    print("-----------------------------------------------------------------------------------------------------")
    print()
    xkjg_tabs = json.loads(xkjg_data.text)
    for xkjg_loop in xkjg_tabs['xkxx'][0]:
        xkjg_kslx = xkjg_tabs['xkxx'][0][xkjg_loop]['examTypeName']
        xkjg_lsmz = str(xkjg_tabs['xkxx'][0][xkjg_loop]['attendClassTeacher']).split(" ")
        if len(xkjg_kslx) <= 1:
            xkjg_kslx = "未知"
        print("%2.2s %2.2s %4.3s" % (
            xkjg_tabs['xkxx'][0][xkjg_loop]['coursePropertiesName'],
            xkjg_kslx,
            xkjg_lsmz[0]
        ), end=' ')
        if xkjg_lsmz[0].find("ty") != -1:
            print("\t", end="")
        print("\t%7.7s" % (xkjg_tabs['xkxx'][0][xkjg_loop]['timeAndPlaceList'][0]['weekDescription']), end="")
        print("\t%1.1s"%(xkjg_tabs['xkxx'][0][xkjg_loop]['timeAndPlaceList'][0]['classDay']), end="")
        print("\t%2.2s" % (xkjg_tabs['xkxx'][0][xkjg_loop]['timeAndPlaceList'][0]['classSessions'])+"-", end="")
        try:
            xkjg_temp = int(xkjg_tabs['xkxx'][0][xkjg_loop]['timeAndPlaceList'][0]['classSessions']) + int(xkjg_tabs['xkxx'][0][xkjg_loop]['timeAndPlaceList'][0]['continuingSession']) -1
        except:
            xkjg_temp = 0
        print("%2.2s" % (str(xkjg_temp)) + "节", end="")
        print("\t%-16.16s\t"
              % (
                  xkjg_tabs['xkxx'][0][xkjg_loop]['courseName'])
              )
    print()
    urps_outs('back')
