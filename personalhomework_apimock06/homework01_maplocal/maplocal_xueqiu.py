from mitmproxy import http


# def request(flow:http.HTTPFlow):
#     # 发起请求，判断url是否为预期值
#     if 'quote.json' in flow.request.pretty_url:
#         # 打开本地的数据文件
#         with open('/Users/v_songchao01/PycharmProjects/Hogwarts_Lagou04/gupiaomessage.json') as f:
#             # 创建一个response
#             flow.response = http.HTTPResponse.make(
#                 200,
#                 # 读取文件中的数据作为返回内容
#                 f.read(),
#                 {'Content-Type': "application/json"}
#             )


def request(flow:http.HTTPFlow):
    if "query.json" in flow.request.pretty_url:
        with open("/Users/v_songchao01/desktop/quote01.json") as f:
            flow.response = http.HTTPResponse.make(
                200,
                f.read(),
                {"Content-Type": "application/json"}
            )

