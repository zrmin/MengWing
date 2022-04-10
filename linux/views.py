from django.shortcuts import render

def linux_terminal(request):
    return render(request, 'linux/linux_terminal.html')

def linux_doc(request):
    return render(request, 'linux/linux_doc.html')
