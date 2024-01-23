import pygame
import sys
from main1 import Button

pygame.init()
WIDTH, HEIGHT = 1000, 1010
MAX_FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
pygame.display.set_caption('No more light')
icon = pygame.image.load("imagesN/icon.jpeg")
pygame.display.set_icon(icon)
main_background = pygame.image.load("imagesN/spaceship/spaceshipforward2.jpeg")
left_background = pygame.image.load("imagesN/spaceship/spaceshipleft.jpg")
right_background = pygame.image.load("imagesN/spaceship/spaceshipright.jpg")
screen_background = pygame.image.load("imagesN/screen.png")
frame = pygame.image.load("imagesN/frame.png")
ghost = pygame.image.load("imagesN/prizrakmus-fotor-bg-remover-2023122404949.png")
main_background_red = pygame.image.load("imagesN/spaceship/red_alert.png")
krik = pygame.mixer.Sound('dfSounds/sumasshedshiy-krik.mp3')
trevoga = [pygame.image.load("imagesN/spaceship/spaceshipforward2.jpeg"),
           pygame.image.load("imagesN/spaceship/red_alert.png")]
trevoga_index = 0
ventil_animation = [pygame.image.load("imagesN/ventil1.png"), pygame.image.load("imagesN/ventil2.png"),
                    pygame.image.load("imagesN/ventil3.png"), pygame.image.load("imagesN/ventil4.png")]
ventil_index = 0
alert = pygame.mixer.Sound("dfSounds/sound_alert.mp3")
esh = False
sound_alert = False
ventil_triger = False
window = True
window_left = False
window_ventil = False
window_right = False
window_error = False
ghost_triger = False
ghost_triger2 = False
zero = 0
clock = pygame.time.Clock()


