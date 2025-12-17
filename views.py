from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vote_fun(request):
    if request.method == 'POST':
        age = int(request.POST.get('txtage'))
        if age > 18:
            return render(request,'vote.html',{"eligible":"eligible for vote","age":age})
        else:
            return render(request,'vote.html', {"eligible": "not eligible for vote","age":age})
    return render(request, "vote.html")