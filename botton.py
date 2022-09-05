from pytube.cli import on_progress
from pytube import YouTube
from moviepy.editor import *
import os

#Verifica e cria pasta para alocar o bot.
def criarPasta():
    if os.path.exists('bot'):
        print('Pasta já criada.')
    else:
        print('Criando pasta...')
        os.mkdir('bot')
        #Movendo para pasta indicada
        local_atual = f'{os.getcwd()}\\botton.py'
        local_destino = f'{os.getcwd()}\\bot\\botton.py'
        os.rename(local_atual, local_destino)

criarPasta()

url = input(str('Cole aqui a URL do vídeo: '))

def baixar_video(url=str):
    #Baixando vídeo
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f'Preparando... vídeo: {yt.title}')
        video = yt.streams.get_highest_resolution()
        print('Baixando...')
        video.download()
        print('Download Finalizado!')
    except:
        print('Error')
    #Renomeando
    vd = f'{yt.title}.mp4'
    os.rename(vd, 'video.mp4')
    #Movendo para pasta indicada
    local_atual = f'{os.getcwd()}\\video.mp4'
    local_destino = f'{os.getcwd()}\\bot\\video.mp4'
    os.rename(local_atual, local_destino)

baixar_video(url)

def cortarVideo(url):
    try:
        clip = VideoFileClip(url)
        clip = clip.subclip(50, 80)
        clip.write_videofile('video_pronto.mp4')
    except:
        print('Não foi possível editar: ')

    local_atual = f'{os.getcwd()}\\video_pronto.mp4'
    local_destino = f'{os.getcwd()}\\bot\\video_pronto.mp4'
    os.rename(local_atual, local_destino)

cortarVideo('./bot/video.mp4')

if os.path.exists('./bot/video.mp4'):
    os.remove('./bot/video.mp4')
