import time
from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()

# cookies = {"LIVE_BUVID":"AUTO7315340732321697", "fts":"1534073233",
# "buvid3":"FDD8C3F2-8C70-4DA1-826F-DBC67077890C19233infoc",
# "stardustvideo":"1", "CURRENT_FNVAL":"16", "CURRENT_QUALITY":"80", 
# "im_notify_type_204975100":"0", "rpdid":"|(um~RRJYk)u0J'ullY|u~J|R", 
# "sid":"ie1q6w1n","_uuid":"F450CA73-33E0-4DBA-3F64-0F5890A7643896087infoc",
# "UM_distinctid":"16e372b73f06d5-0b6cabbfbb563-7711b3e-240000-16e372b73f1bd7", "finger":"3f3919d0", "laboratory":"1-1",
# "bp_t_offset_204975100":"338731185738744835",
# "INTVER":"1", "DedeUserID":"203478513", 
# "DedeUserID__ckMd5":"011ef155d24a7425", 
# "SESSDATA":"761e2763%2C1580911055%2C2588ab11", 
# "bili_jct":"0b0d34a472aaa5ac786dec9811053c4c"}

# cookies = "LIVE_BUVID=AUTO7315340732321697; fts=1534073233; buvid3=FDD8C3F2-8C70-4DA1-826F-DBC67077890C19233infoc; stardustvideo=1; CURRENT_FNVAL=16; CURRENT_QUALITY=80; im_notify_type_204975100=0; rpdid=|(um~RRJYk)u0J'ullY|u~J|R; sid=ie1q6w1n; _uuid=F450CA73-33E0-4DBA-3F64-0F5890A7643896087infoc; UM_distinctid=16e372b73f06d5-0b6cabbfbb563-7711b3e-240000-16e372b73f1bd7; finger=3f3919d0; laboratory=1-1; bp_t_offset_204975100=338731185738744835; INTVER=1; DedeUserID=203478513; DedeUserID__ckMd5=011ef155d24a7425; SESSDATA=761e2763%2C1580911055%2C2588ab11; bili_jct=0b0d34a472aaa5ac786dec9811053c4c"

# for c in cookies:
#     print(c)
# driver.add_cookie({"cookie": cookies})


# cookies = [{'domain': '.bilibili.com', 'expiry': 1580913169.275982, 'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': '67ef530491510dc9fe9988c4bd63d0c7'}, {'domain': '.bilibili.com', 'expiry': 1580913169.275961, 'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': 'b00d56ca%2C1580913169%2Cb3489c11'}, {'domain': '.bilibili.com', 'expiry': 1580913169.275875, 'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '203478513'}, {'domain': '.bilibili.com', 'expiry': 1609857155.215984, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': '4lkrk42x'}, {'domain': '.bilibili.com', 'expiry': 1672929152.555011, 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure':False, 'value': 'BD7006D5-E9BA-4F7D-AA8C-484662D62CF3155824infoc'}, {'domain': '.bilibili.com', 'expiry': 1580913169.275943, 'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '011ef155d24a7425'}, {'domain': '.bilibili.com', 'expiry': 1609857152, 'httpOnly': False,'name': '_uuid', 'path': '/', 'secure': False, 'value': '9FED5741-6E95-0770-7D67-ED2E721CCB7B52235infoc'}, {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'INTVER', 'path': '/', 'secure': False, 'value': '1'}]
cookies = [{'domain': '.bilibili.com', 'expiry': 1580913169.275982, 'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': '67ef530491510dc9fe9988c4bd63d0c7'}, {'domain': '.bilibili.com', 'expiry': 1580913169.275961, 'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': 'b00d56ca%2C1580913169%2Cb3489c11'}, {'domain': '.bilibili.com', 'expiry': 1580913169.275875, 'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '203478513'}, {'domain': '.bilibili.com', 'expiry': 1609857155.215984, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': '4lkrk42x'}, {'domain': '.bilibili.com', 'expiry': 1672929152.555011, 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure':False, 'value': 'BD7006D5-E9BA-4F7D-AA8C-484662D62CF3155824infoc'}, {'domain': '.bilibili.com', 'expiry': 1580913169.275943, 'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '011ef155d24a7425'}, {'domain': '.bilibili.com', 'expiry': 1609857152, 'httpOnly': False,'name': '_uuid', 'path': '/', 'secure': False, 'value': '9FED5741-6E95-0770-7D67-ED2E721CCB7B52235infoc'}, {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'INTVER', 'path': '/', 'secure': False, 'value': '1'}]

for c in cookies:
    #并不是所有cookie都含有expiry 所以要用dict的get方法来获取
    if isinstance(c.get('expiry'), float):
        c['expiry'] = int(c['expiry'])
    driver.add_cookie(c)

driver.get("https://www.bilibili.com/")
