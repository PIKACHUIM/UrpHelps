import os
import hashlib
from PIL import Image
from urps_conf import *

http_urls_logs = "http://zhjw.scu.edu.cn/j_spring_security_check"
http_urls_caps = "http://zhjw.scu.edu.cn/img/captcha.jpg"
# -----------------------------------------------主登录模块--------------------------------------------------
def urps_logi():
    os.system('cls')
    os.system('color 2f')
    print()
    print("                                       ■■■■■■■■■■■")
    print("                                       ■                  ■")
    print("                                       ■   SCU教务处助手  ■")
    print("                                       ■                  ■")
    print("                                       ■      Ver1.0      ■")
    print("                                       ■■■■■■■■■■■")
    print("")
    print("------------------------------------------------登录-------------------------------------------------")
    print()
    try:
        http_caps = http_main.get(http_urls_caps)
    except:
        urps_outs('nete')
        urps_outs('retr')
        return -2
    print("[验证码获取]：", http_caps.status_code, "(此处200为正常)")
    with open('code.jpg', 'wb') as http_capf:
        http_capf.write(http_caps.content)
        http_capf.close()
    http_capi = Image.open('code.jpg')
    http_capi.show()
    print()
    http_code = input("[输入验证码]：")
    print()
    http_user = input("[输入你学号]：")
    print()
    http_pass = input("[输入你密码]：")
    print()
    print("----------------------------------------------正在登陆-----------------------------------------------")
    http_hash = hashlib.md5(http_pass.encode()).hexdigest()
    post_data = {
        "j_username": http_user,
        "j_password": http_hash,
        "j_captcha": http_code}
    try:
        http_post = http_main.post(http_urls_logs, post_data, http_head)
    except:
        print("[严重的错误]：网络连接中断，请确保网络稳定")
        urps_outs('retr')
        return -2
    else:
        pass
    print("[验证码提交]：", http_post.status_code, "(此处200为正常)")
    print()
    if http_post.text.find('验证码错误') != -1:
        print("[登录未成功]：验证码不正确")
        print()
        urps_outs('retr')
        return -1
    if http_post.text.find('的培养方案') == -1:
        print("[登录未成功]：账号密码错误")
        print()
        urps_outs('retr')
        return 1
    if http_post.text.find('的培养方案') != -1:
        print("[已成功登录]：成功登录系统")
        return 0
