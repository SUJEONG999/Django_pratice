from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def exercise1(request):
    template = loader.get_template('exercise1.html')
    name = "진수정"
    context = {'result': name}
    return HttpResponse(template.render(context, request))

def exercise2(request) :
    if request.method == 'POST':
        na = request.POST['name']
        op = request.POST['opinion']
        context = {'na': na, 'op': op}
    else :
         context = None  # 탬플릿에 전달할 게 없으므로 None 전달
    return render(request, 'exercise2.html', context)

def product1(request) :
    template = loader.get_template('product1.html')
    return HttpResponse(template.render(None, request))

def basket1(request):
    query = 'pid' in request.GET
    if query :
        selection = request.GET['pid']
    result = selection.count('p')
    context = {
        'selection' : selection,
        'result': result,
    }
    return render(request, 'basket1.html', context)