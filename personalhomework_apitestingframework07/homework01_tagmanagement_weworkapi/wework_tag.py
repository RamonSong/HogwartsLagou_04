import json

import requests

corpid = "wwca40714985990022"
corpsecret = "Gh9s-2UCDTNuDkTMsi4hiYvgHZEeSvf_7r6N3Xsxx38"
class Tag:
    def __init__(self):
        self.token = ''

    def get_token(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={'corpid': corpid, 'corpsecret': corpsecret},
        )


        print(json.dumps(r.json(), indent=2))
        self.token = r.json()['access_token']



    def list(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={'access_token': self.token},
            json={
                'tag_id': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r


    def add(self, group_name, tags):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={'access_token': self.token},
            json={
                'group_name': group_name,
                'tag': tags
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r


    def delete(self, tag_ids, group_ids):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={'access_token': self.token},
            json={
                'tag_id': tag_ids,
                'group_id':group_ids
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r


    def update(self, tag_id, name, order_id):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            params={'access_token': self.token},
            json={
                "id": tag_id,
                "name": name,
                "order": order_id
            }
        )
        print(json.dumps(r.json(),indent=2))
        return r



    def clear_all(self):
        r = self.list()
        group_ids = [group['group_id'] for group in r.json()['tag_group']]
        self.delete(group_ids, None)
        return self.list()



