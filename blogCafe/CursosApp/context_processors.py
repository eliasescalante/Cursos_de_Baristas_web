from django.contrib.auth.context_processors import auth
from User.models import Imagen

def custom_user(request):
    context = auth(request)
    user = context['user']
    
    if user.is_authenticated:
        imagen = Imagen.objects.filter(user=request.user.id)
        if len(imagen) > 0:
            context['user_avatar'] = imagen[0]
        else:
            context['user_avatar'] = ""
    return context