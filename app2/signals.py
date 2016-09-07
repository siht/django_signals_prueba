from django import dispatch
from django.dispatch import receiver
from .models import A, B
from app1 import models as app1_models
from .forms import AForm

preparing_b = dispatch.Signal(providing_args=['object_dict'])
preparing_a = dispatch.Signal(providing_args=['object_dict'])

@receiver(preparing_b)
def insert_b_object(sender, object_dict, **kwargs):
    print '<<<<<<<<<<<<<<'
    b_objects = B.objects.filter(id=object_dict.get('id'))
    print b_objects
    if not b_objects.count():
        a_objects = A.objects.filter(id=object_dict.get('a'))
        if not a_objects.count():
            preparing_a.send(object_dict={'id': object_dict.get('a')}, sender='insert_b_object')

@receiver(preparing_a)
def insert_a_object(sender, object_dict, **kwargs):
    a = app1_models.A.objects.filter(**object_dict).values('id', 'nombre')[0]
    form = AForm(a)
    if form.is_valid():
        A.objects.get_or_create(**form.cleaned_data)
