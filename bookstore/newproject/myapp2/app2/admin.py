from django.contrib import admin
from .models import book
# Register your models here.

# CHANGE COURSE ADMIN PANEL
admin.site.site_header='BOOKS ADMIN PANEL'

# CHANGE TITLE
admin.site.site_title='BOOKSTORE'

# REGISTER MODEL
admin.site.register(book)

     