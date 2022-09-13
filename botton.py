from genericpath import isfile
from pytube.cli import on_progress
from pytube import YouTube
from moviepy.editor import *
from time import sleep
import threading
import os

#Verifica e cria pasta para alocar o bot.
def criarPasta():
    if os.path.exists('BOT_TIKTOK'):
        print('Pasta já criada.')
    else:
        print('Criando pasta...')
        os.mkdir('BOT_TIKTOK')
        #Movendo para pasta indicada
        local_atual = f'{os.getcwd()}\\botton.py'
        local_destino = f'{os.getcwd()}\\BOT_TIKTOK\\botton.py'
        os.rename(local_atual, local_destino)
    
    # verifica se os vídeos ainda estão lá dentro, caso estejam, excluir eles
    if os.path.isfile('./BOT_TIKTOK/video.mp4'):
        os.remove('./BOT_TIKTOK/video.mp4')
    if os.path.isfile('./BOT_TIKTOK/video_pronto.mp4'):
        os.remove('./BOT_TIKTOK/video_pronto.mp4')

threading.Thread(target=criarPasta).start()

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
    except Exception as err:
        print(f'Error: {err}')
    #Renomeando
    vd = f'{yt.title}.mp4'
    os.rename(vd, 'video.mp4')
    #Movendo para pasta indicada
    local_atual = f'{os.getcwd()}\\video.mp4'
    local_destino = f'{os.getcwd()}\\BOT_TIKTOK\\video.mp4'
    os.rename(local_atual, local_destino)

baixar_video(url)

def cortarVideo(url):
    try:
        clip = VideoFileClip(url)
        clip = clip.subclip(50, 80)
        clip.write_videofile('video_pronto.mp4')
    except Exception as err:
        print(f'Não foi possível editar: {err}')

    local_atual = f'{os.getcwd()}\\video_pronto.mp4'
    local_destino = f'{os.getcwd()}\\BOT_TIKTOK\\video_pronto.mp4'
    os.rename(local_atual, local_destino)

cortarVideo('./BOT_TIKTOK/video.mp4')
