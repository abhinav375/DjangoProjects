from django.shortcuts import render

# Create your views here.
'''COOKIES CODE'''
def index(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'testcookies/index.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response
    
'''SESSSION CODE'''      
'''def index(request):
    if 'count' in request.session:
        newcount=int(request.session['count'])+1
    else:
        newcount=1
    
    request.session['count']=newcount
    return render(request,'testcookies/index.html',{'count':newcount})'''
    