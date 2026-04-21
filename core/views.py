from django.shortcuts import render, redirect
from .models import LogFile 
from .analyzer import analyzer_log
from django.contrib.auth.decorators import login_required
import os 

# Create your views here.

@login_required(login_url='login')
def upload_log(request):
    if request.method == 'POST':
        if 'log_file' not in request.FILES:
            return render(request, 'corehtml/upload.html', {'error': 'Please select a file to upload'})
        
        file = request.FILES['log_file']
        log = LogFile.objects.create(file=file, user=request.user)
        # analyzer immediatley after upload
        file_path = log.file.path
        results = analyzer_log(file_path)
        return render(request, 'corehtml/result.html', {'results': results})
    return render(request, 'corehtml/upload.html')


@login_required(login_url='login')
def dashboard(request):
    logs = LogFile.objects.filter(user=request.user) # only current user's logs

    # analyze all uploaded logs
    all_ips = {}
    for log in logs:
        try:
            if os.path.exists(log.file.path):
                results = analyzer_log(log.file.path)
                for ip, count in results['suspicious_ips'].items():
                    all_ips[ip] = all_ips.get(ip, 0) + count
        except FileNotFoundError:
            # Skip files that no longer exist
            pass

    return render(request, 'corehtml/dashboard.html', {
         'logs': logs,
         'all_ips': all_ips 
         })




