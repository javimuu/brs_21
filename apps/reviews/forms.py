from django import forms
from django.contrib.auth.models import User
from apps.reviews.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'review', 'book')
        widgets = {
            'review': forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder': 'Write your review'},),
            'rating': forms.HiddenInput(),
            'book': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].required = True
        self.fields['rating'].error_messages['required'] = 'You must select the suitable rating '
        self.fields['review'].required = True
        self.fields['book'].required = True

    def save(self, commit=True):
        review = super(ReviewForm, self).save(commit=False)
        # review.user = self.user
        review.user = User.objects.get(pk=1)
        if commit:
            review.save()
        return review

