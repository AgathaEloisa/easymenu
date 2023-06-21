from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def AdminView(request):
    return render(request, 'admin/admin.html')
# class AdminView(View):
#     def get(self, request, *args, **kwargs):
#         context = {

#         }
#         return render(request, 'admin/admin.html', context)
