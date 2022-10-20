from django.shortcuts import render, HttpResponse

contenido_html = """
<h1>Menú navegación</h1>
<ul>
    <li><a href="/">Índice</a></li>
    <li><a href="/contacto/">Contacto</a></li>
    <li><a href="/noticias/">Noticias</a></li>
    <li><a href="/acerca_de/">Acerca de</a></li>
</ul<
"""

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    return HttpResponse(contenido_html+ """
    <h2>Esto es el índice</h2>
    """)

def contacto(request):
    return render(request, 'core/contacto.html')
    return HttpResponse(contenido_html+ """
    <h2>Esto es el contacto</h2>
    """)

def acerca_de(request):
    return render(request, 'core/acerca_de.html')
    return HttpResponse(contenido_html+ """
    <h2>Esto es el acerca de</h2>
    """)