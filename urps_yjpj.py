import random
import time
import json
import os
from urps_conf import *
from urps_outp import *
def urps_zdpj():
    os.system('cls')
    urps_outs("yjpj")
    zdpj_flgs = 0
    while zdpj_flgs == 0:
        print()
        zdpj_choi = input("[请输入选择]：")
        if len(zdpj_choi) >= 1:
            if 'exit' in zdpj_choi \
            or 'EXIT' in zdpj_choi \
            or 'n' in zdpj_choi    \
            or 'N' in zdpj_choi:
                return 1
            elif 'Y' in zdpj_choi \
            or   'y' in zdpj_choi:
                zdpj_flgs = 1
                break
            else:
                urps_outs('iner')
        else:
            urps_outs('iner')
    os.system('cls')
    os.system('color af')
    zdpj_data = http_main.get(http_yjpj_post)
    zdpj_data = http_main.get(http_yjpj_list)
    zdpj_list = json.loads(zdpj_data.text)
    #print(zdpj_list)
    zdpj_temp = []
    for zdpj_kcsx in zdpj_list['data']:
        #print(zdpj_kcsx)
        if zdpj_kcsx["isEvaluated"] == "否":
            zdpj_temp.append({
                "evaluationContent": zdpj_kcsx["evaluationContent"],
                "evaluatedPeople":zdpj_kcsx["evaluatedPeople"],
                "evaluatedPeopleNumber":zdpj_kcsx["id"]["evaluatedPeople"],
                "questionnaireCode":zdpj_kcsx["id"]["questionnaireCoding"],
                "questionnaireName":zdpj_kcsx["questionnaire"]["questionnaireName"],
                "evaluationContentNumber":zdpj_kcsx["id"]["evaluationContentNumber"],
                "evaluationContentContent":""
            })
    #print(zdpj_temp)
    for zdpj_loop in zdpj_temp:
        os.system('cls')
        urps_outs("zzpj")
        zdpj_post = {
            "evaluationContent":zdpj_loop["evaluationContent"],
            "evaluatedPeople": zdpj_loop["evaluatedPeople"],
            "evaluatedPeopleNumber": zdpj_loop["evaluatedPeopleNumber"],
            "questionnaireCode": zdpj_loop["questionnaireCode"],
            "questionnaireName": zdpj_loop["questionnaireName"],
            "evaluationContentNumber": zdpj_loop["evaluationContentNumber"],
            "evaluationContentContent": zdpj_loop["evaluationContentContent"]}
        zdpj_data = http_main.post(http_yjpj_requ,zdpj_post)
        if zdpj_data.text.find("评教") != -1:
            print("")
            print("[获取到课程]：成功进入评教页面")
            time.sleep(3)
            if zdpj_data.text.find("name=\"tokenValue\"") != -1:
                print("[评价课程中]：" + zdpj_loop["evaluationContent"])
                time.sleep(3)
                zdpj_inst=zdpj_data.text.find("name=\"tokenValue\"")
                zdpj_hash=zdpj_data.text[zdpj_inst+48:zdpj_inst+80]
                #print(zdpj_hash)
                zdpj_post = {
                    "tokenValue": zdpj_hash,
                    "questionnaireCode": zdpj_loop["questionnaireCode"],
                    "evaluationContentNumber": zdpj_loop["evaluationContentNumber"],
                    "evaluatedPeopleNumber": zdpj_loop["evaluatedPeopleNumber"],
                    "count": "0",
                    "zgpj":http_yjpj[random.randint(0,29)]
                }
                if   zdpj_loop["questionnaireName"].find("课堂") != -1:
                    zdpj_post.update(http_clas)
                elif zdpj_loop["questionnaireName"].find("实验") != -1:
                    zdpj_post.update(http_exam)
                else:
                    print("[评价未完成]：没找到此课程类型的评价方案，请手动操作")
                    time.sleep(9)
                    continue
                print("[此课程评价]：A   A   A   A   A ")
                print("[此课程评价]："+zdpj_post["zgpj"])
                time.sleep(9)
                zdpj_data = http_main.post(http_yjpj_conf, zdpj_post)
                print("[正提交评教]：" + zdpj_data.text)
                time.sleep(1)
                if zdpj_data.status_code==200 :
                    print("[正提交评教]：成功提交评教")
                    time.sleep(4)
                #print(zdpj_post)
        else:
            print("")
            print("[未找到课程]：无法完成评教操作")
    print()
    print("                                          ****评教完成****                                           ")
    print()
    urps_outs('back')
    return 0