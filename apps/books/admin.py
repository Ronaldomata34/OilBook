from django.contrib import admin
from django.utils.html import format_html

from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ('capitalize_title', 'author', 'subject', 'link_to_url')

	def capitalize_title(self, obj):
		return "{}".format(obj.title.upper())
	capitalize_title.short_description = 'Title'

	def link_to_url(self, obj):
		return format_html(
			'<a href="{url}">{url}</a>'.format(url=obj.url))
	link_to_url.short_description = 'Url'


admin.site.register(Book, BookAdmin)

# Public key ----> GA7MCRRYE4RYB5RJVHILCR7YS7ICLMA2VWCTONEBHRRLWNUGNCWVI4LO
# Secret key ----> SAPOCXH5MXEGYZCBWL26LJSDJOCBSEGPESYUAGCDNZTZTQ4KOJVIXTUJ
# Stellar public key ---> SAPOCXH5MXEGYZCBWL26LJSDJOCBSEGPESYUAGCDNZTZTQ4KOJVIXTUJ