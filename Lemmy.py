import pygame
from pygame import *
from pygame.sprite import Sprite, collide_rect #не забывать импортировать всё что нужно
from pygame import Surface
from pygame.image import load
import pyganim
# import sys


pygame.init()

def Music():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    darkviolet = (148, 0, 211)
    mediumviolet = (186, 85, 211)

    # Game Fonts
    font = "Menu/Aventura-Bold.otf"
    font1 = "Menu/Aventura-Bold.otf"
    background = pygame.image.load("Текстуры/shady-forest-game-background.png").convert()

    clock = pygame.time.Clock()
    FPS = 60

    # Main Menu
    def main_menu():
        menu = True
        selected = "musicoff"
        sel = 0
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sel -= 1

                    elif event.key == pygame.K_DOWN:
                        sel += 1

                    if sel % 3 == 0:
                        selected = "musicoff"
                    elif sel % 3 == 1:
                        selected = "musicon"
                    elif sel % 3 == 2:
                        selected = "back"

                    if event.key == pygame.K_RETURN:
                        if selected == "musicoff":
                            pygame.mixer.music.stop()
                            print("musicoff")
                        if selected == "musicon":
                            pygame.mixer.music.play(-1)
                            print("musicon")
                        if selected == "back":
                            menu = False
                            # quit()
            # Main Menu UI
            screen.blit(background, [0, 0])
            title = text_format("SETTINGS", font, 90, darkviolet)
            if selected == "musicoff":
                text_musicoff = text_format("MUSIC OFF", font, 75, mediumviolet)
            else:
                text_musicoff = text_format("MUSIC OFF", font, 75, black)
            if selected == "musicon":
                text_musicon = text_format("MUSIC ON", font, 75, mediumviolet)
            else:
                text_musicon = text_format("MUSIC ON", font, 75, black)
            if selected == "back":
                text_back = text_format("BACK", font, 75, mediumviolet)
            else:
                text_back = text_format("BACK", font, 75, black)

            title_rect = title.get_rect()
            musicoff_rect = text_musicoff.get_rect()
            musicon_rect = text_musicon.get_rect()
            back_rect = text_back.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
            screen.blit(text_musicoff, (screen_width / 2 - (musicoff_rect[2] / 2), 230))
            screen.blit(text_musicon, (screen_width / 2 - (musicon_rect[2] / 2), 295))
            screen.blit(text_back, (screen_width / 2 - (back_rect[2] / 2), 425))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("LEMMY")

    main_menu()
def Pause():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText


    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    darkviolet = (148, 0, 211)
    mediumviolet = (186, 85, 211)

    # Game Fonts
    font = "Menu/Aventura-Bold.otf"
    font1 = "Menu/Aventura-Bold.otf"
    background = pygame.image.load("Текстуры/shady-forest-game-background.png").convert()


    clock = pygame.time.Clock()
    FPS = 60
    # Main Menu
    def main_menu():
        selected = "Play"
        sel = 0
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sel -= 1

                    elif event.key == pygame.K_DOWN:
                        sel += 1


                    if sel%4 == 0:
                        selected = "Play"
                    elif sel%4 == 1:
                        selected = "quit"

                    if event.key == pygame.K_RETURN:
                        if selected == "Play":
                            menu = False
                        if selected == "quit":
                            pygame.quit()
                            quit()
            # Main Menu UI
            screen.blit(background, [0, 0])
            title = text_format("PAUSE", font, 90, darkviolet)
            if selected == "Play":
                text_start = text_format("PLAY", font, 75, mediumviolet)
            else:
                text_start = text_format("PLAY", font, 75, black)
            if selected == "quit":
                text_quit = text_format("QUIT", font, 75, mediumviolet)
            else:
                text_quit = text_format("QUIT", font, 75, black)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
            screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 230))
            screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 425))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("LEMMY")
    main_menu()

