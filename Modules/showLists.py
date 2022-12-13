from Modules.staticINF import *


def classShow(classData, classNums):
    # 课程序号 ---------------------------------
    try:
        classUUID = str(classData['kch'])
    except (ValueError, TypeError, Exception):
        classUUID = "?????????"
    # 课程名称 ---------------------------------
    try:
        className = str(classData['kcm'])[0:15]
    except (ValueError, TypeError, Exception):
        className = "未知课程名称, 数据错误!!!"
    # 上课校区 ---------------------------------
    try:
        classArea = str(classData['kkxqm'])
    except (ValueError, TypeError, Exception):
        classArea = "未知"
    # 课程余量 ---------------------------------
    try:
        classFree = str(classData['bkskyl'])
    except (ValueError, TypeError, Exception):
        classFree = "??"
    # 课程楼层 ---------------------------------
    try:
        roomBuild = str(classData['jxlm'])[0:4]
    except (ValueError, TypeError, Exception):
        roomBuild = "????"
    # 课程教室 ---------------------------------
    try:
        classRoom = str(classData['jasm'])[0:4]
    except (ValueError, TypeError, Exception):
        classRoom = "未知地点"
    # 课程周数 ---------------------------------
    try:
        classWeek = str(classData['zcsm'])
    except (ValueError, TypeError, Exception):
        classWeek = "????"
    # 课程天数 ---------------------------------
    try:
        classDays = int(classData['skxq'])  # 天数
        classDays = http_week[classDays]
    except (ValueError, TypeError, Exception):
        classDays = 8
        classDays = http_week[classDays]
    # 课程开始 ---------------------------------
    try:
        classTime = str(classData['skjc'])
    except (ValueError, TypeError, Exception):
        classTime = "??"
    # 课程结束 ---------------------------------
    try:
        tmpTime = int(str(classData['cxjc']))
        classEnds = int(classTime) + tmpTime - 1
    except (ValueError, TypeError, Exception):
        classEnds = 0
    # 课程教师 ---------------------------------
    try:
        classTech = str(classData['skjs'][0:9])
    except (ValueError, TypeError, Exception):
        classTech = "未知教师"
    # 输出模块 ------------------------------------------------------------------
    print(
        "%02d %9s %+15s %-2s %+3s %-4s %+4s %+6s 周%+2s %+02s-%-02s节 %-10s" % (
            # 课程编号  课程序号  课程名称   上课校区   课程余量   课程位置
            classNums, classUUID, className, classArea, classFree, roomBuild,
            # 课程教室  课程周数  课程天数   开始时间   结束时间   课程老师
            classRoom, classWeek, classDays, classTime, classEnds, classTech
        )
    )
