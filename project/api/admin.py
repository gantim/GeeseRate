from django.contrib import admin
from .models import Review, Course, Institute, User

admin.site.register(Review)
admin.site.register(Course)
admin.site.register(Institute)
admin.site.register(User)
