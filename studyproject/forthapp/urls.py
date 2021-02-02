from django.urls import path
from . import views

urlpatterns = [
    path('C/', views.c, name='C'),
    path('R/', views.r, name='R1'),  # R/ 만 오면 전체 리스트를 가져 오겠다.
    path('R/<int:id>/', views.r, name='R2'),  # 특정 id 글만 가져오는 요청
    path('U/<int:id>/', views.u, name='U'), # 특정글 하나를 읽고 업데이트(수정)
    path('D/<int:id>/', views.d, name='D'), # 특정글 하나를 읽고 삭제
]