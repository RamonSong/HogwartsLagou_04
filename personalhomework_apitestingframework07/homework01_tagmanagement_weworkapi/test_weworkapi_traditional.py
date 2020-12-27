import json

import requests

corpid = "wwca40714985990022"
corpsecret = "Gh9s-2UCDTNuDkTMsi4hiYvgHZEeSvf_7r6N3Xsxx38"

def test_tag_get():
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        params={'corpid' : corpid, 'corpsecret' : corpsecret},
    )
    token = r.json()['access_token']
    print(json.dumps(r.json(), indent=2))

    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params = {'access_token' : token},
        json={
            'tag_id': []
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0


    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        params={'access_token' : token},
        json={
            'group_name': 'group_demo_1218',
            'tag' : [
                {
                    'name': 'tag_demo_1218'
                }
            ]
        }
    )
    print(json.dumps(r.json(),indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0


    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={'access_token': token},
        json={
            'tag_id': []
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0


    # r = requests.post(
    #     "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
    #     params={'access_token' : token},
    #     json={
    #         'tag_id': []
    #     }
    # )
    # print(json.dumps(r.json(), indent=2))
    # assert r.status_code == 200
    # assert r.json()['errcode'] == 0