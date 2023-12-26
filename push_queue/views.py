from rest_framework import generics, serializers
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import traceback
import logging

logger = logging.getLogger('django')


@api_view(['POST'])
def send_data_to_wms(request):
    pass


@api_view(['POST'])
def receive_wms_data(request):
    pass
