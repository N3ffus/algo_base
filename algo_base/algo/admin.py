from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AlgoTheme)
admin.site.register(DataStructureTheme)
admin.site.register(Algorithm)
admin.site.register(DataStructure)
admin.site.register(ProblemSite)
admin.site.register(Problem)
admin.site.register(Article)
admin.site.register(Video)
admin.site.register(Profile)