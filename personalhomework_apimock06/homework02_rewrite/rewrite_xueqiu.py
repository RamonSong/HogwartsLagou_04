import json


from mitmproxy import http


# def response(flow:http.HTTPFlow):
#     # 加上过滤条件
#     if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
#         #拿到响应数据，转化为Python对象
#         data =json.loads(flow.response.text)
#         # 修改对应的字段的值
#         data['data']['items'][0]['quote']['name'] = "rewrite_hogwarts"
#         # 修改后的数据转换为字符串，赋值给原始响应数据
#         flow.response.text = json.dumps(data)

def response(flow:http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.text)
        data["data"]["items"][0]["quote"]["name"] = "阿里巴巴-SW"
        data["data"]["items"][1]["quote"]["name"] = "明大嘉和明大嘉和"
        data["data"]["items"][2]["quote"]["name"] = ""
        flow.response.text = json.dumps(data)