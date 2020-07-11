from django.http import HttpResponse
class MiddlewareDemo(object):
    def __init__(self,get_response):
        
        self.get_response=get_response
    
    def __call__(self,request):
        print("Middleware got the request now it will transfer to view the same request")
        response=self.get_response(request)
        print("After view Middleware it will exec")
        return response
       
    '''def __call__(self,request):
        return HttpResponse("<h1> Server is under maintainence</h1>")'''
    
    ###def process_exception(self,request,exception):
        ###return HttpResponse('<h1>Currently we are facing some technical problems plz try after some time!!!</h1>')
    
    def process_exception(self,request,exception):
        s1=('<h1>Currently we are facing some technical problems plz try after some time!!!</h1><br>')
        s2=('<h2>Raised Exception is::{}</h2><br>'.format(exception.__class__.__name__))
        s3=('<h2>Exception Message is::{}</h2><br>'.format(exception))
        return HttpResponse([s1,s2,s3])
        #return HttpResponse('<h1>Currently we are facing some technical problems plz try after some time!!!</h1><h2>Raised Exception:{}</h2><h2>Exception Message:{}</h2>'.format(exception.__class__.__name__,exception))

           
class MiddlewareDemo1(object):
    def __init__(self,get_response):
        
        self.get_response=get_response
    
    def __call__(self,request):
        print("Middleware 1 got the request now it will transfer to view the same request")
        response=self.get_response(request)
        print("After view  Middleware 1 will exec")
        return response
       
    '''def __call__(self,request):
        return HttpResponse("<h1> Server is under maintainence</h1>")'''
    
    ###def process_exception(self,request,exception):
        ###return HttpResponse('<h1>Currently we are facing some technical problems plz try after some time!!!</h1>')
    
    def process_exception(self,request,exception):
        s1=('<h1>Currently we are facing some technical problems plz try after some time!!!</h1><br>')
        s2=('<h2>Raised Exception is::{}</h2><br>'.format(exception.__class__.__name__))
        s3=('<h2>Exception Message is::{}</h2><br>'.format(exception))
        return HttpResponse([s1,s2,s3])
