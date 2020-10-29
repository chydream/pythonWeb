from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import top.api

class Tbk_item_info(View):
    """
    淘宝客商品详情
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    def get(self, request):
        req = top.api.TbkItemInfoGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.num_iids = "626134552855"
        req.platform = 1
        req.ip = "11.22.33.43"
        try:
            resp = req.getResponse()
            # print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_material_search(View):
    """
    淘宝客物料搜索
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        req = top.api.TbkDgMaterialOptionalRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))
        req.start_dsr = 10
        req.page_size = 20
        req.page_no = 1
        req.platform = 1
        # req.end_tk_rate = 1234
        # req.start_tk_rate = 1234
        req.end_price = 10
        req.start_price = 10
        # req.is_overseas = False
        # req.is_tmall = False
        # req.sort = "tk_rate_des"
        # req.itemloc = "杭州"
        # req.cat = "16,18"
        req.q = "女装"
        # req.material_id = 2836
        # req.has_coupon = False
        # req.ip = "13.2.33.4"
        req.adzone_id = 110853300272
        # req.need_free_shipment = True
        # req.need_prepay = True
        # req.include_pay_rate_30 = True
        # req.include_good_rate = True
        # req.include_rfd_rate = True
        # req.npx_level = 2
        # req.end_ka_tk_rate = 1234
        # req.start_ka_tk_rate = 1234
        # req.device_encrypt = "MD5"
        # req.device_value = "xxx"
        # req.device_type = "IMEI"
        # req.lock_rate_end_time = 1567440000000
        # req.lock_rate_start_time = 1567440000000
        # req.longitude = "121.473701"
        # req.latitude = "31.230370"
        # req.city_code = "310000"
        # req.seller_ids = "1,2,3,4"
        # req.special_id = "2323"
        # req.relation_id = "3243"
        try:
            resp = req.getResponse()
            # print(resp)
        except Exception as e:
            resp = {}
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_material_optimus(View):
    """
    淘宝客物料精选
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        req = top.api.TbkDgOptimusMaterialRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))
        limit = request.GET.get('limit', 20)
        page = request.GET.get('page', 1)
        material_id = request.GET.get('material_id', 4092)
        req.page_size = limit
        req.adzone_id = 110853300272
        req.page_no = page
        req.material_id = material_id
        # req.device_value = "xxx"
        # req.device_encrypt = "MD5"
        # req.device_type = "IMEI"
        # req.content_id = 323
        # req.content_source = "xxx"
        # req.item_id = 33243
        # req.favorites_id = "123445"
        try:
            resp = req.getResponse()
            # print(resp)
        except Exception as e:
            resp = {}
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_item_convert(View):
    """
    淘宝客商品链接转换
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        item_id = request.GET.get('item_id', '')
        req = top.api.TbkItemConvertRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.fields = "num_iid,click_url"
        req.num_iids = item_id
        req.adzone_id = 110853300272
        req.platform = 1
        # req.unid = "demo"
        # req.dx = "1"
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_itemid_coupon(View):
    """
    根据宝贝id批量查询优惠券
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        item_id = request.GET.get('item_id', '')
        req = top.api.TbkItemidCouponGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.platform = 1
        req.pid = self.pid
        req.num_iids = item_id
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_coupon_convert(View):
    """
    单品券高效转链API
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        item_id = request.GET.get('item_id', '')
        req = top.api.TbkCouponConvertRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.item_id = item_id
        req.adzone_id = 110853300272
        req.platform = 1
        # req.external_id = "12345"
        # req.special_id = "12345"
        # req.relation_id = "12345"
        # req.xid = "abcdefg"
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_item_word(View):
    """
    商品出词
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        item_id = request.GET.get('item_id', '')
        req = top.api.TbkItemWordGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.item_id = item_id
        req.adzone_id = 110853300272
        req.count = 5
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)


class Tbk_shop_search(View):
    """
    店铺搜索
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        req = top.api.TbkShopGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.fields = "user_id,shop_title,shop_type,seller_nick,pict_url,shop_url"
        req.q = "女装"
        # req.sort = "commission_rate_des"
        # req.is_tmall = False
        # req.start_credit = 1
        # req.end_credit = 20
        # req.start_commission_rate = 2000
        # req.end_commission_rate = 123
        # req.start_total_action = 1
        # req.end_total_action = 100
        # req.start_auction_count = 123
        # req.end_auction_count = 200
        req.platform = 1
        req.page_no = 1
        req.page_size = 20
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_shop_recommend(View):
    """
    店铺关联推荐
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        user_id = request.GET.get('user_id', '')
        req = top.api.TbkShopRecommendGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.fields = "user_id,shop_title,shop_type,seller_nick,pict_url,shop_url"
        req.user_id = user_id
        req.count = 20
        req.platform = 1
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_shop_convert(View):
    """
    店铺店铺转链
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        user_id = request.GET.get('user_id', '')
        req = top.api.TbkShopConvertRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.fields = "user_id,click_url"
        req.user_ids = user_id
        req.platform = 1
        req.adzone_id = 110853300272
        # req.unid = "demo"
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)


class Tbk_activity_info(View):
    """
    官方活动转链
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        material_id = request.GET.get('material_id', '')
        user_id = request.GET.get('user_id', '')
        req = top.api.TbkActivityInfoGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))

        req.adzone_id = 110853300272
        req.sub_pid = self.pid
        # req.relation_id = 123
        req.activity_material_id = material_id
        # req.union_id = "demo"
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)

class Tbk_tpwd_create(View):
    """
    官方活动转链
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        req = top.api.TbkTpwdCreateRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))
        user_id = request.GET.get('user_id', '')
        text = request.GET.get('text', '')
        url = request.GET.get('url', '')
        req.user_id = user_id
        req.text = text
        req.url = "https://uland.taobao.com/"
        # req.logo = "https://uland.taobao.com/"
        # req.ext = "{}"
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)


class Tbk_spread(View):
    """
    官方活动转链
    """
    appkey = '31300145'
    secret = '581b6ec91f1405070bbf01ec0f79ca61'
    pid = 'mm_15446204_2034900375_110853300272'
    def get(self, request):
        req = top.api.TbkSpreadGetRequest()
        req.set_app_info(top.appinfo(self.appkey, self.secret))
        url = request.GET.get('url', '')
        req.requests = [url]
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)