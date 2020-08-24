import os
from urps_xkjg import *
from urps_zxyk import *
from urps_scor import *
from urps_conf import *
from urps_yjpj import *
def urps_menu():
    os.system('cls')
    os.system('color 3f')
    print()
    print("                                       ■■■■■■■■■■■")
    print("                                       ■                  ■")
    print("                                       ■   SCU教务处助手  ■")
    print("                                       ■                  ■")
    print("                                       ■      Ver1.0      ■")
    print("                                       ■■■■■■■■■■■")
    print("")
    print("----------------------------------------------登录成功-----------------------------------------------")
    print()
    print("                                          1.绩点计算              ")
    print()
    print("                                          2.一键评教              ")
    print()
    print("                                          3.自动抢课              ")
    print()
    print("                                          4.选课结果              ")
    print()
    print("                                          5.退出登录              ")
    print()
    urps_outs(0)
    print()
    user_inpu = input("[请输入选项]：")
    if len(user_inpu) == 1:
        user_chos = int(user_inpu)
        if user_chos in range(1, 6):
            if user_chos == 1:
                urps_jdjs()
            if user_chos == 2:
                urps_zdpj()
            if user_chos == 3:
                urps_zdqk(http_main)
            if user_chos == 4:
                urps_xkjg()
            if user_chos == 5:
                os.system('cls')
                print()
                print("                                       ■■■■■■■■■■■")
                print("                                       ■                  ■")
                print("                                       ■     退出成功     ■")
                print("                                       ■                  ■")
                print("                                       ■■■■■■■■■■■")
                print()
                input("--------------------------------------------按回车键登录---------------------------------------------")
                return 0
    return -1