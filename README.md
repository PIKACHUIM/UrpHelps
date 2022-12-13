# 四川大学综合教务系统助手 - 皮卡丘版本

## Assistant of Comprehensive Educational Administration System of SCU

## 软件介绍

四川大学综合教务系统助手（皮卡丘版本）是一款优化四川大学本科教务系统选课体验的程序

**本程序是一款独立软件，不依赖于浏览器和教务处系统，本程序不保存或者上传密码、学号等任何信息**

###### **许可：GPL-3.0  CC BY-NC-SA 3.0**

## 免责声明

### 	使用本程序，表示您已经充分理解并完全同意下列全部条款和约束

- #### 数据使用

  本程序不存储到磁盘、保存、上传任何用户输入的或者直接或间接的从任何地方收集的用户信息

  所有数据均临时存储在RAM内存中，本程序及其作者也不会收集用户信息，不对任何形式的泄密承担责任

- #### 法律责任

  本程序的一切数据来源均通过【四川大学本科教务处系统】获得，其登录信息由用户提供

  本程序不提供一切违背《四川大学学生守则》的行为以及方法，不承担一切因为选课导致的问题和责任

## 功能介绍

- ### 绩点计算

  - #### 成绩查询

    可以看到所有公开或者部分没公开的成绩，并且可以看到按照等级标注的成绩的真实分数

  - #### 绩点计算

    通过先折算后加权的计算方法，计算当前有效成绩的全部绩点。

    注意：许多国外学校和国内学校对绩点的计算方式并不相同，因此，本绩点计算功能仅作参考

- ### 一键评教

  自动完成评教，一键评教全部给【好评】，因此，如果你不想给某个课程/老师好评，请先手动评教

  自动评教并不会覆盖之前已经评教的内容，无论是自动还是手动，好评文字来自预设随机模板

- ### 自动选课

  - #### 使用方法

    > 1. 进入菜单，按【1】添加课程
    >
    > 2. 输入【课程/学院/教师】的部分关键字，【回车】查找
    >
    > 3. 查看结果，根据结果输入课程前方的【序号】，然后回车
    >
    >    注意：你可以输入多个编号，用空格隔开
    >
    > 4. 等待添加完成，按【回车】返回
    >
    > 5. 不要【返回主菜单】，可以重复添加课程
    >
    > 6. 添加完成后，按【4】进行抢课
    >
    > 7. 此时会让你输入延迟，建议输入【2】~【4】，输入【1】会按照最快速度抢课
    >
    > 8. 等待直到抢课完成
    >
    > 9. 抢课的时候你可以按下CTRL+C返回上一层，但只要不返回主菜单，数据就不会丢失

  - #### 注意事项

    - 同一个关键词重复添加会被【覆盖】，因此不用重复用一个关键词查找，其实一个关键词一次性就可以选择多个序号，用空格隔开就好，比如【1 2 3 4】就会选择前四个

    - 正常情况延迟时间不建议输入【1】，会较增大jwc网络负载，同时部分老电脑和笔记本会变得很卡，甚至比更大的延迟处理速度慢，因此你需要多比较一下

- ### 查看课表

  - 查看课表可能有Bug，比如显示时间和周不太一样，一切以教务处最新的记录为准，本程序不保证准确性

## 更新记录

- ### 0.3

  - #### 0.3.2

    ###### DEC 13 2022

    > - 修复了选课的一些问题，改变了脚本内容
    > - 改变了打包方式，优化了课程输出内容
    >

  - #### 0.3.1

    ###### SEP 14 2022

    > - 修复了接口更新导致无法登录的BUG
    > - 绩点计算和成绩查看失效了，暂时屏蔽
    > - 新增配置，可以在config设置账号密码
    >

  - #### 0.3.0 

    ###### DEC 29 / 2020

    > - 新增了多关键词搜索抢课机制，现在不止能查询一个关键词抢课了
    >
    > - 新增中断机制异常捕获处理，可以中途使用CTRL+C来返回上一层了（而不是关闭程序）
    >
    > - 优化异常处理，闪退几率<u>应该</u>会下降
    >
    > - 优化了提示信息

- ### 0.2

  - #### 0.2.3

    ###### JUN 27 / 2020

    > - 修复了自动抢课可能出现的部分异常导致的闪退问题
    > - 针对教务处对多次刷新会启用验证码进行了一些优化

  - #### 0.2.2

    ###### JUN 22 / 2020

    > - 教务处换接口了，本次升级同步更换了接口参数

  - #### 0.2.1

    ###### MAR 07 / 2020

    > - 优化了一键评教
    > - 改善了抢课逻辑，修复了可能会抢错的一些bug
    > - 修改了抢课的时间延迟逻辑
  - #### 0.2.0

    ###### DEC 30 / 2019

    > - 新增了一键评教
    >
    > - 新增了绩点计算
    >
    > - 新增了查看成绩
    >
    > - 改善了抢课逻辑
    >
    > - 重构了全部代码
    >
    > - 修改了退出登录方式
    >
    > - 增加了异常处理

- ### 0.1

  - #### 0.1.0

    ###### DEC 17 / 2018

    > - 增加了抢课功能
    >
    > - 增加了选课结果
    >

