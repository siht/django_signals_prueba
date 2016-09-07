import logging
from . import models as models2
from . import forms
from .signals import preparing_b
from app1 import models as models1

logger = logging.getLogger(__name__)


def main():
    print('inicio de programa')
    dict_b_origen = models1.B.objects.values('id', 'nombre', 'a').filter(id=1).first()
    print '==================='
    print(dict_b_origen)
    preparing_b.send(object_dict=dict_b_origen, sender='main')
    b_objects = models2.B.objects.filter(id=dict_b_origen.get('id'))
    if not b_objects:
        form = forms.BForm(dict_b_origen)
        if form.is_valid():
            models2.B.objects.get_or_create(**form.cleaned_data)

if __name__ == '__main__':
    main()
