from django.contrib import admin

# Register your models here.
from smpool_app.models import content_service
from smpool_app.models import website_content_info

from smpool_app.models import course_info
from smpool_app.models import class_info
from smpool_app.models import menu_info
from smpool_app.models import course_exam_info

admin.site.register(menu_info)
admin.site.register(content_service)
admin.site.register(website_content_info)

admin.site.register(course_info)
admin.site.register(class_info)
admin.site.register(course_exam_info)

