from django import forms
from django.contrib.auth.models import User
from apps.comments.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment', 'review')
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder': 'Write your comment'},),
            'review': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = True
        self.fields['review'].required = True

    def save(self, commit=True):
        review = super(CommentForm, self).save(commit=False)
        # review.user = self.user
        review.user = User.objects.get(pk=1)
        if commit:
            review.save()
        return review


