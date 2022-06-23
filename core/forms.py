from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
  # image = forms.ImageField(
  #   widget=forms.ClearableFileInput(
  #     attrs={'class': 'file-image'}
  #     # attrs={'style':'display: none;','class':'form-control', 'required': False, }
  #   )
  # )

  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   self.helper = FormHelper()
  #   self.helper.layout = Layout(
  #     # Div(
  #     #   Div('image', css_class='form-grouppp'),
  #     #   css_class='form-rowww'
  #     # )
  #     Div(
  #       HTML("""
  #       <div class="fileupload fileupload-new" data-provides="fileupload">
  #         <div class="fileupload-new thumbnail" style="width: 200px; height: 150px;">
  #           <img src="http://www.placehold.it/200x150/EFEFEF/AAAAAA&text=no+image" />
  #         </div>
  #         <div class="fileupload-preview fileupload-exists thumbnail" style="max-width: 200px; max-height: 150px; line-height: 20px;">
  #         </div>
  #         <div class"smalltest">
  #         <span class="btn btn-file">
  #           <span class="fileupload-new">Select image</span>
  #         <span class="fileupload-exists">Change</span>
  #       """),
  #       Field('image'),
  #       HTML("""</span><a href="#" class="btn fileupload-exists" data-dismiss="fileupload">Remove</a></div></div>"""),
  #       css_class = 'photofield'
  #     ),
  #   )
  class Meta: 
    model = Movie 
    fields = ('file', 'image')
