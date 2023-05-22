import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


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
font = "Aventura-Bold.otf"
font1 = "Aventura-Bold.otf"
background = pygame.image.load("shady-forest-game-background.png").convert()


clock = pygame.time.Clock()
FPS = 60


# Main Menu
def main_menu():
    menu = True
    selected = "background"
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



                if sel%3 == 0:
                    selected = "musicoff"
                elif sel%3 == 1:
                    selected = "musicon"
                elif sel%3 == 2:
                    selected = "back"

                if event.key == pygame.K_RETURN:
                    if selected == "musicoff":
                        print("musicoff")
                    if selected == "musicon":
                        print("musicon")
                    if selected == "back":
                        import settings
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
        pygame.display.set_caption("TRUMPARIO")


main_menu()
pygame.quit()
quit()