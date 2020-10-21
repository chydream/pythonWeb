import top.api

appkey = "31300145"
secret = "581b6ec91f1405070bbf01ec0f79ca61"
adzone_id = "mm_15446204_2034900375_110853300272"

def get_tbk_coupon(keyword):
    req = top.api.TbkItemInfoGetRequest()
    req.set_app_info(top.appinfo(appkey, secret))
    req.aazone_id = adzone_id
    req.platform = 1
    req.cat = "16,18"
    req.page_size = 5
    req.q = keyword
    req.page_no = 1
    try:
        resp = req.getResponse()
        for r in resp['tbk_dg_item_coupon_get_response']['results']['tbk_coupon']:
            conpon_url = r['coupon_click_url']
            coupon_text = r['title']
            print(conpon_url, coupon_text)
            generate_token(conpon_url, coupon_text)
    except Exception as e:
        print(e)

def generate_token(url, text):
    req = top.api.TbkTpwdCreateRequest()
    req.set_app_info(top.appinfo(appkey, secret))
    req.text = text
    req.url= url
    req.logo="https://uland.taobao.com/"
    req.ext="{}"
    try:
        resp = req.getResponse()
        print(resp)
    except Exception as e:
        print(e)

def get_tbk_item_info():
    req = top.api.TbkItemInfoGetRequest()
    req.set_app_info(top.appinfo(appkey, secret))
    req.num_iids = "622084715230"
    req.platform = 1
    req.ip = "11.22.33.43"
    try:
        resp = req.getResponse()
        print(resp)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    get_tbk_item_info()