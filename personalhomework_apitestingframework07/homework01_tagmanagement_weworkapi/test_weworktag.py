

import json

import pytest
import requests

from personalhomework_apitestingframework07.homework01_tagmanagement_weworkapi.wework_tag import Tag

# corpid = "wwca40714985990022"
# corpsecret = "Gh9s-2UCDTNuDkTMsi4hiYvgHZEeSvf_7r6N3Xsxx38"

class TestWeworkTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()


    def test_tag_list(self):
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    @pytest.mark.parametrize("group_names, tag_names", [
        ["group_demo_1218", [{'name': 'tag_demo_1218'}]],
        ["group_demo_1218", [{'name': 'tag_demo_1218'}], [{'name': 'tag_demo_1218'}]]
    ])
    def test_tag_add(self, group_names, tag_names):
        r = self.tag.add(group_names, tag_names)
        assert r.status_code == 200
        # assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        group = [group for group in r.json()['tag_group'] if r.json()['group_name'] == group_names][0]
        tags = [{'name' : tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_names
        assert tags == tag_names


    @pytest.mark.parametrize()
    def test_tag_delete(self, tag_ids, group_ids):
        self.tag.delete()
