from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .models import Disabled_ch, Notice_nocookie, RollFile

# Create your views here.



def nocookie(request):
    template_name = "youtube_nocookie.html"
    context = {}
    chs = Disabled_ch.objects.filter(is_noticed=True)
    context['chs'] = chs
    notice = Notice_nocookie.objects.all()
    if notice:
        context['notice'] = notice[0]

    if request.method == "POST":
        ch_val = request.POST.get('new_ch')
        if Disabled_ch.objects.filter(ch_name=ch_val):
            exist_ch = Disabled_ch.objects.get(ch_name=ch_val)
            exist_ch.is_noticed = True
            exist_ch.save()
        else:
            new_ch = Disabled_ch(ch_name=ch_val)
            new_ch.save()

    return render(request, template_name, context)

def GsuiteConvertor(request):
    template_name = "g-suite_convertor.html"
    context = {}

    if request.method == 'POST':
        file = request.FILES['roll_file']
        file_name = f'{request.POST.get("school")}_user.csv'
        fs = FileSystemStorage()
        filename = fs.save(file_name, file)
        # roll_file = RollFile(title=file_name,
        # roll_file=file)
        # roll_file.save()
        # context['result_url'] = roll_file
        context['result_url'] = fs.url(filename)


    return render(request, template_name, context)