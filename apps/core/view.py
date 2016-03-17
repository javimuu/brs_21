from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
import json
import base64


class LoginRequiredMixin(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def upload_to_imgur(image_path, title):
    file = open(image_path, 'rb')
    binary_data = file.read()
    base64image = base64.b64encode(binary_data)

    payload = {'key': settings.IMGUR_SECRET,
               'image': base64image,
               'title': title}
    headers = {"Authorization": "Client-ID "+settings.IMGUR_ID}
    response = requests.post(
        settings.IMGUR_URL,
        headers=headers,
        data=payload
    )

    json_tmp = json.loads(response.text)
    if not json_tmp['success']:
        return None
    return json_tmp['link']


