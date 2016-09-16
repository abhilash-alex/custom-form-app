from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['phone'].error_messages = {
            "required": u"Please tell us your phone number.",
            "invalid": u"The provided phone number appears invalid, please fix it to proceed further.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('phone',)
