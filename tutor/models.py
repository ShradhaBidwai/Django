from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    publish_date = models.DateField()



    def __str__(self):
        return self.title

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTA0NTE3OCwiaWF0IjoxNzQ0OTU4Nzc4LCJqdGkiOiIyNTdkOGZlMTU5NGI0YWViYThmN2MwN2JlNGQxOTkzZSIsInVzZXJfaWQiOjJ9.Q6_hbw_-0VB1IQM97rI4ZDttJM3ufmeaJqSdMGBWR6w",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0OTU5MDc4LCJpYXQiOjE3NDQ5NTg3NzgsImp0aSI6ImRkOTJmZDljZGZkMTRmN2JiNGYyYTVhNTFiZDc2MWZhIiwidXNlcl9pZCI6Mn0.BksApZSYg7_1d_BqcW_mVaYoXN2VGwQi4UFd51WHS3A"
# }