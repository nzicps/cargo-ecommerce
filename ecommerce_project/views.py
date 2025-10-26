from django.shortcuts import render

def home(request):
    apps = [""accounts","cart","catalog","dashboard","orders","payments","shipping""]
    return render(request, 'home.html', {'apps': apps})
