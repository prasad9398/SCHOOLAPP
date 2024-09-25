from django.shortcuts import render


# Create your views here.

#function based views
def feeCollection(request):
    return render(request,'finance/fee-collection.html')

def feeDuesReport(request):
    return render(request,'finance/fee-dues-report.html')

def feeCollectionReport(request):
    return render(request,'finance/fee-collection-report.html')
