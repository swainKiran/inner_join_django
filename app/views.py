from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
def innerEquijoins(request):
    JDED = Emp.objects.select_related('deptid').all()
    JDED = Emp.objects.select_related('deptid').filter(job='developer')
    JDED = Emp.objects.select_related('deptid').filter(emp_name='kiran')
    JDED = Emp.objects.select_related('deptid').filter(deptid='101')
    JDED = Emp.objects.select_related('deptid').filter(deptid__deptloc='odisha')
    d={'JDED':JDED}
    return render(request,'innerEquijoin.html',d)


def selfJoin(request):
    JDSD=Emp.objects.select_related('mgr').all()
    JDSD=Emp.objects.select_related('mgr').filter(emp_name='kiran')
    JDSD=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    JDSD=Emp.objects.select_related('mgr').filter(Q(mgr__emp_name='kiran')|Q(mgr__emp_sal__gt=1000),emp_id=1111)

    s={'JDSD':JDSD}
    return render(request,'selfJoin.html',s)


def empdeptsal(request):
    EMSD=Emp.objects.select_related('mgr','deptid').all()
    EMSD=Emp.objects.select_related('mgr','deptid').filter(mgr__emp_name='kiran',deptid=100)
    EMSD=Emp.objects.select_related('mgr','deptid').filter(deptid__deptname__endswith='a',deptid=102)
    EMSD=Emp.objects.values('mgr','deptid').filter(emp_sal__gt=Sal_grade.objects.values('lowsal').filter(grade=1),emp_sal__lt=Sal_grade.objects.values('highsal').filter(grade=1))
    EMSD=Emp.objects.values('emp_name').filter(emp_sal__gt=20)

    #using extra method 

    EMSD=Emp.objects.extra(where=["LENGTH(emp_name) = 5"])
    EMSD=Emp.objects.extra(where=[" emp_name LIKE '%a_' "])
    EMSD=Emp.objects.extra(where=[" emp_name LIKE '%a_'and emp_name LIKE 'k%' "])
    EMSD=Emp.objects.extra(where=["LENGTH(emp_name) = 5 or LENGTH(emp_name) = 6" ])

    

    k={'EMSD':EMSD}
    return render(request,'3table.html',k)

def updateMethod(request):

    #Emp.objects.filter(emp_name='kanha').update(emp_name='kanhu')
    #Emp.objects.filter(emp_name='kanhu').update(job='engineer')
    #Emp.objects.filter(emp_name='kanhu').update(deptid=500)#error bcz deptid not present
    #Emp.objects.filter(emp_name='kanhu').update(deptid=100)
    #Emp.objects.filter(emp_name='kanhu').update(job='cook',coomition=1000)


    #update_or_create method
    #Emp.objects.update_or_create(emp_name='kanhu',defaults={'job':'nothing'})
    #Emp.objects.update_or_create(emp_name='rama',defaults={'job':'nothing'}) #error u have to give all data in defult
    MO=Emp.objects.get(emp_id=1111)
    DO=Dept.objects.get(deptid=100)

    Emp.objects.update_or_create(emp_name='rama',defaults={'emp_id':9090 ,'emp_name':'rama','emp_sal':6700,'job':'teacher','hire_date':'2000-12-23','mgr':MO,'coomition':200 ,'deptid':DO})

    
    EMPO=Emp.objects.all()
    j={'EMPO':EMPO}
    return render(request,'update.html',j)


def deleteMethod(request):
    #Emp.objects.filter(emp_name='kanhu').delete()
    #Emp.objects.filter(emp_name='kiran').delete()
    Emp.objects.filter(deptid=100).delete()
     

    EMDO=Emp.objects.all()
    j={'EMDO':EMDO}
    return render(request,'delete.html',j)