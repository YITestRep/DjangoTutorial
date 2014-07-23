#coding:utf-8

from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_today(self):
        import datetime
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice


#adminページヘの登録
from django.contrib import admin
#admin.site.register(Poll)#自動で生成したUI

'''
# Fieldの表示順の変更
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
'''

'''
#段落わけ的なことをする
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
'''

'''
#collapseオプションの追加
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
admin.site.register(Poll, PollAdmin)

#Choiceオブジェクトの作成
admin.site.register(Choice)
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
admin.site.register(Poll, PollAdmin)

