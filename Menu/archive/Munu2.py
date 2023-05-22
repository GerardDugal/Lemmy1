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
font = "Retro.ttf"
font1 = "Retro.ttf"
background = pygame.image.load("123.gif").convert()


clock = pygame.time.Clock()
FPS = 60


# Main Menu
def main_menu():
    menu = True
    selected = "start"
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
                        print("Start")
                    if selected == "settings":
                        import settings
                    if selected == "about":
                        open("about.txt")
                    if selected == "quit":
                        pygame.quit()
                        quit()
        # Main Menu UI
        screen.blit(background, [0, 0])
        title = text_format("TRUMPARIO", font, 90, darkviolet)
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
        pygame.display.set_caption("TRUMPARIO")


main_menu()
pygame.quit()
quit()