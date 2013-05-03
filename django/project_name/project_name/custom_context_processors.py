from django.conf import settings

def facebook(request):

    return {
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID,
        'FACEBOOK_API_SECRET': settings.FACEBOOK_API_SECRET,
    }
