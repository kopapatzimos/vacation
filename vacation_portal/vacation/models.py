from django.db import models
from django.contrib.auth.models import User

class VacationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_requests')

    def __str__(self):
        return f"{self.user.username}'s vacation request from {self.start_date} to {self.end_date}"
