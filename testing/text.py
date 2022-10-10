from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/')

class Firereport(models.Model):
    FullName = models.CharField(max_length=250, null=True)
    MobileNumber = models.CharField(max_length=12, null=True)
    Location = models.CharField(max_length=200, null=True)
    Message = models.CharField(max_length=200, null=True)
    AssignTo = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
    Status = models.CharField(max_length=150, null=True)
    Postingdate = models.DateTimeField(auto_now_add=True)
    AssignedTime = models.CharField(max_length=150, null=True)
    UpdationDate = models.DateTimeField(null=True)