global level
level = [
 "        ****************************************************************************************************************-",
 "                                                                                                                        -",
 "                                                                                                                        -",
 "                                                                                                                        -",
 "                                                                                                                        -",
 "                                                                                                                        -",
 "                *                                                                                                       -",
 "       *-                                              ---     *                        -    *                          -",
 "                       -                                                                          -                     -",
 "                                                                                                   **    -             F-",
 "                                              -                              -                                        ---",
 "               -                                                                                                     -  -",
 "                                                                                                -*                      -",
 "                                      -                             -                           **                      -",
 "                                                                                                                        -",
 "           -                                            *-                                                   ------     -",
 "      @                    *-                                                                 -                         -",
 "    ---                                                                                                                 -",
 "----*********************************************************************************************************************"]
def Levels():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    darkviolet = (148, 0, 211)
    mediumviolet = (186, 85, 211)

    # Game Fonts
    font = "Menu/Aventura-Bold.otf"
    font1 = "Menu/Aventura-Bold.otf"
    background = pygame.image.load("Текстуры/shady-forest-game-background.png").convert()

    clock = pygame.time.Clock()
    FPS = 60

    # Main Menu
    def main_menu():
        menu1 = True
        selected = "Ease"
        sel = 0
        while menu1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sel -= 1

                    elif event.key == pygame.K_DOWN:
                        sel += 1

                    if sel % 4 == 0:
                        selected = "Ease"
                    elif sel % 4 == 1:
                        selected = "Medium"
                    elif sel % 4 == 2:
                        selected = "Hard"
                    elif sel % 4 == 3:
                        selected = "back"

                    if event.key == pygame.K_RETURN:
                        if selected == "Ease":
                            global level
                            level = [
                                "        ****************************************************************************************************************-",
                                "                                                                                                                        -",
                                "                                                                                                                        -",
                                "                                                                                                                        -",
                                "                                                                                                                        -",
                                "                                                                                                                        -",
                                "                *                                                                                                       -",
                                "       *-                                              ---     *                        -    *                          -",
                                "                       -                                                                          -                     -",
                                "                                                                                                   **    -             F-",
                                "                                              -                              -                                        ---",
                                "               -                                                                                                     -  -",
                                "                                                                                                -*                      -",
                                "                                      -                             -                           **                      -",
                                "                                                                                                                        -",
                                "           -                                            *-                                                   ------     -",
                                "      @                    *-                                                                 -                         -",
                                "    ---                                                                                                                 -",
                                "----*********************************************************************************************************************"]
                            menu1 = False
                        if selected == "Medium":
                            level = [
                                "       ****************************************************************************************************************-",
                                "                                                                                                                       -",
                                "                                                                                                                       -",
                                "                                                                                                                       -",
                                "                                                                                                                       -",
                                "                                 *                                                                                     -",
                                "                                                                                            -    *                     -",
                                "                                 ---                                                             *                     -",
                                "                                                                                         *       *                     -",
                                "                  *  -                         --                ******              -  *        *                    F-",
                                "                  *                                                                                                  ---",
                                "                                        *  -                                                                        -  -",
                                "               -                                                               -                                       -",
                                "          *                               *                    --------                                                -",
                                "                               *                                                                               *       -",
                                "                               * -     *                                                                     --*--     -",
                                "    @     ---  *                      *                   -                                            -               -",
                                "  ---             -                 - *------                                               -                          -",
                                "--*********************************************************************************************************************-"]
                            menu1 = False
                        if selected == "Hard":
                            level = [
                                "     ******************************************************************************************************************-",
                                "                                                                                                                         -",
                                "                                                                                                                         -",
                                "                                                *                              **                                        -",
                                "                  *-                                   *                                                                 -",
                                "                                            -                                                                            -",
                                "                         --                 *       ----                                                                 -",
                                "          ---                                                                 ---                                        -",
                                "                  --                                          -                                           L              -",
                                "                          *  -              *  --                                                                        -",
                                "               ***                                *                 -                     *                        F     -",
                                "                                --                         *                                      ---            -----   -",
                                "                                                        ------                                                           -",
                                "                         ---           **              -                                                                 -",
                                "                                    --     ---                                                            -              -",
                                "            ---                                                                          ---                             -",
                                "      @                                                                                                                  -",
                                "    ---            --         --                  --                             *-*                                     -",
                                "----****************************************************************************************************************** -"]
                            menu1 = False
                        if selected == "back":
                            menu1 = False

                            # quit()
            # Main Menu UI
            screen.blit(background, [0, 0])
            title = text_format("CHOOSE YOUR LEVEL", font, 60, darkviolet)
            if selected == "Ease":
                text_level = text_format("EASE", font, 75, mediumviolet)
            else:
                text_level = text_format("EASE", font, 75, black)
            if selected == "Medium":
                text_music = text_format("MEDIUM", font, 75, mediumviolet)
            else:
                text_music = text_format("MEDIUM", font, 75, black)
            if selected == "Hard":
                text_back = text_format("HARD", font, 75, mediumviolet)
            else:
                text_back = text_format("HARD", font, 75, black)
            if selected == "back":
                B_back = text_format("BACK", font, 75, mediumviolet)
            else:
                B_back = text_format("BACK", font, 75, black)

            title_rect = title.get_rect()
            level_rect = text_level.get_rect()
            music_rect = text_music.get_rect()
            back_rect = text_back.get_rect()
            back_Back = B_back.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 40))
            screen.blit(text_level, (screen_width / 2 - (level_rect[2] / 2), 255))
            screen.blit(text_music, (screen_width / 2 - (music_rect[2] / 2), 320))
            screen.blit(text_back, (screen_width / 2 - (back_rect[2] / 2), 385))
            screen.blit(B_back, (screen_width / 2 - (back_Back[2] / 2), 470))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Lemmy")

    main_menu()


