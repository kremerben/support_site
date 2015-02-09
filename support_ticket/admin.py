from django.contrib import admin

# Register your models here.
from support_ticket.models import Ticket, Update, FileAttachment


class TicketAdmin(admin.ModelAdmin):
    list_display = ('priority', 'status', 'owner','title',)
    list_filter = ('priority', 'status', 'owner','title',)


class UpdateAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'writer', 'message',)
    list_filter = ('ticket', 'writer', 'message',)


class FileAttachmentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'description', 'file',)
    list_filter = ('ticket', 'description', 'file',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(FileAttachment, FileAttachmentAdmin)


