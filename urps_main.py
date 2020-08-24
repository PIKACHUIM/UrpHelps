import os
import json
import requests

from urps_auth import urps_logi
from urps_menu import urps_menu




# -----------------------------------------------主循环部分--------------------------------------------------
os.system('mode con cols=101 lines=50')
os.system('title 皮卡丘SCU-URP助手 V1.0')
while 1:
    if urps_logi() == 0:
        while urps_menu() == -1:
            pass
