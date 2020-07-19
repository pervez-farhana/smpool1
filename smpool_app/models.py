from django.db import models
from django.contrib.auth.models import User



 #widget = forms.Textinput(attrs={"class" : "form-control",
        #                                                             "placeholder": "contenttext"
        #                                                            }
        #                                                    )
        #                            )
# Create your models here.
class content_service(models.Model):

    manage= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    service_desc = models.CharField(max_length=500)
    service_cost = models.FloatField()

    def __str__(self):
        return self.service_desc + ":" + str(self.service_cost)


class menu_info(models.Model):

    menu_code = models.CharField(max_length=500)
    menu_name  = models.CharField(max_length=5000)
    submenu_name  = models.CharField(max_length=5000) 
    menu_srl = models.CharField(max_length=500)
    menu_desc = models.CharField(max_length=500)
    menu_ph = models.CharField(max_length=500)

    def __str__(self):
        return self.menu_name + ":" + self.menu_desc



class website_content_info(models.Model):

    body_code = models.CharField(max_length=500)
    body_title = models.CharField(max_length=500)
    body_subtitle = models.CharField(max_length=500)  
    body_text = models.CharField(max_length=5000)    
    body_type = models.CharField(max_length=500) 
    body_pos  = models.CharField(max_length=500)
    body_page = models.CharField(max_length=500)
    body_pic_path = models.CharField(max_length=500)
    body_area = models.TextField()
    menuid = models.ForeignKey(menu_info, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.body_code + ":" + self.body_title


class course_info(models.Model):

    course_code = models.CharField(max_length=500)
    course_name = models.CharField(max_length=500)
    course_title = models.CharField(max_length=500)  
    module_name = models.CharField(max_length=500)    
    course_duration = models.CharField(max_length=500) 
    course_fees  = models.CharField(max_length=500)
    exam_code = models.CharField(max_length=500)
    exam_fees = models.CharField(max_length=500)
    course_comments = models.CharField(max_length=500)
    course_ph = models.CharField(max_length=500)
    bodyid = models.ForeignKey(website_content_info, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.course_name + ":" + self.course_title

class class_info(models.Model):

    class_code = models.CharField(max_length=500)
    class_title = models.CharField(max_length=500)
    class_subtitle = models.CharField(max_length=500)  
    class_text = models.CharField(max_length=500)    
    class_type = models.CharField(max_length=500) 
    batch_no  = models.IntegerField()
    class_start_date = models.CharField(max_length=500)
    class_day = models.CharField(max_length=500)
    class_time = models.CharField(max_length=500)
    class_ph = models.CharField(max_length=500)
    bodyid = models.ForeignKey(website_content_info, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.class_title + ":" + self.class_start_date

class course_exam_info(models.Model):
    exam_code = models.CharField(max_length=500)
    exam_name = models.CharField(max_length=500)
    exam_fees = models.CharField(max_length=500)
    exam_text = models.CharField(max_length=500)
    exam_type = models.CharField(max_length=500)
    exam_ph = models.CharField(max_length=500)
    bodyid = models.ForeignKey(website_content_info, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.exam_name + ":" + self.exam_text