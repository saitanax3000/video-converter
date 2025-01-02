# Herramienta para videos y converter

## Comandos y tools: 
pip install yt-dlp
yt-dlp --version

## Dirígete a la página de descargas de ffmpeg.
https://ffmpeg.org/download.html
by BtBN

## Agregar ffmpeg al PATH del sistema:
Haz clic con el botón derecho en Este PC (o Mi PC) y selecciona Propiedades.
En el panel izquierdo, selecciona Configuración avanzada del sistema.
En la ventana de Propiedades del sistema, haz clic en Variables de entorno.
En la sección de Variables del sistema, busca la variable Path y haz clic en Editar.
En la ventana de edición, agrega la ruta completa de la carpeta bin de ffmpeg, por ejemplo: C:\ffmpeg\bin.

Prueba en una nueva consola: ffmpeg -version

## Convertir a mp4
ffmpeg -i input_video.webm output_video.mp4
