from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # clean 함수를 호출하고 리턴하지 않으면 값을 지워버린다. 변할 수 없는 함수명 clean , clean_attribute
    # clean을 쓰면 각 필드에 error를 추가하기 위해 add_error를 추가해준다.
    # cleaned_data로 확인할 수 있다.
    # 여기서 리턴해주는 것을 views.py 에서 cleaned_data로 출력 가능

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Incorrect Password"))
                # password 칸에 에러를 띄우기 위해 그냥 위에 띄우려면 raise error
        except models.User.DoesNotExist:
            self.add_error("password", forms.ValidationError("User not exist"))
        # this error describe on browser


class SignupForm(forms.ModelForm):
    """Signup Form"""

    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "email"]

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return password
        else:
            print(password, confirm_password)
            self.add_error(
                "confirm_password", forms.ValidationError("Password not Same")
            )

    def save(self, *args, **kwargs):
        # save 오버라이드, Username하고 위에서 필드에 넣지않은 password 저장 시켜주기 위해
        user = super().save(commit=False)  # objects 생성만 하고 데이터베이스에는 저장 No
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user.username = email
        user.set_password(password)
        user.save()  # commit=True

