import os
import django.http

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from sendfile import sendfile


class FileView(LoginRequiredMixin, View):
    def get(self, request, path):
        path = os.path.normpath(os.path.join(settings.SENDFILE_ROOT, path))
        if not os.path.isfile(path):
            raise django.http.Http404()
        return sendfile(request, path)
