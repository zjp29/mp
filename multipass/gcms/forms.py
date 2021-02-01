from .models import Dataset, URLs
from django import forms

# class ZipFileField(forms.FileField):
#     def validate(self, value):
#         # First run the parent class' validation routine
#         super().validate(value)
#         # Run our own file extension check
#         file_extension = os.path.splitext(value.name)[1]
#         if file_extension != '.zip':
#             raise ValidationError(
#                  ('Invalid file extension'),
#                  code='invalid'
#             )

class DatasetForm(forms.modelform):
    class meta:
        model = Dataset
        fields = [
            'title',
            'renewal',
            'summary',
            'detail',
            'tags',
            'f'
        ]

