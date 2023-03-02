from django.forms import ModelForm, CharField
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['postAuthor', 'postType', 'category', 'head', 'postText', ]

    #def __init__(self, *args, **kwargs):
    #    #user = kwargs.pop('user', '')
    #    super(PostForm, self).__init__(*args, **kwargs)
    #    self.fields['writer'] = ModelChoiceField(queryset=User.objects.all())
    #    self.fields['code'] = ModelChoiceField(queryset=Category.objects.all())
