#programa para generar una redaccion de correo electrónico predefinido

def generar_correo(destinatario, asunto, mensaje):
    """
    Genera un correo electrónico predefinido.

    Args:
        destinatario (str): Dirección de correo del destinatario.
        asunto (str): Asunto del correo.
        mensaje (str): Cuerpo del mensaje.

    Returns:
        str: Correo electrónico formateado.
    """
    correo = f"Para: {destinatario}\n"
    correo += f"Asunto: {asunto}\n\n"
    correo += f"{mensaje}\n"
    return correo


" Ejemplo de uso "


if __name__ == "__main__":
    
    destinatario = "cespedes.jac@gmail.com"      #Ingresa el correo del destinatario
    # Puedes cambiar el destinatario a cualquier correo electrónico válido.    # Asegúrate de que el destinatario sea una dirección de correo electrónico válida.


    asunto = "Prueba de correo" # Asunto del correo electrónico 
    
    
    mensaje = "Estimad@ Gerente: \n"  # Puedes personalizar el mensaje según tus necesidades.
    mensaje += "Espero que se encuentre bien, le informo que adjunto le envío el análisis de costo alimento del mes de junio.\n\n"
    mensaje += "Esperando que sea de su agrado, quedo muy atento a sus observaciones o solicitudes de cambio que desee.\n"  # Puedes personalizar el mensaje según tus necesidades.
    mensaje += "Saludos cordiales,\n"  # Puedes personalizar el mensaje según tus necesidades.
    

    correo_generado = generar_correo(destinatario, asunto, mensaje)
    print(correo_generado)


    import urllib.parse
    import webbrowser

    def enviar_gmail(destinatario, asunto, mensaje):
        asunto_encoded = urllib.parse.quote(asunto)
        mensaje_encoded = urllib.parse.quote(mensaje)
        url = f"https://mail.google.com/mail/?view=cm&fs=1&to={destinatario}&su={asunto_encoded}&body={mensaje_encoded}"
        webbrowser.open(url)

    # Ejemplo de uso para enviar el correo generado
    enviar_gmail(destinatario, asunto, mensaje)
    # Nota: Asegúrate de que el navegador esté configurado para abrir enlaces de correo electrónico.
    # Esto abrirá una nueva pestaña en el navegador con el formulario de Gmail prellen  