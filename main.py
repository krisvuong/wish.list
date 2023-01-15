import pygame as pg, sys


class Home:
    def __init__(self):
        self.bg = "#171717"
        self.settings_bg = "#c4c4c4"
        self.explore_bg = "#29299e"
        pg.init()
        # self.width = self.screen.get_size()[0]
        # self.height = self.screen.get_size()[1]
        self.width = 1280
        self.height = 720
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.font = "assets/SFPRODISPLAYBOLD.OTF"

    def get_font(self, file_path, size):
        return pg.font.Font(file_path, size)

    def fade_out(self, colour):
        fade = pg.Surface((self.width, self.height))
        fade.fill(colour)
        for alpha in range(0, 30):
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0, 0))
            pg.display.update()
            self.clock.tick(60)

    # handles all events
    def handler(self, event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # if a key is pressed
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:  # if press 1: change bg to red
                self.bg = (226, 114, 106)

            elif event.key == pg.K_2:  # if press 2: change bg to green
                self.bg = (163, 136, 191)

            elif event.key == pg.K_3:  # if press 2: change bg to green
                self.settings_menu()

    def main_menu(self):
        pg.display.set_caption("Main Menu")

        while True:

            # fill with default bg colour
            self.screen.fill(self.bg)

            # DO THINGS HERE

            # get mouse position
            mouse_pos = pg.mouse.get_pos()

            # create buttons
            main_settings = Button(image=None, pos=(self.width // 2, self.height * 0.75), text_input="Settings",
                                   font=self.get_font(self.font, 50), base_color="#8f8f8f",
                                   hovering_color="White")

            main_explore = Button(image=None, pos=(self.width // 2, self.height // 2), text_input="Explore",
                                  font=self.get_font(self.font, 100), base_color="#09b2e6",
                                  hovering_color="White")

            # NO MORE DOING THINGS AFTER HERE

            # catch all events
            for event in pg.event.get():
                self.handler(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    # change menu screen if click on button
                    if main_settings.checkForInput(mouse_pos):
                        self.fade_out(self.settings_bg)
                        self.settings_menu()
                    elif main_explore.checkForInput(mouse_pos):
                        self.fade_out(self.explore_bg)
                        self.explore_menu()

            # change colour of button if hovering
            for button in [main_settings, main_explore]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            # update screen
            pg.display.flip()
            self.clock.tick(60)

    def settings_menu(self):
        pg.display.set_caption("Settings")

        while True:

            # fill with default bg colour
            self.screen.fill(self.settings_bg)

            # DO THINGS HERE

            # get mouse position
            mouse_pos = pg.mouse.get_pos()

            # create buttons
            settings_back = Button(image=None, pos=(100, 50), text_input="Back",
                                   font=self.get_font(self.font, 50), base_color="#171717",
                                   hovering_color="White")

            # NO MORE DOING THINGS AFTER HERE

            # catch all events
            for event in pg.event.get():
                self.handler(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    # change menu screen if click on button
                    if settings_back.checkForInput(mouse_pos):
                        self.fade_out(self.bg)
                        self.main_menu()

            # change colour of button if hovering
            for button in [settings_back]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            # update screen
            pg.display.flip()
            self.clock.tick(60)

    def explore_menu(self):
        pg.display.set_caption("Explore")

        # Load search icon png
        search_icon = pg.image.load("assets/search.png").convert_alpha()
        search_icon = pg.transform.scale(search_icon, (50, 50))
        search_icon_rect = search_icon.get_rect()
        search_icon_rect.center = (self.width * 0.77, self.height * 0.3)
        # search_icon.fill((150, 150, 30))

        while True:

            # fill with default bg colour
            self.screen.fill(self.explore_bg)

            # DO THINGS HERE

            # get mouse position
            mouse_pos = pg.mouse.get_pos()

            # create buttons
            explore_back = Button(image=None, pos=(100, 50), text_input="Back",
                                  font=self.get_font(self.font, 50), base_color="#637dff",
                                  hovering_color="White")

            search_bar = pg.Rect(0, 0, 800, 75)
            search_bar.center = (self.width // 2, self.height * 0.3)
            pg.draw.rect(self.screen, "#aaaaaa", search_bar, border_radius=100)

            # draw search icon
            self.screen.blit(search_icon, search_icon_rect)

            # NO MORE DOING THINGS AFTER HERE

            # catch all events
            for event in pg.event.get():
                self.handler(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    # change menu screen if click on button
                    if explore_back.checkForInput(mouse_pos):
                        self.fade_out(self.bg)
                        self.main_menu()

            # change colour of button if hovering
            for button in [explore_back]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            # update screen
            pg.display.flip()
            self.clock.tick(60)


# button class from https://github.com/baraltech/Menu-System-PyGame/blob/main/button.py
# public use
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


test = Home()
test.main_menu()
