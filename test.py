import top.api

appkey = '31300145'
secret = '581b6ec91f1405070bbf01ec0f79ca61'
req = top.api.TbkItemInfoGetRequest()
req.set_app_info(top.appinfo(appkey, secret))

req.num_iids = "626134552855"
req.platform = 1
req.ip = "11.22.33.43"
try:
  resp= req.getResponse()
  print(resp)
except Exception as e:
  print(e)