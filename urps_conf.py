import os
import requests
http_main = requests.session()
http_week = ['一', '二', '三', '四', '五', '六', '日','  ']
http_clas = {"0000000159": "10_1","0000000160": "10_1","0000000161": "10_1",
             "0000000162": "10_1","0000000163": "10_1","0000000164": "10_1","0000000165": "10_1"}
http_exam = {"0000000166": "10_1","0000000167": "10_1","0000000168": "10_1",
             "0000000169": "10_1","0000000170": "10_1","0000000171": "10_1","0000000172": "10_1"}
http_urls_zyxk = "http://zhjw.scu.edu.cn/student/courseSelect/courseSelect/index"
http_urls_xkl1 = "http://zhjw.scu.edu.cn/student/courseSelect/courseSelectResult/index"
http_urls_xkl2 = "http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/callback"
http_urls_jdjs = "http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/coursePropertyScores/index#id_1"
http_urls_jddt = "http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/coursePropertyScores/callback"
http_urls_kclb = "http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/courseList"
http_urls_post = "http://zhjw.scu.edu.cn/student/courseSelect/selectCourse/checkInputCodeAndSubmit"
http_yjpj_post = "http://zhjw.scu.edu.cn/student/teachingEvaluation/evaluation/index"
http_yjpj_list = "http://zhjw.scu.edu.cn/student/teachingEvaluation/teachingEvaluation/search"
http_yjpj_requ = "http://zhjw.scu.edu.cn/student/teachingEvaluation/teachingEvaluation/evaluationPage"
http_yjpj_conf = "http://zhjw.scu.edu.cn/student/teachingEvaluation/teachingEvaluation/evaluation"
http_head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
http_yjpj =[
    "老师非常好，和蔼可亲，教学经验丰富，互动充分","老师有点严厉，但是上课认真，知识丰富讲解详细","教学经验丰富，复杂问题能用通俗易懂的语言讲解",
    "授课时生动形象，极具幽默感，很能调动课堂气氛","重点突出，合理使用各种教学形式，激发学生兴趣","认真负责，有很强敬业精神，和蔼可亲，幽默风趣",
    "课堂气氛十分活跃，讲课有特色，很受学生的欢迎","讲授详细，讲授认真，课堂教学，内容较易于接受","答疑很认真，对同学们提出的问题能够详尽的解答",
    "突出重点，内容详细，对深奥的现象解释通俗易懂","善于调动同学们的学习积极性，课堂气氛十分活跃","授课认真仔细，声音甜美，和蔼可亲，态度很认真",
    "讲课十分认真投入，内容纲举目分，条理性比较强","特别善于举例，让同学联系实际，学习起来很轻松","为人和蔼，课堂能与同学们互动，营造温馨的气氛",
    "讲课重点突出，授课条理清晰，认真负责严谨耐心","内容丰富，涉及内容十分广泛，课堂气氛非常好的","总是能把授课和社会实际结合起来，授课内容易懂",
    "课堂内容充实，简单明了，学生能够轻松掌握知识","老师教学认真，课堂效率高，授课内容十分的详细","能跟着老师思路，气氛活跃，整节课学下来有收获",
    "授课有条理，有重点，既热情又严格，是老师榜样","根据本课程知识结构的特点，重点突出，层次分明","善于用凝练的语言将复杂难于理解的过程公式清晰",
    "治学严谨要求严格，深入了解学习状况，循循善诱","课堂气氛较为活跃上课例题丰富不厌其烦细心讲解","认真工整，批改作业认真并注意讲解学生易犯错误",
    "语言生动条理清晰，举例恰当，对待学生严格要求","适当缓和课堂气氛，充分调动了学生学习的积极性","有很强的敬业精神和蔼可亲幽默风趣，讲课有特色"]
def urps_outs(urps_data=0):
    if urps_data==0:
        print("-----------------------------------------------------------------------------------------------------")
    elif urps_data==1:
        print("----------------------------------------------搜索结果-----------------------------------------------")
        print()
        print("#                课程名           校区 余量  位置   教室    周数    时间    教师")
        print("-----------------------------------------------------------------------------------------------------")
    elif urps_data==-1:
        print()
        print("**************************************列表为空，请检查输入内容**************************************")
        print()
        input("--------------------------------------------按回车键返回--------------------------------------------")
    elif urps_data=="zdqk":
        print("----------------------------------------------自动抢课-----------------------------------------------")
    elif urps_data=="yjpj":
        print()
        print()
        print("                                       ■■■■■■■■■■■")
        print("                                       ■                  ■")
        print("                                       ■     一键评教     ■")
        print("                                       ■                  ■")
        print("                                       ■■■■■■■■■■■")
        print()
        print("-----------------------------------------------------------------------------------------------------")
        print()
        print("                              一键评教将会给所有未评教的老师全部好评                                   ")
        print()
        print("                   如果你想亲自给某位老师评价，请先前往教务处网站完成操作后重开                         ")
        print()
        print("-----------------------------------------------------------------------------------------------------")
        print()
        print("********************输入YES回车确认开始评教，输入NO/EXIT或者其他内容退出并返回主菜单*****************")
        print()
    elif urps_data=="zzpj":
        print()
        print()
        print("                                       ■■■■■■■■■■■")
        print("                                       ■                  ■")
        print("                                       ■     正在评教     ■")
        print("                                       ■                  ■")
        print("                                       ■■■■■■■■■■■")
        print()
        print("-----------------------------------------------------------------------------------------------------")
        print()
    elif urps_data=='zzqk':
        print("----------------------------------------------正在抢课-----------------------------------------------")
    elif urps_data=="back":
        input("--------------------------------------------按回车键返回---------------------------------------------")
    elif urps_data=='succ':
        os.system('color 2f')
        print()
        print()
        print("                                       ■■■■■■■■■■■")
        print("                                       ■                  ■")
        print("                                       ■     抢课成功     ■")
        print("                                       ■                  ■")
        print("                                       ■■■■■■■■■■■")
        print("[指令发送OK]：仅表示成功提交，不保证抢到")
        print("[指令发送OK]：如果失败，可能是别人先提交")
        print()
    elif urps_data=='fail':
        os.system('color 4f')
        print()
        print()
        print("                                       ■■■■■■■■■■■")
        print("                                       ■                  ■")
        print("                                       ■     抢课失败     ■")
        print("                                       ■                  ■")
        print("                                       ■■■■■■■■■■■")
        print()
        print("----------------------------------------------5s后重试-----------------------------------------------")
    elif urps_data=='next':
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>按回车下一页>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    elif urps_data=='nete':
        print("[严重的错误]：网络连接中断，请确保网络稳定")
    elif urps_data=='iner':
        print("[输入不正确]：请重新输入")
    elif urps_data=='retr':
        input("--------------------------------------------按回车键重试---------------------------------------------")