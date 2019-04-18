from django.db import models

# Create your models here.
# N:M
# 병원에 오는 사람들을 기록하는 시스템
# 필수적인 모델은 환자와 의사
# 어떠한 관계로 표현할 수 있을까?

class Doctor(models.Model):
    name=models.TextField()
    
    
class Patient(models.Model):
    name=models.TextField()
    doctors=models.ManyToManyField(Doctor,related_name='patients')
    

# doctor1.patients.remove(patient2)
# doctor1.patients.add(patient2)
# doctor1 이랑 patient2랑 위치 바꿔도 됨


    

    
# Doctor:Reservation =1:N
# Patient:Reservation =1:N
# Doctor:Patient=M:N
# 추가적인 정보가 더 필요할때에는 중간 table을 만들어서 M:N 을 만드는것이 더 좋음
# class Reservation(models.Model):
#     doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient=models.ForeignKey(Patient, on_delete=models.CASCADE)


    
    
