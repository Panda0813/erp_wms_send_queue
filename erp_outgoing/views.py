from rest_framework import generics, serializers
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.ext_utils import REST_FAIL, REST_SUCCESS

import traceback
import logging

logger = logging.getLogger('django')


@api_view(['GET'])
def send_data_to_wms(request):
    query_str = request.META.get('QUERY_STRING', '')
    print(query_str)
    return REST_SUCCESS({'msg': '推送成功'})
