from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Qrcode


# Create your views here.
class QrcodeList(ListView):
    model = Qrcode
    queryset = Qrcode.objects.all()


class QrcodeCreate(CreateView):
    model = Qrcode
    fields = '__all__'

    success_url = reverse_lazy('generator:list')


class QrcodeUpdate(UpdateView):
    model = Qrcode
    fields = '__all__'

    success_url = reverse_lazy('generator:list')
