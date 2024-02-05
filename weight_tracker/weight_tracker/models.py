from django.db import models

class WeightEntry(models.Model):
    username = models.CharField(max_length=50)
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.username} - {self.date}"
