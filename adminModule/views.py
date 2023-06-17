from django.shortcuts import render
from django.views import View
# from django.contrib.auth.decorators import login_required

# @login_required
class AdminView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'admin/admin.html', context)
