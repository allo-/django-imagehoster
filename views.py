from django.views.generic.simple import direct_to_template
from django.views.generic.list import ListView
from django.shortcuts import redirect

import settings
from forms import ImageUploadForm
from models import Image

def upload(request):
    if not request.POST:
        form = ImageUploadForm()
    else:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            relative_url = settings.MEDIA_URL + settings.UPLOAD_DIR + str(form.cleaned_data['image'])
            return redirect(relative_url)
    return direct_to_template(request, "upload.html", {'form': form})

class file_list(ListView):
    model = Image
    def get_context_data(self, **kwargs):
        context = super(file_list, self).get_context_data(**kwargs)
        context['form'] = ImageUploadForm()
        return context

    def get_queryset(self):
        return self.model.objects.filter(private=False).order_by("-date")
