from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def is_admin(user):
    return user.is_authenticated and user.is_superuser

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not is_admin(request.user):
            return redirect('base:index')  # Redirect to the home page
        return view_func(request, *args, **kwargs)
    return _wrapped_view