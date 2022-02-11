from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import PescriptionCreateForm
from django.contrib import messages
# Create your views here.
class HomeView(View):
    template_name='core/index.html'
    def get(self, request):
        return render(request, self.template_name)

class PescriptionCreateView(View):
    template_name='core/pescription_create.html'
    pescription_form = PescriptionCreateForm
    def get(self, request):
        return render(request, self.template_name, {'form': self.pescription_form})

    def post(self, request):
        form = self.pescription_form(request.POST, request.FILES)
        if form.is_valid():
            form_user=form.save(commit=False)
            form_user.user= request.user
            form_user.save()
            messages.success(request,'Pescription is uploaded successfully')
            return redirect('core:home')
        return render(request,self.template_name, {'form':form})
