from django.forms import ModelForm
from todo.models import Category, PlanningUser, Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit, Row, Column
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



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
        
class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'form-label create-label'
        self.helper.field_class = 'form-control mb-3'
        self.helper.layout = Layout(
            Field("username"),
            Field("email"),
            Field("password1"),
            Field("password2"),
            HTML("<br>"),
            Submit('submit', 'Save'),      
            )
        
        
class UserSignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(UserSignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'form-label create-label'
        self.helper.field_class = 'form-control mb-3'
        self.helper.layout = Layout(
            Field("username"),
            Field("password"),
            HTML("<br>"),
            Submit('submit', 'Login'),      
            )
