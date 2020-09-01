import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from rest_framework import permissions
# from rest_framework.views import APIView
from shares.models import SharesCategory
import baostock as bs
import pandas as pd
import numpy as np

class Shares_category(View):
    def get(self, request, *args, **kwargs):
        queryset = SharesCategory.objects.all()
        shares_cate_list = []
        for item in queryset:
            shares_cate_list.append({
                'uid': item.uid,
                'industry': item.industry,
                'industryClassification': item.industryClassification,
                'created_at': item.created_at,
                'updated_at': item.updated_at,
                'count': item.count
            })
        return JsonResponse(shares_cate_list, safe=False)

class Shares_category_export(View):
    def get(self, request, *args, **kwargs):
        lg = bs.login()
        rs = bs.query_stock_industry()
        # print(rs)
        data_list = []
        while (rs.error_code=='0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        result1 = pd.DataFrame(result['industry'])
        result1['count'] = pd.Series(np.random.randint(1, 2, 4061))
        result1['industryClassification'] = result['industryClassification']
        result1 = result1.groupby('industry').sum()
        shares_cate_list = []
        for index, row in result1.iterrows():
            cate_obj = SharesCategory(industry=index, industryClassification='申万一级行业', count=row['count'])
            cate_obj.save()
            shares_cate_list.append({
                'industry': index,
                'industryClassification': '申万一级行业',
                'count': row['count']
            })
        bs.logout()
        return JsonResponse(shares_cate_list, safe=False)