"""
JSON API for the Order app
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from django.conf.urls import url

from .models import PurchaseOrder, PurchaseOrderLineItem
from .serializers import POSerializer, POLineItemSerializer


class POList(generics.ListCreateAPIView):
    """ API endpoint for accessing a list of Order objects

    - GET: Return list of PO objects (with filters)
    - POST: Create a new PurchaseOrder object
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = POSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    filter_backends = [
        DjangoFilterBackend,
    ]

    filter_fields = [
        'supplier',
    ]


class PODetail(generics.RetrieveUpdateAPIView):
    """ API endpoint for detail view of a PurchaseOrder object """

    queryset = PurchaseOrder.objects.all()
    serializer_class = POSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]


class POLineItemList(generics.ListCreateAPIView):
    """ API endpoint for accessing a list of PO Line Item objects

    - GET: Return a list of PO Line Item objects
    - POST: Create a new PurchaseOrderLineItem object
    """

    queryset = PurchaseOrderLineItem.objects.all()
    serializer_class = POLineItemSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    filter_backends = [
        DjangoFilterBackend,
    ]

    filter_fields = [
        'order',
        'part'
    ]


class POLineItemDetail(generics.RetrieveUpdateAPIView):
    """ API endpoint for detail view of a PurchaseOrderLineItem object """

    queryset = PurchaseOrderLineItem
    serializer_class = POLineItemSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]


po_api_urls = [
    url(r'^order/(?P<pk>\d+)/?$', PODetail.as_view(), name='api-po-detail'),
    url(r'^order/?$', POList.as_view(), name='api-po-list'),

    url(r'^line/(?P<pk>\d+)/?$', POLineItemDetail.as_view(), name='api-po-line-detail'),
    url(r'^line/?$', POLineItemList.as_view(), name='api-po-line-list'),
]
