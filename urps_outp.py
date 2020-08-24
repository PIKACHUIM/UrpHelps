from urps_conf import *
def urps_oupt(zyxk_loop, zyxk_nums):
    print(str(zyxk_nums).rjust(2, ' '),           # 编号
          zyxk_loop['kcm'][0:15].rjust(15, ' '),  # 课名
          zyxk_loop['kkxqm'].ljust(2, ' '),       # 校区
          str(zyxk_loop['bkskyl']).rjust(3, ' '), # 余量
          zyxk_loop['jxlm'][0:4].ljust(4, ' '),   # 位置
          zyxk_loop['jasm'][0:4].rjust(4, ' '),   # 教室
          end="")
    # -----------------------检测教学楼-----------------------
    for zyxk_jslp in range(0, 4 - len(zyxk_loop['jasm'])):
        print(" ", end="")
    # -------------------------------------------------------
    print(" "+zyxk_loop['sjdd'][0]['zcsm'].rjust(6,'0')+" 周",end="")  # 周数
    try:
        zyxk_temp = int(zyxk_loop['sjdd'][0]['skxq'].rjust(1, ' '))    # 天数
    except:
        zyxk_temp = 8
    print(http_week[zyxk_temp-1]+" "+zyxk_loop['sjdd'][0]['skjc'].rjust(2, '0')+"-", end="")# 星期
    try:
        zyxk_temp = int(zyxk_loop['sjdd'][0]['skxq'].rjust(1,' '))+int(zyxk_loop['sjdd'][0]['cxjc'])-1
    except:
        zyxk_temp = 0
    print(str(zyxk_temp).rjust(2, '0') + "节",zyxk_loop['skjs'][0:9].ljust(10, ' '))  # 老师
