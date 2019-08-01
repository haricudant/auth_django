from django.contrib import admin

from interface_app.models import Book, Genre,BookInstance,Author



admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Author)


# Define the admin class


# Register the admin class with the associated model
# admin.site.register(Author, )



# # Register the Admin classes for BookInstance using the decorator
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
# # Register the admin class with the associated model
#
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#
#
# def display_genre(self):
#     """Create a string for the Genre. This is required to display genre in Admin."""
#     return ', '.join(genre.name for genre in self.genre.all()[:3])
#
#
# display_genre.short_description = 'Genre'
#
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#
# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#         list_filter = ('status', 'due_back')
#
#         fieldsets = (
#             (None, {
#                 'fields': ('book', 'imprint', 'id')
#             }),
#             ('Availability', {
#                 'fields': ('status', 'due_back')
#             }),
#         )
#
#
# # admin.site.register(Choice)
#
# # Register your models here.class AuthorAdmin(admin.ModelAdmin):
# #     pass
# #
# # # Register the admin class with the associated model
# # admin.site.register(Author, AuthorAdmin)
