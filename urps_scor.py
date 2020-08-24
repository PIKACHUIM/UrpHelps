import os
import json
from urps_conf import *
from urps_gets import *
def urps_jdjs():
    os.system('cls')
    print()
    print("                                       ■■■■■■■■■■■")
    print("                                       ■                  ■")
    print("                                       ■     成绩查询     ■")
    print("                                       ■                  ■")
    print("                                       ■■■■■■■■■■■")
    print("")
    urps_outs(0)
    print()
    print("                                           1.成绩查询            ")
    print()
    print("                                           2.绩点计算            ")
    print()
    print("                                           3.返回上级            ")
    print()
    urps_outs(0)
    print()
    while 1:
        jdjs_inpu = input("[请输入选项]：")
        if len(jdjs_inpu) >= 1:
            if int(jdjs_inpu) == 1:
                os.system('cls')
                jdjs_temp = http_main.get(http_urls_jdjs)
                jdjs_temp = http_main.get(http_urls_jddt)
                jdjs_tabs = json.loads(jdjs_temp.text)
                jdjs_data = []
                for jdjs_lotq in jdjs_tabs:
                    for jdjs_lotp in jdjs_lotq['cjList']:
                        jdjs_data.append(jdjs_lotp)
                jdsj_coun = 0
                for jdsj_loop in jdjs_data:
                    if jdsj_coun%40==0:
                        if jdsj_coun!=0:
                            print()
                            urps_outs('next')
                            input()
                            os.system('cls')
                        print()
                        print("----------------------------------------------课程成绩-----------------------------------------------")
                        print()
                        print("属性   成绩   绩点   年份     学期   学分    课程名")
                        urps_outs(0)
                    jdsj_coun = jdsj_coun + 1
                    print(jdsj_loop['courseAttributeName']," ",
                          jdsj_loop['courseScore']," ",
                          jdsj_loop['gradePointScore']," ",
                          jdsj_loop['academicYearCode']," ",
                          jdsj_loop['termName']," ",
                          jdsj_loop['credit']," ",
                          jdsj_loop['courseName'])
                break
            elif int(jdjs_inpu) == 2:
                os.system('cls')
                jdjs_alls = 0
                jdjs_allc = 0
                jdjs_bxjs = 0
                jdjs_bxjc = 0
                jdjs_xxjs = 0
                jdjs_xxjc = 0
                jdjs_bxjd = 0
                jdjs_xxjd = 0
                jdjs_allj = 0
                jdjs_temp = http_main.get(http_urls_jdjs)
                jdjs_temp = http_main.get(http_urls_jddt)
                jdjs_tabs = json.loads(jdjs_temp.text)
                jdjs_data = []
                for jdjs_lotq in jdjs_tabs:
                    for jdjs_lotp in jdjs_lotq['cjList']:
                        jdjs_data.append(jdjs_lotp)
                for jdsj_loop in jdjs_data:
                    jdjs_allc = jdjs_allc + int(jdsj_loop['credit'])
                    jdjs_alls = jdjs_alls + int(jdsj_loop['credit']) * int(jdsj_loop['courseScore'])
                    jdjs_allj = jdjs_allj + urps_chan(int(jdsj_loop['courseScore']))*int(jdsj_loop['credit'])
                    if jdsj_loop['courseAttributeName'] == '必修':
                        jdjs_bxjc = jdjs_bxjc + int(jdsj_loop['credit'])
                        jdjs_bxjs = jdjs_bxjs + int(jdsj_loop['credit']) * int(jdsj_loop['courseScore'])
                        jdjs_bxjd = jdjs_bxjd + urps_chan(int(jdsj_loop['courseScore']))*int(jdsj_loop['credit'])
                    else:
                        jdjs_xxjc = jdjs_xxjc + int(jdsj_loop['credit'])
                        jdjs_xxjs = jdjs_xxjs + int(jdsj_loop['credit']) * int(jdsj_loop['courseScore'])
                        jdjs_xxjd = jdjs_xxjd + urps_chan(int(jdsj_loop['courseScore']))*int(jdsj_loop['credit'])
                jdjs_allj = jdjs_allj/jdjs_allc
                jdjs_bxjd = jdjs_bxjd/jdjs_bxjc
                jdjs_xxjd = jdjs_xxjd/jdjs_xxjc
                print()
                print()
                print("***********************************************成绩计算**********************************************")
                print()
                print()
                print("-----------------------------------------------综合成绩----------------------------------------------")
                print()
                print("总分：%06d              学分：%03d              平均：%3.3f              绩点：%3.3f" % (
                    jdjs_alls,
                    jdjs_allc,
                    jdjs_alls / jdjs_allc,
                    jdjs_allj))
                print()
                urps_outs(0)
                print()
                print()
                print("----------------------------------------------必修成绩-----------------------------------------------")
                print()
                print("总分：%06d              学分：%03d              平均：%3.3f              绩点：%3.3f" % (
                    jdjs_bxjs,
                    jdjs_bxjc,
                    jdjs_bxjs / jdjs_bxjc,
                    jdjs_bxjd))
                print()
                urps_outs(0)
                print()
                print()
                print("----------------------------------------------选修成绩-----------------------------------------------")
                print()
                print("总分：%06d              学分：%03d              平均：%3.3f              绩点：%3.3f" % (
                    jdjs_xxjs,
                    jdjs_xxjc,
                    jdjs_xxjs / jdjs_xxjc,
                    jdjs_xxjd))
                print()
                urps_outs(0)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("计算绩点时，先计算单科然后加权平均，这与教务处网站上的有差别")
                print("计算依照Grade Point Average-4.0规则计算,不同国家学校有所不同")
                print("方法请参见https://en.wikipedia.org/wiki/Grading_in_education")
                print()
                break
            elif int(jdjs_inpu) == 3:
                return 0
            else:
                continue
        print("[输入不正确]：请重新输入")
    urps_outs('back')
    return 0