from django.contrib import admin
from datetime import timedelta
from .models import TopicTag, Skill, Profile


class AdminTopicTag(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-empty field-'


class AdminSkillTag(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-empty field-'


class AdminUserProfile(admin.ModelAdmin):
    list_display = ('username','email','get_utc',)
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-empty field-'

    def get_utc(self, obj):
        return obj.user.date_joined + timedelta(minutes=330)

    get_utc.short_description = 'Created (UTC)'


admin.site.register(TopicTag, AdminTopicTag)
admin.site.register(Skill, AdminSkillTag)
admin.site.register(Profile, AdminUserProfile)