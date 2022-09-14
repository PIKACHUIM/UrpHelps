import hashlib
import json

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
        http_page = http_main.get(http_urls_init)
        print("[登录页获取]：", http_page.status_code, "(此处200为正常)")
        if http_page.status_code != 200:
            urps_outs('err_')
            urps_outs('retr')
            return -2
        else:
            token_value = http_page.text.find("tokenValue")
            if token_value > 0:
                token_value = http_page.text[token_value + 37:token_value + 69]
                print("[随机码获取]：", token_value)
            else:
                urps_outs('e_tv')
                urps_outs('retr')
                return -2
        http_caps = http_main.get(http_urls_caps)
    except requests.exceptions.ConnectionError:
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
    try:
        config_flag = True
        with open("config.ini", 'r') as config_file:
            config_json = json.loads(config_file.read())
            if not config_json['autoVery']:
                config_flag = False
                print("[登录页获取]：未配置自动登录")
            if len(config_json['username']) <= 0 \
                    or len(config_json['password']) <= 0:
                config_flag = False
                print("[登录页获取]：未配置账号密码")
            else:
                http_user = config_json['username']
                http_pass = config_json['password']
    except FileNotFoundError:
        config_flag = False
        print("[登录页获取]：找不到配置文件")
    except json.decoder.JSONDecodeError:
        config_flag = False
        print("[登录页获取]：配置文件转换错误")
    except KeyError:
        config_flag = False
        print("[登录页获取]：配置文件读取错误")
    if not config_flag:
        http_user = input("[输入你学号]：")
        print()
        http_pass = input("[输入你密码]：")
        print()
    print("----------------------------------------------正在登陆-----------------------------------------------")
    http_hash = hashlib.md5(http_pass.encode()).hexdigest()
    post_data = {
        "tokenValue": token_value,
        "j_username": http_user,
        "j_password": http_hash,
        "j_captcha": http_code}
    try:
        http_post = http_main.post(http_urls_logs, post_data, http_head)
    except requests.exceptions.ConnectionError:
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
    elif http_post.text.find('token校验失败') != -1:
        print("[登录未成功]：token校验失败")
        print()
        urps_outs('retr')
        return -1
    elif http_post.text.find('的培养方案') == -1:
        print("[登录未成功]：账号密码错误")
        print()
        urps_outs('retr')
        return 1
    if http_post.text.find('的培养方案') != -1:
        print("[已成功登录]：成功登录系统")
        return 0
