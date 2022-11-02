from django.contrib import admin
from basic_app.models import UserProfileInfo,Result_Men,Result_Women,Medals,Room,Booking
from django.contrib.auth.models import User
# Register your models here.

class mymodel(admin.ModelAdmin):
    fields = ['user','country','sport','portofolio_site','profile_pic']
    search_fields = ['user__username']
    list_filter = ['country']
    list_display = ['user','country','sport','portofolio_site','profile_pic']
    list_editable = ['country','sport']
class mymodel1(admin.ModelAdmin):
    list_display = ['sport','gold_medal','silver_medal','bronze_medal']
    list_editable = ['gold_medal','silver_medal','bronze_medal']
    # i = 'gold_medal'+'silver_medal'+'bronze_medal'
class mymodel2(admin.ModelAdmin):
    model=Medals
    list_display = ['country','gold_medal','silver_medal','bronze_medal','total_medals']
    list_editable = ['gold_medal','silver_medal','bronze_medal','total_medals']
    #prepopulated_fields = {'total_medals':sum(['gold_medal','silver_medal','bronze_medal'])}
admin.site.register(UserProfileInfo,mymodel)
admin.site.register(Result_Men,mymodel1)
admin.site.register(Result_Women,mymodel1)
admin.site.register(Medals,mymodel2)
admin.site.register(Room)
admin.site.register(Booking)
