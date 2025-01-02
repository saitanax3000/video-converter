import yt_dlp

def descargar_video(link):
    try:
        # Configuración de la descarga
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Mejor calidad de video y audio
            'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo basado en el título
        }

        # Descargar el video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        print("¡Descarga completa!")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Solicitar enlace de YouTube al usuario
link_video = input("Introduce el enlace del video de YouTube: ")
descargar_video(link_video)
