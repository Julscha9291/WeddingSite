from django.db import models
from datetime import datetime

class Guest(models.Model):
    name = models.CharField(max_length=80)
    guests = models.IntegerField()
    attendance = models.CharField(max_length=20)
    rsvp_date = models.DateTimeField(default=datetime.utcnow)
    
    def __str__(self):
        return self.name
    
      
    def total_guests(self):
        return self.guests

    def total_attending(self):
        if self.attendance == 'Ich nehme teil':
            return self.guests
        else:
            return 0

    def total_not_attending(self):
        if self.attendance == 'Ich nehme nicht teil':
            return self.guests
        else:
            return 0 
    
class Meta:
    app_label = 'rsvp'
  
