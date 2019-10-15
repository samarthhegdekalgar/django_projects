from django.contrib import admin
from .models import Book, Author, Member, Borrow
from django import forms


class AuthorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        author = self.cleaned_data.get('author_name')
        if len(author) < 4:
            raise forms.ValidationError('Please enter a valid name, name cannot be less than 4 Characters',
                                        code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(AuthorAdminForm, self).save(commit=commit)


class BorrowAdminForm(forms.ModelForm):
    def __inti__(self, *args, **kwargs):
        super(BorrowAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        book = self.cleaned_data.get('borrowed_book')
        is_returned = self.cleaned_data.get('book_returned')
        flag = self.cleaned_data.get('returned')
        if book.in_stock <= 0 and not is_returned:
            raise forms.ValidationError(f"{book.book_name} is not available", code="not available")
        return self.cleaned_data

    def save(self, commit=True):
        return super(BorrowAdminForm, self).save(commit=commit)


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
    form = BorrowAdminForm


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'about_author')
    form = AuthorAdminForm


admin.site.register(Member, MemberAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
