from django.forms import ModelForm

from measurement.models import Measurement


class AddMeasurementForm(ModelForm):
    """Форма для добавления измерений"""
    class Meta:
        model = Measurement     # модель, к которой привязывается форма
        fields = ['weight', 'hip_girth', 'biceps_girth']  # поля, которые отображать на форме
        labels = {
            'weight': 'Вес',
            'hip_girth': 'Охват бедер',
            'biceps_girth': "Обхват бицепса"
        }

    def __init__(self, *args, **kwargs):
        super(AddMeasurementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