def Settings():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    darkviolet = (148, 0, 211)
    mediumviolet = (186, 85, 211)

    # Game Fonts
    font = "Menu/Aventura-Bold.otf"
    font1 = "Menu/Aventura-Bold.otf"
    background = pygame.image.load("Текстуры/shady-forest-game-background.png").convert()

    clock = pygame.time.Clock()
    FPS = 60

    # Main Menu
    def Settings_menu():
        menu = True
        selected = "level"
        sel = 0
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sel -= 1

                    elif event.key == pygame.K_DOWN:
                        sel += 1

                    if sel % 4 == 0:
                        selected = "level"
                    elif sel % 4 == 1:
                        selected = "music"
                    elif sel % 4 == 2:
                        selected = "back"

                    if event.key == pygame.K_RETURN:
                        if selected == "level":
                            Levels()
                        if selected == "music":
                            Music()
                        if selected == "back":
                            menu = False

                            # quit()
            # Main Menu UI
            screen.blit(background, [0, 0])
            title = text_format("SETTINGS", font, 90, darkviolet)
            if selected == "level":
                text_level = text_format("LEVEL", font, 75, mediumviolet)
            else:
                text_level = text_format("LEVEL", font, 75, black)
            if selected == "music":
                text_music = text_format("MUSIC", font, 75, mediumviolet)
            else:
                text_music = text_format("MUSIC", font, 75, black)
            if selected == "back":
                text_back = text_format("BACK", font, 75, mediumviolet)
            else:
                text_back = text_format("BACK", font, 75, black)

            title_rect = title.get_rect()
            level_rect = text_level.get_rect()
            music_rect = text_music.get_rect()
            back_rect = text_back.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
            screen.blit(text_level, (screen_width / 2 - (level_rect[2] / 2), 295))
            screen.blit(text_music, (screen_width / 2 - (music_rect[2] / 2), 360))
            screen.blit(text_back, (screen_width / 2 - (back_rect[2] / 2), 425))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Lemmy")

    Settings_menu()

pygame.mixer.init()
sound = pygame.mixer.music.load('Звук/Kevin-MacLeod_-_Run-Amok_musplay.cc (online-audio-converter.com).ogg')
pygame.mixer.music.play(-1)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
darkviolet = (148, 0, 211)
mediumviolet = (186, 85, 211)

# Game Fonts
font = "Menu/Aventura-Bold.otf"
font1 = "Menu/Aventura-Bold.otf"
background = pygame.image.load("Текстуры/shady-forest-game-background.png").convert()


