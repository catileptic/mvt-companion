from django.urls import path

from . import views

app_name = "analyzer"
urlpatterns = [
    path("", views.index, name="index"),
    path("load_scan_results", views.load_scan_results, name="load_scan_results"),
    # shouldn't it be <str:name>/result?
    path("<str:name>/results", views.scan_result, name="scan_result_detail"),
    # shouldn't it be <str:name>/delete?
    path("<str:name>/delete", views.delete_scan_result, name="delete_scan_result"),
]
