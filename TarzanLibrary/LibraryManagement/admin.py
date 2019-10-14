from django.contrib import admin
from .models import Book, Author, Member, Borrow


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'ISBN', 'availability', 'number_of_copy', 'in_stock', 'author_name', 'book_price',)
    search_fields = ('book_name', 'ISBN', 'author_name__author_name')
    list_filter = ('availability', 'category')
    ordering = ('book_name',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_ID', 'member_name', 'member_email', 'member_phone_no', 'member_address')
    search_fields = ('member_ID', 'member_name',)
    ordering = ('member_name',)


class BorrowAdmin(admin.ModelAdmin):
    list_display = ('borrowed_member', 'borrowed_book', 'borrow_date', 'return_date', 'expired', 'is_returned')
    list_filter = ('return_date',)
    search_fields = ('borrowed_member__member_name', 'borrowed_member__member_ID')
    ordering = ('return_date',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'about_author')


admin.site.register(Member, MemberAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