clock = pygame.time.Clock()
FPS = 60
# Main Menu
def main_menu():
    selected = "start"
    sel = 0
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sel -= 1

                elif event.key == pygame.K_DOWN:
                    sel += 1


                if sel%4 == 0:
                    selected = "start"
                elif sel%4 == 1:
                    selected = "settings"
                elif sel%4 == 2:
                    selected = "about"
                elif sel%4 == 3:
                    selected = "quit"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        menu = False
                    if selected == "settings":
                        Settings()
                    if selected == "about":
                        open("J:/untitled3/about.txt")
                    if selected == "quit":
                        pygame.quit()
                        quit()
        # Main Menu UI
        screen.blit(background, [0, 0])
        title = text_format("LEMMY", font, 90, darkviolet)
        if selected == "start":
            text_start = text_format("START", font, 75, mediumviolet)
        else:
            text_start = text_format("START", font, 75, black)
        if selected == "settings":
            text_settings = text_format("SETTINGS", font, 75, mediumviolet)
        else:
            text_settings = text_format("SETTINGS", font, 75, black)
        if selected == "about":
            text_about = text_format("ABOUT", font, 75, mediumviolet)
        else:
            text_about = text_format("ABOUT", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, mediumviolet)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        settings_rect = text_settings.get_rect()
        about_rect = text_about.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 230))
        screen.blit(text_settings, (screen_width / 2 - (settings_rect[2] / 2), 295))
        screen.blit(text_about, (screen_width / 2 - (about_rect[2] / 2), 360))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 425))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Lemmy")
main_menu()

def Game_over():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    # Game Fonts
    font = "Retro.ttf"
    background = pygame.image.load("Текстуры/dandy_konets_igri.jpg").convert()

    clock = pygame.time.Clock()
    FPS = 30

    # Main Menu
    def Game_over_menu():
        menu = True
        selected = "Try again"
        sel = 0
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if sel == 0:
                        selected = "Try again"

                    if event.key == pygame.K_RETURN:
                        if selected == "Try again":
                            pygame.quit()
                            quit()
            # Main Menu UI
            screen.blit(background, [0, 0])
            if selected == "Try again":
                text_enter = text_format("Try again", font, 20, red)
            else:
                text_enter = text_format("Try again", font, 20, white)


            quit_rect = text_enter.get_rect()

            # Main Menu Text
            screen.blit(text_enter, (screen_width / 2 - (quit_rect[2] / 2), 500))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("LEMMY")

    Game_over_menu()

def Congratulations():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    # Game Fonts
    font = "Menu/Aventura-Bold.otf"
    background = pygame.image.load("Текстуры/twitter-интернет-отношения-3416281.jpeg").convert()

    clock = pygame.time.Clock()
    FPS = 30

    # Main Menu
    def Game_over_menu():
        menu = True
        selected = " "
        sel = 0

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if sel == 0:
                        selected = " "
                    if event.key == pygame.K_RETURN:
                        if selected == " ":
                            pygame.quit()
                            quit()
            # Main Menu UI
            screen.blit(background, [0, 0])
            if selected == " ":
                text_enter = text_format(" ", font, 20, red)
            else:
                text_enter = text_format(" ", font, 20, white)

            quit_rect = text_enter.get_rect()

            # Main Menu Text
            screen.blit(text_enter, (screen_width / 2 - (quit_rect[2] / 2), 500))
            screen.blit(info_string, (0, 0))
            info_string.fill((139, 0, 255))
            info_string.blit(speed_font.render('YOUR TIME: ' + str(counter), True, (0, 0, 0)), (100, 1))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("LEMMY")

    Game_over_menu()


pygame.display.set_caption("LEMMY") #название окна

#платформа
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

#доллары
DOLLARS_WIDTH = 32
DOLLARS_HEIGHT = 32

#окно
WIN_WIDTH = 800
WIN_HEIGHT = 600


WIDTH = 22
HEIGHT = 32


PLATFORM_COLOR = "#FF6262"
BACKGROUND_COLOR = pygame.image.load('Текстуры/GererdLOX.png').convert()



