from django.contrib import admin
from .models import Hotel, Room, Guest, Record, Manager, Category
from django import forms
from datetime import date


class FormRecordAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormRecordAdmin, self).__init__(*args, **kwargs)
        if not self.instance.id:
            self.fields['completed'].disabled = True
            self.fields['is_canceled'].disabled = True
            self.fields['modified'].disabled = True
        if self.instance.id:
            self.fields['room_no'].disabled = True
            self.fields['guest'].disabled = True
            self.fields['checkin_date'].disabled = True
            self.fields['people_count'].disabled = True
        if self.instance.completed or self.instance.is_canceled:
            self.fields['completed'].disabled = True
            self.fields['is_canceled'].disabled = True
            self.fields['modified'].disabled = True

    def clean(self):
        p_total = self.cleaned_data.get('people_count')
        ci_date = self.cleaned_data.get('checkin_date')
        co_date = self.cleaned_data.get('checkout_date')
        t_completed = self.cleaned_data.get('completed')
        is_canceled = self.cleaned_data.get('is_canceled')
        room_number = self.cleaned_data.get('room_no')
        modified = self.cleaned_data.get('modified')
        guest_name = self.cleaned_data.get('guest')

        if co_date < ci_date:
            raise forms.ValidationError(f'Please select the valid dates', code='invalid dates')


        if p_total > 3:
            raise forms.ValidationError(f"Sorry! up to three members can accommodate", code='count exceeded')
        if date.today() == ci_date and is_canceled:
            raise forms.ValidationError(f'You cannot cancel the booking, booking status is confirmed',
                                        code='cannot cancel')
        record_obj = Record.objects.filter(completed=False).filter(is_canceled=False)
        for obj in record_obj:
            value = obj
            if str(value.room_no) == str(room_number.number) and not t_completed and not is_canceled and not modified\
                    and value.checkout_date > ci_date and not co_date < value.checkin_date:
                raise forms.ValidationError(f'Someone already booked this room', code='guest exist')
            if str(value.guest) == str(guest_name.name) and not t_completed and not is_canceled and not modified:
                raise forms.ValidationError(f'One user can book one room at a time', code='user active')
        if t_completed and is_canceled and not modified:
            raise forms.ValidationError(f'Please select either cancel or complete', code='selection error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(FormRecordAdmin, self).save(commit=commit)


class FormGuestAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormGuestAdmin, self).__init__(*args, **kwargs)

    def clean(self):
        phone_no = self.cleaned_data.get('phone_no')
        adhar_number = self.cleaned_data.get('adhar_number')

        if len(phone_no) < 10:
            raise forms.ValidationError(f'Enter the valid phone number', code='invalid phone number')

        if len(adhar_number) < 12:
            raise forms.ValidationError(f'Enter the valid Adhar number', code='invalid Adhar number')

        return self.cleaned_data

    def save(self, commit=True):
        return super(FormGuestAdmin, self).save(commit=commit)


class FormManagerAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormManagerAdmin, self).__init__(*args, **kwargs)

    def clean(self):
        phone_no = self.cleaned_data.get('phone_number')

        if len(phone_no) < 10:
            raise forms.ValidationError(f'Enter the valid phone number', code='invalid phone number')
        return self.cleaned_data

    def save(self, commit=True):
        return super(FormManagerAdmin, self).save(commit=commit)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_no', 'guest', 'people_count', 'checkin_date', 'checkout_date', 'completed',
                    'is_canceled', 'calculate_price')
    form = FormRecordAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type', 'price',)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'adhar_number')
    form = FormGuestAdmin


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    form = FormManagerAdmin


class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_type')


admin.site.register(Hotel)
admin.site.register(Room, RoomAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Category, CategoryAdmin)
