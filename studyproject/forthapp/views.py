from django.shortcuts import render, redirect
from forthapp.models import Meeting


def c(request) :
    if request.method == 'POST' :
        name = request.POST.get('name')
        personnel = request.POST.get('personnel')
        title = request.POST.get('title')
        meetingdate = request.POST.get('meetingdate')
        meeting = Meeting(name=name,personnel=int(personnel), title=title, meetingdate=meetingdate)
        meeting.save();
        context = { "msg" : "저장 완료되었어용"  }
    else :
        context = None
    return render(request, 'c.html', context)

def r(request, id=0) : # 기본값 id = 0
    if id == 0 : # 아무것도 안 온경우(R/)
        meetings = Meeting.objects.all() # 전체 리스트를 뽑아옴.
        context = {"meetings": meetings} # 키값으로 담아서 딕셔너리로 만듦.
    else :
        try:
            meeting = Meeting.objects.get(id = id)  # 해당 id만 뽑아오기
            context = {"meeting": meeting}
        except Meeting.DoesNotExist: # id가 존재하지 않을 때
            context = {"msg": str(id) + '번 데이터가 없어용ㅜ'}
    return render(request, 'r.html', context)

def u(request, id) : # 꼭 뭔가 와야하므로, 기본값 없게끔
    if request.method == 'POST' :
        meeting = Meeting.objects.get(id=id)  # 업데이트할 대상 id의 meet 객체를 받아와야함.
        meeting.name = request.POST.get('name')
        meeting.personnel = request.POST.get('personnel')
        meeting.title = request.POST.get('title')
        meeting.meetingdate = request.POST.get('meetingdate')
        meeting.save();
        context = { "msg" : "수정 완료되었어용"  }
    else :
        meeting = Meeting.objects.get(id=id)
        context = {"meeting": meeting}
    return render(request, 'u.html', context)

def d(request, id) :
    try :
        meeting = Meeting.objects.get(id=id)   # 해당 id 만 삭제할 수 있게끔
        meeting.delete()
        context = {"msg": '삭제 되었어용'}
        #return redirect("R1")
    except Meeting.DoesNotExist : # 없는 글을 삭제하려고 할 때
        context = {"msg": str(id)+'번 데이터가 없어서 삭제하지 못했어용'}
    return render(request, 'd.html', context)

