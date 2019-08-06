# coding:utf-8
import requests
import pandas as pd
import time

cookie = 'xsessionid=3450c46024e513aa27b6ea517d106cd549363200; dsessionid=29452d54b1c373ab358ff29790ddd9cfa16fbe0a; WA_FROM=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8b_qTERviD33cTd-EuUql98bmGXz70y6mKbmc8VQeOVC1PZrs-WcKeVC4EDMxTZY%26wd%3D%26eqid%3Da7a7b76300120fc5000000035d49196f; WA_TO=%2F; __jsluid_s=8da5cf4d42156ff3c3279d5c04f170d7; gr_user_id=b2e42176-c09e-4e8b-bda4-a16ed707e5d4; _af_init=a2b5988024b68a0e228da77a649644fd; gr_session_id_a20c274701ec9918=7d936d0e-d71a-47b1-9c35-153f3bf64b31; gr_cs1_7d936d0e-d71a-47b1-9c35-153f3bf64b31=user_id%3A28721481; gr_session_id_a20c274701ec9918_7d936d0e-d71a-47b1-9c35-153f3bf64b31=true; nsession=cb76f11eb978c56a5e860b42b4e03ee8; nsession2=fc1e05cd503b3a9948db1d124e9b14bb; JSESSIONID=d2f9f2f7-7586-4e2b-ae75-102ecd58acb2; DRSESSIONID=d2f9f2f7-7586-4e2b-ae75-102ecd58acb2; nsession2=5630e414e33a9bf7f1fa6c63c5f84171'

# 消息头数据
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': cookie,
    'Host': 'www.dianrong.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dianrong.com/account/my-account',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'X-Tingyun-Id': 'vI_KkaHsbFU;r=72535364',

}

requests.packages.urllib3.disable_warnings()

url = 'https://www.dianrong.com/feapi/plans/plan-notes/groups?includeHuoQiPlan=true'

r = requests.get(url, headers=headers, verify=False)
groupItems = r.json()



def anaDetail(loanId):
    detailUrl = 'https://www.dianrong.com/feapi/loans/' + str(loanId)
    detailResult = requests.get(detailUrl, headers=headers, verify=False)
    detailJson = detailResult.json()
    print(detailJson)


def anaItem(planId):
    res = pd.DataFrame(columns=(
        'loanId', 'loanStatus', 'loanStatusText', 'intRate', 'loanClass', 'remainingPaymentsCount', 'subType',
        'subTypeText',
        'holdingAmount', 'loanTotalTerms', 'loanPaidTerms', 'appAmount', 'classification', 'todayData'))
    page = 0
    pagesize = 20
    while True:
        planUrl = 'https://www.dianrong.com/api/v2/asset/plan-notes/loans?planId=' + str(planId) + '&page=' + str(
            page) + '&pageSize=' + str(pagesize)
        print("planUrl:", planUrl)
        planResult = requests.get(planUrl, headers=headers, verify=False)
        planJson = planResult.json()
        # print(planResult.text)
        planSize = planJson['content']['totalRecords']
        planArray = planJson['content']['userHoldLoanItems']
        page = page + 1
        for item in planArray:
            print(item)
            a = {"loanId": item['loanId'], "loanStatus": item['loanStatus'], "loanStatusText": item['loanStatusText'],
                 "intRate": item['intRate'],
                 "loanClass": item['loanClass'], "remainingPaymentsCount": item['remainingPaymentsCount'],
                 "subType": item['subType'], "subTypeText": item['subTypeText'], "holdingAmount": item['holdingAmount'],
                 "loanTotalTerms": item['loanTotalTerms'], "loanPaidTerms": item['loanPaidTerms'],
                 "appAmount": item['appAmount'], "classification": item['classification'],
                 "todayData": item['todayData']}
            res = res.append(a, ignore_index=True)
        if planSize <= page * pagesize:
            res.to_csv('planId_' + str(int(time.time())) + '_data.csv', encoding='utf-8-sig')
            break


for item in groupItems['content']['list']:
    planId = item['planId']
    anaItem(planId)

