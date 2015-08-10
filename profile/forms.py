from django import forms
from django.contrib.auth import get_user_model

from profile.models import Character


class UserModelForm(forms.ModelForm):

    main_character = forms.ModelChoiceField(
            queryset=Character.objects.filter(main_user=None),
            required=False)

    characters = forms.ModelMultipleChoiceField(
            queryset=Character.objects.filter(owner=None),
            required=False)

    def save(self, commit=True):
        return super(UserModelForm, self).save(commit=commit)
        print '\nSAVING CUSTOM FORM\n'
        import ipdb; ipdb.set_trace()
        print self.cleaned_data
        # TODO: save character data to user.characters

        characters = self.cleaned_data.get('characters', None)
        main_character = self.cleaned_data.get('main_character', None)

    class Meta:
        model = get_user_model()
        fields = '__all__'
