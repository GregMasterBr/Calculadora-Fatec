from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    cpf = forms.CharField(
        max_length=11,
        required=True,
        label="CPF"
    )
    avatar = forms.ImageField(
        required=False,
        label="Foto de perfil"
    )

    def save(self, request):
        user = super().save(request)

        user.cpf = self.cleaned_data["cpf"]
        user.avatar = self.cleaned_data.get("avatar")
        user.save()

        return user
