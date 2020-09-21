from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import top.api

class Tbk_list(View):
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
            print(resp)
        except Exception as e:
            resp = []
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

        req.page_size = 20
        req.adzone_id = 110853300272
        req.page_no = 1
        req.material_id = 4092
        # req.device_value = "xxx"
        # req.device_encrypt = "MD5"
        # req.device_type = "IMEI"
        # req.content_id = 323
        # req.content_source = "xxx"
        # req.item_id = 33243
        # req.favorites_id = "123445"
        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            resp = []
            print(e)
        return JsonResponse(resp, safe=False)