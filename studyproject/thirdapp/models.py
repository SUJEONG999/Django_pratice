from django.db import models

class DBTest(models.Model) :
    name = models.CharField(max_length=10)  # max_length 속성은 필수( 최대 10글자까지 저장 가능)
    age = models.IntegerField(null=True) # 생략가능하다.

    def __str__(self):
        return self.name + ":" + str(self.age)

