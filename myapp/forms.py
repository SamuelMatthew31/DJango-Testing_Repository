from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition',
            'placeholder': 'Your name',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition',
            'placeholder': 'you@example.com',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 '
                     'focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition resize-none',
            'placeholder': 'Write your message...',
            'rows': 4,
        })
    )
