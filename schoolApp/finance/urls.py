from django.urls import path

from finance.views import feeCollection;
from finance.views import feeDuesReport;
from finance.views import feeCollectionReport;


urlpatterns = [

    path('feecoll/', feeCollection),
    path('duesreport/', feeDuesReport),
    path('collectionreport/', feeCollectionReport),



    ]
