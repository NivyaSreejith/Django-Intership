from django.contrib import admin
from .models import Profile, Movie, Review, Category

# Register your models here.


admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Category)
