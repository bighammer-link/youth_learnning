import requests, re, json

# 设置代理，这个地方先不用改，代理失效的话再修改
proxy = {'https': 'https://127.0.0.1:7890'}
#填写openid，可以是多个账号的，多个账号的请用英文逗号隔开
openids = ['']
#server推送方式
SCKEY = ''


#  获取最新一期大学习的版本号
def getNewestVersionInfo(proxy):
    url = "http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getNewestVersionInfo"

    headers = {
        "Origin": "http://qndxx.youth54.cn",
        "Cookie": "JSESSIONID=756AF07760D382583821EC32F02C1520",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001031) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=",
        "Host": "qndxx.youth54.cn",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Length": "0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    try:
        response = requests.post(url, headers=headers, verify=False, timeout=20, proxies=proxy)
        if response.status_code == 200:
            result = json.loads(response.text)
            print('最新版本是：{}'.format(result['version']))
            return result['version']
        return ''
    except:
        return ''


# 获取你之前已经学过的版本号，用来检测是否已经学习最新的一期
def get_PersonStudyRecord(person_openid,proxy):
    url = "http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=queryPersonStudyRecord"
    headers = {
        "Origin": "http://qndxx.youth54.cn",
        "Cookie": "JSESSIONID=DF3D44A8E4A4FE910B5671C4DF2AB02A",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; WLZ-AN00 Build/HUAWEIWLZ-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4375 MMWEBSDK/20221206 Mobile Safari/537.36 MMWEBID/2483 MicroMessenger/8.0.32.2300(0x28002055) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Connection": "keep-alive",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=",
        "Host": "qndxx.youth54.cn",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Length": "0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    # 因为是是要获取你个人的学习记录，所以要求有openid
    data = {'openid': person_openid}
    response = requests.post(url, data=data, headers=headers, verify=False, timeout=5, proxies=proxy)
    if response.status_code == 200:
        result = json.loads(response.text)
        print('已经学习到：{}版本'.format(result['vds'][0]['version']))
        return result['vds'][0]['version']
    return ''

def passInfo(SCKEY,proxy,openids):
    url = 'http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=studyLatest'
    headers = {
        "Cookie": "JSESSIONID=551858919D81B6E40C56261D4F7ABA2E",
        "Origin": "http://qndxx.youth54.cn",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=",
        "Connection": "close",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Site": "same-origin",
        "Host": "qndxx.youth54.cn",
        "Accept-Encoding": "gzip, deflate",
        "Dnt": "1",
        "Sec-Fetch-Mode": "cors",
        "Te": "trailers",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Length": "48",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    nst_vn = getNewestVersionInfo(proxy)
    # 多个账号的openid,逐个进行学习
    for person_openid in openids:
        last_vn = get_PersonStudyRecord(person_openid,proxy)
        data = {'openid': person_openid,
                'version': nst_vn}
        if nst_vn != last_vn:
            response = requests.post(url=url,headers=headers,data=data,verify=False, timeout=5, proxies=proxy)
            if response.status_code == 200 and response.json()["errcode"] == "0":
                content = '{}已经完成本期大学习（当前版本：{}）'.format(person_openid,nst_vn)
                print(content)
                if SCKEY !='':
                    requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY,"青年大学习",content))
            else:
                content = '学习失败，请检查问题'
                print(content)
                if SCKEY != '':
                    requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, "青年大学习", content))
        else:
            content = '大学习还未更新（当前版本：{}）'.format(nst_vn)
            print(content)
            if SCKEY != '':
                requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY,"青年大学习",content))


if __name__ == "__main__":
    passInfo(SCKEY,proxy,openids)
