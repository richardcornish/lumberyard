from django.contrib.auth.validators import ASCIIUsernameValidator


class ASCIIUsernameValidator(ASCIIUsernameValidator):
    regex = r'^[\w-]+\Z'
    message = 'Enter a valid username of letters, numbers, <code>-</code>, or <code>_</code>.'
