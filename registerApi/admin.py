from django.contrib import admin
from .models import Member, Batch, Payment
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=['FullName','Email','Batch','Gender','MobileNo','Age']

class BatchAdmin(admin.ModelAdmin):
    list_display=['MemberId','BatchTiming']
class PaymentAdmin(admin.ModelAdmin):
    list_display=['PaymentId','PaymentDate','PaymentMethod','Status']
admin.site.register(Member,MemberAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Payment,PaymentAdmin)

