# coding:utf-8
import requests

cookie = 'xsessionid=e78dd182d5f157981abc14451cf7a734f44fbd47; dsessionid=3b7ead4545e292eaf024cfa1f9781cd61d6d50ac; __jsluid_s=2790368bab9d6302ed790dd29ad8e332; _af_init=0ef8c61c9c96e1f46ada50bcb1e0ec49; gr_user_id=95dd80af-8830-47c4-b6df-eb9bbdcf6ab6; nsession=cb76f11eb978c56a5e860b42b4e03ee8; gr_session_id_a20c274701ec9918=2bb827d1-73a0-4127-bd3a-74212e78e9d9; nsession2=fc1e05cd503b3a9948db1d124e9b14bb; gr_session_id_a20c274701ec9918_2bb827d1-73a0-4127-bd3a-74212e78e9d9=true; nsession2=7b30bee7b520b389a01b45ab4fa9c2db; gr_cs1_2bb827d1-73a0-4127-bd3a-74212e78e9d9=user_id%3A28721481; JSESSIONID=e6a6aeba-64d2-4d23-9a21-b91189e0c9ff; DRSESSIONID=e6a6aeba-64d2-4d23-9a21-b91189e0c9ff; WA_TO=%2Faccount%2Fmy-account'

# 消息头数据
headers = {
    'User-Agent': 'self-defind-user-agent',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie': cookie
}

requests.packages.urllib3.disable_warnings()

url = 'https://www.dianrong.com/feapi/plans/plan-notes/groups?includeHuoQiPlan=true'

r = requests.get(url, headers=headers, verify=False)
groupItems = r.json()


def anaItem(planId):
    page = 0
    pagesize = 20
    while True:
        planUrl = 'https://www.dianrong.com/feapi/transaction/hlz/investmentList?page=' + str(
            page) + '&pageSize=' + str(pagesize) + '&selectType=INVESTMENT_TRANSFER_REPAYMENT&planId=' + str(planId)
        print(planUrl)
        planResult = requests.get(planUrl, headers=headers, verify=False)
        planJson = planResult.json()
        try:
            planLen = len(planJson['content']['list'])

            print(planLen)
            print(planJson)
            if planLen > 0:
                page = page + 1
            else:
                break
        except Exception as err:
            break


for item in groupItems['content']['list']:
    planId = item['planId']
    anaItem(planId)

