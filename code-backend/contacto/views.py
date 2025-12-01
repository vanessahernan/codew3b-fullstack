# contacto/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

# Deshabilita la protección CSRF para esta vista, necesaria para la comunicación con Vue
@csrf_exempt 
def contact_form_submit(request):
    if request.method == 'POST':
        try:
            # 1. Parsear el JSON del frontend
            data = json.loads(request.body)
            # Asegúrate de que estas claves coincidan con lo que envías desde Vue
            nombre = data.get('nombre')
            email = data.get('email')
            idea_proyecto = data.get('idea_proyecto') 

            # 2. Validación básica
            if not all([nombre, email, idea_proyecto]):
                return JsonResponse({'message': 'Faltan campos obligatorios.'}, status=400)

            # 3. Construir el correo
            subject = f"NUEVA PROPUESTA DE PROYECTO de {nombre} (CodeW3b)"
            
            html_message = f"""
                <html><body>
                    <h2>Detalles del Cliente:</h2>
                    <p><strong>Nombre:</strong> {nombre}</p>
                    <p><strong>Correo:</strong> <a href="mailto:{email}">{email}</a></p>
                    <hr>
                    <h3>Idea del Proyecto:</h3>
                    <p>{idea_proyecto.replace('\n', '<br>')}</p>
                </body></html>
            """
            
            # 4. Enviar el correo usando la configuración SMTP de settings.py
            send_mail(
                subject,
                f"Nombre: {nombre}\nCorreo: {email}\n\nProyecto:\n{idea_proyecto}", # Mensaje en texto plano (fallback)
                settings.SERVER_EMAIL,                          # Remitente (tu correo de envío)
                ['codew3b25@gmail.com'],               # Destinatario (Tu correo personal)
                fail_silently=False,
                html_message=html_message                       
            )

            # 5. Respuesta de Éxito al Frontend
            return JsonResponse({'message': 'Propuesta enviada con éxito!'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Formato de datos JSON inválido.'}, status=400)
        except Exception as e:
            # Esto imprimirá el error real (ej. credenciales inválidas) en tu terminal
            print(f"Error al enviar correo: {e}") 
            return JsonResponse({'message': 'Error interno del servidor al enviar el correo.'}, status=500)
    
    return JsonResponse({'message': 'Método no permitido.'}, status=405)