from django.db import models

class empdata(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128,default='')
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_no = models.BigIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models

class Service(models.Model):
    SERVICE_CHOICES = [
        ('PLUMBER', 'Plumber'),
        ('ELECTRICIAN', 'Electrician'),
        ('CARPENTER', 'Carpenter'),
        ('TV TECH', 'TV Technician'),
    ]
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField()
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()}"
