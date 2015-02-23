from django.contrib import admin

# Register your models here.
from support_ticket.models import Ticket, Comment, FileAttachment


class TicketAdmin(admin.ModelAdmin):
    list_display = ('priority', 'status', 'owner', 'title',)
    list_filter = ('priority', 'status', 'owner', 'title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'message',)
    list_filter = ('ticket', 'user', 'message',)


class FileAttachmentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'description', 'file',)
    list_filter = ('ticket', 'description', 'file',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(FileAttachment, FileAttachmentAdmin)


