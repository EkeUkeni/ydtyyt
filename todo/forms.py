from django import forms
from todo.models import TodoList

# class TodoForm(forms.Form):
    # title = forms.CharField(max_length=200)
    # description = forms.CharField(widget=forms.Textarea)
    # created_at = forms.DateField(widget=forms.SelectDateWidget)
    # updated_at = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    # complete = forms.BooleanField()
class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['title','description','complete']

