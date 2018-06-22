from django.conf.urls import url, include
from categories.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(CategoriesEdit.as_view()) , name="categories_edit")
]