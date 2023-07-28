from django.contrib import admin
from chatAgent.models import ClientUser, Conversation, Message

class MessageInline(admin.TabularInline):
    model = Message
    readonly_fields = ('sender', 'text', 'timestamp')

class ConversationAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline,
    ]
    list_display = ('id', 'clientUser', 'status')

admin.site.register(ClientUser)
admin.site.register(Conversation, ConversationAdmin)
