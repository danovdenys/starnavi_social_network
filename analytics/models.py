from django.db import models

from analytics.choices import UserActivityChoice

class UserActivity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    activity = models.CharField(max_length=100, choices=UserActivityChoice.choices)
    date = models.DateTimeField(auto_now_add=True)
    
    request_path = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.activity} at {self.date}'
    
    class Meta:
        ordering = ['-date']