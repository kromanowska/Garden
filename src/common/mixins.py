from django.contrib.auth.mixins import LoginRequiredMixin


class LoginSuperuserRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated \
                or not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class LoginDifferentSuperuserRequiredMixin(LoginRequiredMixin):
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated \
                or not request.user.is_superuser \
                or request.user.id == int(self.kwargs.get(self.pk_url_kwarg)):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
