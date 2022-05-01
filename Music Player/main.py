import pygame as py
from pygame.locals import *
from pygame import display, time, mouse, font, mixer, key, draw, image
import os
import tkinter as tk
from tkinter import filedialog
import audio_metadata

py.init()
font.init()
mixer.init()
root = tk.Tk()
root.withdraw()


class Button:
    def __init__(self, 
    text:str, x:int, y:int, width:int=32, height:int=32, 
    font_size:py.font.Font=20, color:list=(255, 255, 255), 
    image_surface:py.Surface=None):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.width = width
        self.height = height
        self.font_size = font_size
        self.rect = (x, y, self.width, self.height)
        self.image = image_surface
    
    def draw(self, win):
        py.draw.rect(win, self.color, self.rect)
        font = py.font.SysFont('Arial', self.font_size)
        text = font.render(self.text, 1, (255, 255, 255))
        x = self.x + round(self.width/2) - round(text.get_width()/2)
        y = self.y + round(self.height/2) - round(text.get_height()/2)
        win.blit(text, (x, y))
        if self.image != None:
            image_x = self.x + round(self.width/2) - round(32/2)
            image_y = self.y + round(self.height/2) - round(32/2)
            win.blit(self.image, (image_x, image_y))
    def clicked(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


class Song:

    def __init__(self, path, files, count):
        self.current_song = count
        self.song = mixer.Sound(os.path.join(path, files[self.current_song]))
        self.max_count = len(files)
        self.metadata = audio_metadata.load(os.path.join(path, files[self.current_song]))
        self.none = 'None'

    def play(self):
        self.song.play()

    def pause(self):
        mixer.pause()

    def unpause(self):
        mixer.unpause()

    def next(self):
        if self.current_song < self.max_count:
            self.current_song += 1
            mixer.stop()
            return True, self.current_song
        return False, self.current_song
    
    def previous(self):
        if self.current_song > 0:
            self.current_song -= 1
            mixer.stop()
            return True, self.current_song
        return False, self.current_song
    
    def stop(self):
        mixer.stop()
        self.current_song = 0

    def set_volume(self, vol):
        self.song.set_volume(vol)

    def get_size(self):
        try:
            return str(self.metadata['filesize'])
        except:
            return self.none

    def get_len(self):
        try:
            return str(self.metadata.streaminfo['duration'])
        except:
            return self.none
        
    def get_album(self):
        try:
            return str(self.metadata.tags['album'])
        except:
            return self.none
    
    def get_artist(self):
        try:
            return str(self.metadata.tags['artist'])
        except:
            return self.none

    def get_date(self):
        try:
            return str(self.metadata.tags['date'])
        except:
            return self.none

    def get_title(self):
        try:
            return str(self.metadata.tags['title'])
        except:
            return self.none


pauseButton = image.load('src\\pauseButton.png')
playButton = image.load('src\\playButton.png')
muteButton = image.load('src\\muteButton.png')
volumeUpButton = image.load('src\\volumeUpButton.png')
volumeDownButton = image.load('src\\volumeDownButton.png')
previousButton = image.load('src\\previousButton.png')
nextButton = image.load('src\\nextButton.png')
FONT = font.Font('src\\font.ttf', 20)
TEXT_FONT = font.Font('src\\font.ttf', 40)
mute_font = font.SysFont('Arial', 40)
WIDTH, HEIGHT = 800, 500
WIN = display.set_mode((WIDTH, HEIGHT))
icon = image.load('src\\icon.jpg')
display.set_icon(icon)
display.set_caption('Music Player')
vol = 10
FPS = 30

def get_folder():
   file_path = filedialog.askdirectory()

   return file_path


def main(win):
    global vol
    run = True
    folder_path = None
    files = []
    current_song = 0
    is_get_files = False
    is_get_song = False
    is_playing = False
    is_paused = False
    is_mute = False
    button_open = Button("Open", 10, 10, 100, 40, 30, (128, 128, 128))
    button_pause = Button('', WIDTH/2-90, 400+25, 50, 50, 20, (128, 128, 255), pauseButton)
    button_play = Button('', WIDTH/2-20, 400+25, 50, 50, 20, (128, 128, 255), playButton)
    button_next = Button('', WIDTH/2+40, 400+25, 50, 50, 20, (128, 128, 255), nextButton)
    button_pre = Button('', WIDTH/2-160, 400+25, 50, 50, 20, (128, 128, 255), previousButton)
    button_volUp = Button('', WIDTH/2+100, 400+25, 50, 50, 20, (128, 128, 255), volumeUpButton)
    button_volDown = Button('', WIDTH/2-220, 400+25, 50, 50, 20, (128, 128, 255), volumeDownButton)
    button_mute = Button('', WIDTH/2-280, 425, 50, 50, 50, (128, 128, 128), muteButton)
    clock = time.Clock()
    while run:
        clock.tick(FPS)
        win.fill((200, 200, 200))
        
        button_volDown.draw(win)
        button_volUp.draw(win)
        button_pause.draw(win)
        button_open.draw(win)
        button_next.draw(win)
        button_play.draw(win)
        button_pre.draw(win)
        button_mute.draw(win)


        for event in py.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
                if event.key == K_o or event.key == K_INSERT:
                    try:
                        if is_get_files:mixer.stop()
                        folder_path = get_folder()
                        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f[-3:]=='mp3']
                        print(files)
                        is_get_files = True
                        is_get_song = False
                        is_playing = False
                    except:
                        pass
                if event.key == K_SPACE:
                    if is_playing and not is_paused and is_get_song:
                        print('pause')
                        song.pause()
                        is_paused = True
                    elif is_playing and is_paused and is_get_song:
                        print('unpause')
                        song.unpause()
                        is_paused = False
                if event.key == K_LEFT:
                    try:
                        ter, current_song = song.previous()
                    
                        if ter:
                            is_playing = False
                            is_get_song = False
                            is_paused = False
                        print(ter)
                    except:
                        pass
                if event.key == K_RIGHT:
                    try:
                        ter, current_song = song.next()
                    
                        if ter:
                            is_playing = False
                            is_get_song = False
                            is_paused = False
                        
                        print(ter)
                    except:
                        pass
                if event.key == K_m:
                    if is_mute:is_mute = False
                    else:is_mute=True

            if event.type == MOUSEBUTTONDOWN:
                pos = mouse.get_pos()
                if button_mute.clicked(pos):
                    if is_mute:is_mute = False
                    else:is_mute = True
                if button_open.clicked(pos):
                    try:
                        if is_get_files:mixer.stop()
                        folder_path = get_folder()
                        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f[-3:]=='mp3']
                        print(files)
                        is_get_files = True
                        is_get_song = False
                        is_playing = False
                    except:
                        pass
                if button_next.clicked(pos) and is_get_song:
                    ter, current_song = song.next()
                    if ter:
                        is_playing = False
                        is_get_song = False
                        is_paused = False
                    print(ter)
                if button_pre.clicked(pos) and is_get_song:
                    ter, current_song = song.previous()
                    if ter:
                        is_playing = False
                        is_get_song = False
                        is_paused = False
                    print(ter)

                if button_pause.clicked(pos) and is_get_song:
                    song.pause()
                    is_paused = True

                if button_play.clicked(pos) and is_get_song:
                    song.unpause()
                    is_paused = False
                
                if button_volUp.clicked(pos):
                    if vol < 100 and is_get_song:
                        vol += 1
                        song.set_volume(float(vol/100))
                    elif vol < 100:
                        vol += 1
                if button_volDown.clicked(pos):
                    if vol > 0 and is_get_song:
                        vol -= 1
                        song.set_volume(float(vol/100))
                    elif vol > 0:
                        vol -= 1

        pressed_key = key.get_pressed()
        if pressed_key[K_UP]:
            if vol < 100 and is_get_song:
                vol += 1
                if not is_mute and is_get_song:
                    song.set_volume(float(vol/100))
            elif vol < 100:
                vol += 1

        if pressed_key[K_DOWN]:
            if vol > 0 and is_get_song:
                vol -= 1
                if not is_mute and is_get_song:
                    song.set_volume(float(vol/100))
            elif vol > 0:
                vol -= 1


        text = TEXT_FONT.render(f'Volume: {str(int(vol))}', 0, (0, 0, 255))
        win.blit(text, [130, 10])


        if is_mute:
            text = mute_font.render('Mute', 1, (0, 0, 0))
            win.blit(text, [350, 10])
            if is_get_song:
                song.set_volume(0)
        elif not is_mute and is_get_song:
            song.set_volume(float(vol/100))
        

            

        if is_get_song:
            text = TEXT_FONT.render(f'Name: {files[current_song][:-4]}', 1, (255, 255, 200))
            win.blit(text, [80, 200])
            text = TEXT_FONT.render(f'Title: {song.get_title()[2:-2]}', 1, (51, 51, 255))
            win.blit(text, [80, 240])
            text = TEXT_FONT.render(f'Artist: {song.get_artist()[2:-2]}', 1, (255, 0, 127))
            win.blit(text, [80, 280])
            text = TEXT_FONT.render(f'Album: {song.get_album()[2:-2]}', 1, (255, 51, 51))
            win.blit(text, [80, 320])

        if is_get_files and not is_get_song:
            try:
                if files[current_song][-3:] == 'mp3':
                    song = Song(folder_path, files, current_song)
                is_get_song = True
            except IndexError:
                current_song = 0

        if not is_paused and is_get_files and not is_playing:
            song.play()
            if not is_mute:
                song.set_volume(float(vol/100))
            if is_mute:
                song.set_volume(0)
            is_playing = True
    
        draw.rect(win, (128, 255, 255), (130, 60, vol*2, 20))

        display.update()


    py.quit()

main(WIN)
