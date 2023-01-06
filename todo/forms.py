from django.forms import ModelForm
from todo.models import Category, Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["title", "description"]

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "category"]
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'todo:create'
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'form-label create-label'
        self.helper.field_class = 'form-control mb-3'
        self.helper.layout = Layout(
            Field("title"),
            Field("description"),
            Field("priority"),
            Field("category"),
            HTML("<br>"),
            Submit('submit', 'Save'),      
            )
