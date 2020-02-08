from django.shortcuts import render
import pafy
from django.utils.encoding import smart_str
from django.http import HttpResponse

def downloader(request):


    if request.method== 'POST':
        urls= request.POST.get('url')

        streamDetails= list()
        links= list()
        res= list()
        ext= list()
        size = list()
        
        video = pafy.new(urls)

        vt=video.title
        vd=video.description
        streams = video.streams
        best = video.getbest()

        for s in streams:
            streamDetails.append(s)
        
        for l in streams:
            response = HttpResponse(l.url,content_type='application/l.url') # mimetype is replaced by content_type for django 1.7
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(l.url)        
            links.append(response)
            res.append(l.resolution)
            ext.append(l.extension)
            sz= round(l.get_filesize()/1000000,2)
            size.append(sz)
        

        return render(request,'index.html',{'title':vt,'desc':vd,'strm':streamDetails,'dl':links,'rs':res,'ext':ext,'size':size})
    else:
         return render(request,'index.html')