DISPLAY = (WIN_WIDTH, WIN_HEIGHT) #  Группируем ширину и высоту в одну переменную
screen = pygame.Surface(DISPLAY)
screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.FULLSCREEN)


MOVE_SPEED = 7
JUMP_POWER = 10
GRAVITY = 0.4

global HITPOINTS
HITPOINTS = 50

class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('Текстуры/world_inactive_block.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class BlockDie(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        Platform.__init__(self, x, y)
        self.image = image.load("Текстуры/dieBlock.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class LieBlockDie(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        Platform.__init__(self, x, y)
        self.image = image.load("Текстуры/world_inactive_block.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Dollars(Sprite):
    def __init__(self, x1, y1):
        Sprite.__init__(self)
        self.image = load('Текстуры/imgonline-com-ua-Resize-9E3FzKpwN2u.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0

class Finish(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('Текстуры/checkered-vector-4.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0


ANIMATION_DELAY = 1

ANIMATION_STAY = [('Дима/Покой право.png', ANIMATION_DELAY)]
ANIMATION_JUMP_R = ['Дима/прыжок право 1.png',
                    'Дима/прыжок право 2.png',
                    'Дима/прыжок право 3.png',
                    'Дима/прыжок право 4.png',
                    'Дима/прыжок право 5.png',
                    'Дима/прыжок право 6.png',
                    'Дима/прыжок право 7.png',
                    'Дима/прыжок право 8.png',
                    'Дима/прыжок право 9.png']

ANIMATION_JUMP_L = ['Дима/прыжок лево 1.png',
                    'Дима/прыжок лево 2.png',
                    'Дима/прыжок лево 3.png',
                    'Дима/прыжок лево 4.png',
                    'Дима/прыжок лево 5.png',
                    'Дима/прыжок лево 6.png',
                    'Дима/прыжок лево 7.png',
                    'Дима/прыжок лево 8.png',
                    'Дима/прыжок лево 9.png']

ANIMATION_RIGHT = ['Дима/бег право 1.png',
                   'Дима/бег право 2.png',
                   'Дима/бег право 3.png',
                   'Дима/бег право 4.png',
                   'Дима/бег право 5.png',
                   'Дима/бег право 6.png',
                   'Дима/бег право 7.png',
                   'Дима/бег право 8.png',
                   'Дима/бег право 9.png',
                   'Дима/бег право 10.png']

ANIMATION_LEFT = ['Дима/бег лево 1.png',
                  'Дима/бег лево 2.png',
                  'Дима/бег лево 3.png',
                  'Дима/бег лево 4.png',
                  'Дима/бег лево 5.png',
                  'Дима/бег лево 6.png',
                  'Дима/бег лево 7.png',
                  'Дима/бег лево 8.png',
                  'Дима/бег лево 9.png',
                  'Дима/бег лево 10.png']

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((60, 71))
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startX = 0  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = 0
        self.onGround = False
        self.image.set_colorkey((0, 0, 0))
        self.HITPOINTS = 3
        self.SCORE = 0



        def make_boltAnim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

        self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()

        self.boltAnimJumpR = make_boltAnim(ANIMATION_JUMP_R, ANIMATION_DELAY)
        self.boltAnimJumpR.play()

        self.boltAnimJumpL = make_boltAnim(ANIMATION_JUMP_L, ANIMATION_DELAY)
        self.boltAnimJumpL.play()

        self.jump_sound = mixer.Sound('Звук/sfx-13.ogg')
    def update(self, left, right, up, platforms):
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill((0, 0, 0))
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.xvel = MOVE_SPEED
            self.image.fill((0, 0, 0))
            self.boltAnimRight.blit(self.image, (0, 0))
        if not(left or right):
            self.xvel = 0
            if not up:
                self.image.fill((0, 0, 0))
                self.boltAnimStay.blit(self.image, (0, 0))

        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.jump_sound.play()



        if up and right:
            self.boltAnimJumpR.blit(self.image, (0, 0))
            self.boltAnimRight.stop()
        else:
            self.boltAnimRight.play()

        if up and left:
            self.boltAnimJumpL.blit(self.image, (0, 0))
            self.boltAnimLeft.stop()
        else:
            self.boltAnimLeft.play()
        if not self.onGround:
            self.yvel += GRAVITY
        if self.rect.x < -2:
            self.die()


        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if isinstance(pl, BlockDie): # если пересакаемый блок - blocks.BlockDie или Monster
                    self.die()# умираем
                if isinstance(pl, LieBlockDie): # если пересакаемый блок - blocks.BlockDie или Monster
                    self.die()# умираем
                if isinstance(pl, Finish):
                    pygame.mixer.music.stop()
                    jump_sound = mixer.Sound('Звук/Queen - We Are A Champions (online-audio-converter.com).ogg')
                    jump_sound.play()
                    Congratulations()
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def die(self):
        self.teleporting(0, 0) # перемещаемся в начальные координаты
        global HITPOINTS
        HITPOINTS -= 1
        if HITPOINTS == 0:
            pygame.mixer.music.stop()
            jump_sound = mixer.Sound('Звук/К_-_К_(Audio-VK4.ru).ogg')
            jump_sound.play()
            Game_over()
            global gameover
            gameover = True
        info_string.fill((45, 80, 40))
        info_string.blit(speed_font.render('HITPOINTS: ' + str(HITPOINTS), 1, (0, 0, 0)), (10, 1))

def time():
    info_string.fill((45, 80, 40))
    info_string.blit(speed_font.render('YOUR TIME: ' + str(counter), True, (0, 0, 0)), (200, 1))
    info_string.blit(speed_font.render('HITPOINTS: ' + str(HITPOINTS), 1, (0, 0, 0)), (10, 1))

#создание героя
hero = Player(32, 400)
left = right = up = False

#создание уровня
sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms = []

x = 0
y = 0
for row in level:
    for col in row:
        if col == "-":
            pl = Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        if col == "*":
            bd = BlockDie(x, y)
            sprite_group.add(bd)
            platforms.append(bd)
        if col == "@":
            dl = Dollars(x, y)
            sprite_group.add(dl)
        if col == "L":
            lb = LieBlockDie(x, y)
            sprite_group.add(lb)
            platforms.append(lb)
        if col == "F":
            fb = Finish(x, y)
            sprite_group.add(fb)
            platforms.append(fb)
        x += PLATFORM_WIDTH
    y += PLATFORM_HEIGHT
    x = 0


global gameover
gameover = False
timer = pygame.time.Clock()

#камера
class Camera():
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0,0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + WIN_WIDTH / 2
    t = -target_rect.y + WIN_HEIGHT / 2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - DISPLAY[0]), l)
    t = max(-(camera.height - DISPLAY[1]), t)
    t = min(0, t)
    screen.blit(info_string, (0, 0))
    return pygame.Rect(l, t, w, h)

total_level_width = len(level[0]) * 32
total_level_height = len(level) * 32

camera = Camera(camera_func, total_level_width, total_level_height)


#информационная строка
info_string = pygame.Surface((380, 30))

#шрифты
pygame.font.init()
speed_font = pygame.font.Font(None, 32)


#отрисовка шрифтов
info_string.fill((45, 80, 40))
info_string.blit(speed_font.render('HITPOINTS: ' + str(3), 1, (0, 0, 0)), (10, 1))
info_string.blit(speed_font.render('SCORE: ' + str(0), 1, (0, 0, 0)), (200, 1))

#время
counter = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Настройка звука


while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter += 1
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_w:
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_d:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.05)
                print(pygame.mixer.music.get_volume())
            if event.key == pygame.K_a:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.05)
                print(pygame.mixer.music.get_volume())
            if event.key == pygame.K_ESCAPE:
                gameover = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False




    screen.blit(info_string, (0, 0))
    time()
    #рабочая поверхность
    screen.blit(BACKGROUND_COLOR, (0,0))

    #отображение героя

    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))
    camera.update(hero)
    hero.update(left, right, up, platforms)



    #обновление окна
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    timer.tick(60)