def main_view():
    global trevoga, screen, trevoga_index, window, window_left, window_right, zero
    left_string_button = Button(0, HEIGHT / 2, 165, 117, "", "imagesN/stringleft.png",
                                "imagesN/stringleft1.png", "dfSounds/chair.mp3")
    right_string_button = Button(830, HEIGHT / 2, 165, 117, "", "imagesN/stringright.png",
                                 "imagesN/stringright1.png", "dfSounds/chair.mp3")
    text = [
        "Приветствую вас, капитан. Я бортовой компьютер корабля Ray, серии AITD. Для продолжения полëта требуется проверить основные системы корабля.   "
        , "Повернитесь налево"]
    running = True
    while running:

        screen.fill((255, 255, 255))

        screen.blit(trevoga[trevoga_index], (0, 0))
        screen.blit(frame, (-30, 0))

        if esh:
            if trevoga_index == 1:
                trevoga_index = 0
            else:
                trevoga_index += 1
        if sound_alert:
            alert.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == left_string_button:
                print('Кнопка левого экрана была нажата')
                zero += 1
                window_left = True
                left_view()
            if event.type == pygame.USEREVENT and event.button == right_string_button:
                print('Кнопка правого экрана была нажата')
                window_right = True
                right_view()

            for btn in [left_string_button, right_string_button]:
                btn.handle_event(event)
        for btn in [left_string_button, right_string_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
        if window:
            show_transparent_rectangle(text)
            window = False
        clock.tick(8)


def left_view():
    global ventil_triger, ventil_index, ventil_animation, window_left, window_ventil, ghost_triger, zero, krik
    text = [
        "Перед вами модуль управления системой жизнеобеспечения корабля. Вентиль посередине отвечает за управление подачей кислорода."
        " Проверьте его исправность. после взаимодействия с вентилем"]
    text2 = [' Системы жизнеобеспечения исправны. Теперь повернитесь к навигационной панели в правой части кабины.']
    right_string_button = Button(830, HEIGHT / 2, 165, 117, "", "imagesN/stringright.png",
                                 "imagesN/stringright1.png", "dfSounds/chair.mp3")
    ventil_button = Button(375, 400, 150, 149, "", "imagesN/ventil1.png",
                           "", "")
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(left_background, (0, 0))
        screen.blit(ventil_animation[ventil_index], (300, 325))
        screen.blit(frame, (-30, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if ventil_triger:
                if ventil_index == 3:
                    ventil_index = 0
                    ventil_triger = False
                else:
                    ventil_index += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == right_string_button:
                running = False
            if event.type == pygame.USEREVENT and event.button == ventil_button:
                ventil_triger = True
                window_ventil = True
                if window_ventil:
                    show_transparent_rectangle(text2)
                    window_ventil = False

                print("Ты нажал на вентель")

            for btn in [right_string_button, ventil_button]:
                btn.handle_event(event)

        for btn in [right_string_button, ventil_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        if window_left and zero == 1:
            show_transparent_rectangle(text)
            window_left = False

        if zero == 2:
            screen.blit(ghost, (300, 300))
            krik.play(1)

        pygame.display.flip()
        clock.tick(2)


def right_view():
    global window_right, window_error
    text = ["Это навигационная панель. Здесь вы сможете выбирать пункты назначения в вашем путешествии. ",
            'На этом экране вы будете указывать точку маршрута и корабль начнет движение к ней. Куда хотите отправиться, капитан? Выбирайте скорее...']
    text2 = [" Выбран пункт назначения. Подготовка к прыжку. 3 2 1 Запуск двиг!№""!!; Прыжок невозможен. ",
             "Внимание: обнаружено нарушение работы подачи кислорода, проверьте главный вентиль. ",
             "Внимание: обнаружено нар?:%;шение работы подачи кисло(??:да, прове%?;()те главный вентиль."]
    left_string_button = Button(0, HEIGHT / 2, 165, 117, "", "imagesN/stringleft.png",
                                "imagesN/stringleft1.png", "dfSounds/chair.mp3")
    screen_button = Button(525, 437, 305, 99, "", "imagesN/screens.png", "imagesN/screens.png", "")
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(right_background, (0, 0))
        screen.blit(frame, (-30, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_view()

            if event.type == pygame.USEREVENT and event.button == left_string_button:
                main_view()
            if event.type == pygame.USEREVENT and event.button == screen_button:
                screen_view()
                print("ты нажал на экран")

            for btn in [left_string_button, screen_button]:
                btn.handle_event(event)

        for btn in [left_string_button, screen_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        if window_right:
            show_transparent_rectangle(text)
            window_right = False
        if window_error:
            show_transparent_rectangle(text2)
            window_error = False

        pygame.display.flip()


def screen_view():
    global trevoga, screen, trevoga_index, esh, sound_alert, window_error, ghost_triger
    screen_button = Button(535, 365, 90, 90, "", "imagesN/planet.png", "", "")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(screen_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_error = True
                    right_view()
            if event.type == pygame.USEREVENT and event.button == screen_button:
                esh = True
                sound_alert = True
                ghost_triger = True
                print("ты нажал на планету")

            for btn in [screen_button]:
                btn.handle_event(event)

        for btn in [screen_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()


import pygame

pygame.init()


def show_transparent_rectangle(text):
    global screen

    running = True
    current_text_index = 0
    current_char_index = 0
    font = pygame.font.Font(None, 17)
    line_spacing = 10  # Расстояние между строчками текста
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if current_text_index >= len(text) - 1:
                        running = False
                    else:
                        current_text_index += 1
                        current_char_index = 0

        # Отрисовка полупрозрачного прямоугольника
        rectangle_width = 276
        rectangle_height = 150
        rectangle = pygame.Surface((rectangle_width, rectangle_height), pygame.SRCALPHA)
        rectangle.fill((0, 0, 0, 128))
        screen.blit(rectangle, (75, 70))

        # Отрисовка текста
        current_text = text[current_text_index]
        if current_text_index >= len(text):
            running = False
        current_line = current_text[:current_char_index]
        lines = []
        words = current_line.split(" ")
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[
                0] <= rectangle_width - 20:  # Проверка, что текст помещается в ширину прямоугольника
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)

        if current_char_index < len(current_text):
            current_char_index += 1

        y = screen.get_height() - rectangle_height + 10 - 790
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (80, y))
            y += font.get_height() + line_spacing

        pygame.display.flip()
        clock.tick(10)  # Уменьшаем скорость появления текста


if __name__ == "__main__":
    main_view()
