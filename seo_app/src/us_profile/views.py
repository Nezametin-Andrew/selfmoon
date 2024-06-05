import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Profile
from .forms import ProfileUpdateForm


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request=request, template_name='profile/profile.html', context={"user": request.user})
        return redirect('login')


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile/profile.html'
    success_url = reverse_lazy('profile')

    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({'errors': errors}, status=400)


class UploadImageView(View):

    def post(self, request):
        if 'avatar' in request.FILES:
            img = request.FILES.get('avatar')
            img_path = f'media/var/avatar/{img.name}'
            with open(img_path, 'wb') as file:
                for chunk in img.chunks():
                    file.write(chunk)
            return JsonResponse({'message': 'Image uploaded successfully', 'image_path': f'{img_path}'})

        return JsonResponse({'error': 'No image found in the request'}, status=400)


class SaveImageView(View):

    def post(self, request):
        if 'avatar' in request.POST:
            image_data = request.POST['avatar']
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            profile = request.user.profile
            profile.avatar.save('avatar.jpg', image)
            profile.save()
            return JsonResponse({'message': 'Image uploaded successfully'})

        return JsonResponse({'error': 'No image found in the request'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class TrashAvatar(View):

    def post(self, request):
        user = request.user
        try:
            profile = user.profile
            profile.avatar.delete(save=True)
            profile.save()
            return JsonResponse({'status': 'ok'})
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profile does not exist'}, status=400)