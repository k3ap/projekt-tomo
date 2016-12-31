from django.shortcuts import render

def main_view(request):
    return render(request, 'tomo_statistics/statistika_test.html')
