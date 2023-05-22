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

# Game Fonts
font = "Menu/Retro.ttf"
background = pygame.image.load("Текстуры/dandy_konets_igri.jpg").convert()


clock = pygame.time.Clock()
FPS = 30


# Main Menu
def main_menu():
    f = open("about.txt", "t")
    print(f)
    menu = True
    selected = "Enter"
    sel = 0
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if sel == 0:
                    selected = "Enter"

                if event.key == pygame.K_RETURN:
                    if selected == "Enter":
                        pygame.quit()
                        quit()
        # Main Menu UI
        screen.blit(background, [0, 0])
        if selected == "Enter":
            text_quit = text_format("Enter", font, 20, red)
        else:
            text_quit = text_format("Enter", font, 20, white)


        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 500))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Он вам не димон")


main_menu()
pygame.quit()
quit()

if __name__ == "__main__":
    main()