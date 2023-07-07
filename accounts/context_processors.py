from .models import CustomUser


def user_image(request):
    if request.user.is_authenticated:
        user = request.user
        return {'image': user.image.url if user.image else ''}
    return {'image': ''}

