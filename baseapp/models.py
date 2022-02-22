from django.db import models

class BaseTable:
    #id, name, gender, parent_id, is_alive, created_at, updated_at
    GENDER_CHOICE = [
        ('M', 'Male'), 
        ('F',  'Female')
    ]
    name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False, choices=GENDER_CHOICE)
    parent = models.ForeignKey('self', null=True, blank=True, db_column='parent_id', on_delete=models.SET_NULL)
    is_alive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)