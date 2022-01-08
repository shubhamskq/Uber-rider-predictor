from django.shortcuts import render,redirect
import pickle
import os
from . models import Prediction     #prediction is class of models.py


# Create your views here
def index (request):           #index is view here
    res=Prediction.objects.all()
    return render(request,"index.html",{'res':res})   #index.html is template
def test(request):             #test is view here
    ppw=int(request.POST['ppw'])
    pn = int(request.POST['pn'])
    mi = int(request.POST['mi'])
    appw = int(request.POST['appw'])
    modulepath=os.path.dirname(__file__)   #isse root directory mil jayegi
    model=pickle.load(open(os.path.join(modulepath,'taxi.pkl'),'rb'))
    res=str(model.predict([[ppw,pn,mi,appw]]).round(2))
    pre=Prediction(ppw=str(ppw),pn=str(pn),mi=str(mi),appm=str(appw),result=res)      #ORM=object relationship model
    pre.save()
    return redirect('index')      #redirected to index template(index.html)
