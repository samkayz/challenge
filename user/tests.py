from django.test import TestCase
from django.utils import timezone
from .models import *
from datetime import datetime

# base_date_time = datetime.now()
# now = (datetime.strftime(base_date_time, "%Y-%m-%d %H:%M %p"))


"""Test Case for the Models"""
class UserManagementTest(TestCase):

    def create_Record(self, firstname="Samson", 
                      lastname="Ilemobayo", 
                      phone="08069475532", 
                      email="ilemobayosamson@gmail.com", 
                      dob="1998-04-17", gender="male",
                      nationality="Nigeria"):
        return UserManagement.objects.create(firstname=firstname, 
                                             lastname=lastname, 
                                             phone=phone, 
                                             email=email, 
                                             dob=dob, 
                                             nationality=nationality)

    def test_record_creation(self):
        w = self.create_Record()
        self.assertTrue(isinstance(w, UserManagement))
        self.assertEqual(w.__unicode__(), w.firstname)
        
        
        
        