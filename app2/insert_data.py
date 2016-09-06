from . import models as models2
from . import forms
from .signals import preparing_b
from app1 import models as models1

def main():
    dict_b_origen = models1.B.objects.values('id', 'nombre', 'a').first()
    preparing_b.send(object_dict=dict_b_origen, sender='main')
    b_objects = models2.B.objects.filter(id=dict_b_origen.get('id'))
    if not b_objects:
        form = forms.BForm(dict_b_origen)
        if form.is_valid():
            models2.B.objects.get_or_create(**dict_b_origen)

if __name__ == '__main__':
    main()
