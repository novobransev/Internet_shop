from django.urls import path

from .views import ElectricalEngineeringView, ElectricalEngineeringDetailView

urlpatterns = [
    path('electrical_product/', ElectricalEngineeringView.as_view(), name='electrical_product'),
    path('detail_product/<int:pk>/', ElectricalEngineeringDetailView.as_view(), name='detail_product'),
]
