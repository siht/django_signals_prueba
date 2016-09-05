from django import dispatch
from django.dispatch import receiver
from .models import A, B
from .forms import AForm, BForm

preparing_b = dispatch.Signal(providing_args=['object_dict'])
preparing_a = dispatch.Signal(providing_args=['object_dict'])

@receiver(preparing_b)
def insert_b_object(sender, object_dict):
    pass
