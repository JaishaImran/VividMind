from django.db import models
 
class UppercaseBooleanField(models.BooleanField):
    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            value_lower = value.lower()
            if value_lower == 'true':
                return True
            elif value_lower == 'false':
                return False
        return bool(value)
    

class CentralRequest(models.Model):
    request_id = models.UUIDField(primary_key=True, unique=True, editable=False)
    request_type = models.CharField(max_length=255)
    endpoint = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('passed', 'Passed'),
        ('awaiting', 'Awaiting'),
        ('retry', 'Retry'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='awaiting')
    payload = models.JSONField()
