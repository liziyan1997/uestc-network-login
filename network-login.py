# python = 3.6
# author: garylee

import time,requests
from selenium import webdriver

try:
    r = requests.get('https://www.baidu.com')
    r.raise_for_status()
except:
    driver = webdriver.Chrome()
    driver.get('http://192.168.9.8/srun_portal_pc.php?ac_id=1&')

    username = driver.find_element_by_id('uname')
    username.send_keys('username')  # your username
    pswd = driver.find_elements_by_name('password')
    pswd[0].send_keys('password')   # your password

    time.sleep(1)

    loginButton = driver.find_element_by_id('school')
    loginButton.click()

    driver.quit()
else:
    print('already online')



