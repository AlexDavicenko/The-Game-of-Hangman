import pygame
import string
import sys
from hangman import *
from tkinter import *
from tkinter.filedialog import *
import webbrowser

LIGHT_GREY = (214, 195, 191)
GREY = (122, 117, 116)
LIGHT_BLACK = (41, 36, 35)
DARK_BLUE = (10, 7, 61)
DARK_GREEN = (0, 28, 9)
ORANGE_RED = (179, 36, 7)
WHITE = (255, 255, 255)
GREEN =(38, 156, 14)
RED = (255, 0, 0)
BG_COLOUR = (213, 221, 232)
BLACK = (0,0,0)
pygame.init()
FONT_80 = pygame.font.SysFont(None, 80)
FONT_200 = pygame.font.SysFont(None, 200)
FONT_60 = pygame.font.SysFont(None, 60)
FONT_70 = pygame.font.SysFont(None, 70)
FONT_100 = pygame.font.SysFont(None, 100)
FONT_180 = pygame.font.SysFont(None, 180)
FONT_30 = pygame.font.SysFont(None, 30)


screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption('HANGMAN')


def word_enter():
    showError = False
    def start(text):
        if len(text) >60:

            label2.config(text="Too long")
            label2.pack(anchor='center')
            return False
        if all([True if i in Hangman.allowed else False for i in text]) and any([True if i in string.ascii_letters else False for i in text]):
            root.destroy()
            main_window(text)
        else:
            label2.config(text="Choose a different word")
            label2.pack(anchor='center')
        
    root = Tk()
    root.title("Word Select")
    root.geometry("150x100")
    root.resizable(False, False)

    label = Label(root, text="Type a Word/Phrase")
    label2 = Label(root)
    entry = Entry(root)
    button = Button(root, text="Start",command = lambda: start(entry.get()))


    label.pack(anchor='n')
    entry.pack(anchor='n')
    button.pack(anchor='center')
    root.mainloop()


def main_window(text=None, dict_name = None):
    greyarr = [[40, 200, 80, 80], [140, 200, 80, 80], [240, 200, 80, 80], [340, 200, 80, 80], [440, 200, 80, 80],
               [540, 200, 80, 80], [40, 300, 80, 80], [140, 300, 80, 80], [240, 300, 80, 80], [340, 300, 80, 80],
               [440, 300, 80, 80], [540, 300, 80, 80], [40, 400, 80, 80], [140, 400, 80, 80], [240, 400, 80, 80],
               [340, 400, 80, 80], [440, 400, 80, 80], [540, 400, 80, 80], [40, 500, 80, 80], [140, 500, 80, 80],
               [240, 500, 80, 80], [340, 500, 80, 80], [440, 500, 80, 80], [540, 500, 80, 80], [40, 600, 80, 80],
               [140, 600, 80, 80]]
    color1arr = [[45, 205, 70, 70], [145, 205, 70, 70], [245, 205, 70, 70], [345, 205, 70, 70], [445, 205, 70, 70],
                 [545, 205, 70, 70], [45, 305, 70, 70], [145, 305, 70, 70], [245, 305, 70, 70], [345, 305, 70, 70],
                 [445, 305, 70, 70], [545, 305, 70, 70], [45, 405, 70, 70], [145, 405, 70, 70], [245, 405, 70, 70],
                 [345, 405, 70, 70], [445, 405, 70, 70], [545, 405, 70, 70], [45, 505, 70, 70], [145, 505, 70, 70],
                 [245, 505, 70, 70], [345, 505, 70, 70], [445, 505, 70, 70], [545, 505, 70, 70], [45, 605, 70, 70],
                 [145, 605, 70, 70]]
    textarr = [(60, 215), (160, 215), (260, 215), (360, 215), (460, 215), (560, 215), (60, 315), (160, 315), (270, 315),
               (360, 315), (460, 315), (560, 315), (60, 415), (160, 415), (260, 415), (360, 415), (460, 415),
               (560, 415), (60, 515), (160, 515), (260, 515), (360, 515), (455, 515), (560, 515), (60, 615), (164, 615)]
    bounds = [[40, 200, 120, 280], [140, 200, 220, 280], [240, 200, 320, 280], [340, 200, 420, 280],
              [440, 200, 520, 280], [540, 200, 620, 280], [40, 300, 120, 380], [140, 300, 220, 380],
              [240, 300, 320, 380], [340, 300, 420, 380], [440, 300, 520, 380], [540, 300, 620, 380],
              [40, 400, 120, 480], [140, 400, 220, 480], [240, 400, 320, 480], [340, 400, 420, 480],
              [440, 400, 520, 480], [540, 400, 620, 480], [40, 500, 120, 580], [140, 500, 220, 580],
              [240, 500, 320, 580], [340, 500, 420, 580], [440, 500, 520, 580], [540, 500, 620, 580],
              [40, 600, 120, 680], [140, 600, 220, 680]]

    alphabet = string.ascii_uppercase
    running = True
    if text:
        game = Hangman(string=text)
    else:
        game = Hangman(dictionary=dict_name)
    hint_used = False
    while running:
        mx, my = pygame.mouse.get_pos()

        if len(game.guess_wrong) >= 10:
            running = False
            loss_screen(game)

        if game.check_win():
            running = False
            win_screen(game)


        curLetters = list(alphabet)

        screen.fill(BG_COLOUR)

        try:
            image = pygame.image.load(f'assets/{len(game.guess_wrong)}.png')
            screen.blit(image, (800,100))
        except FileNotFoundError:
            pass


        if len(game.dis) <=30:
            toGuess = FONT_70.render("".join(i + " " for i in game.dis), True, LIGHT_BLACK)
            screen.blit(toGuess, (20, 20))
        elif len(game.dis) >30 and len(game.dis) <=60:
            if game.string[30]!=" " and game.string[29]!=" ":
                msg = "".join(i + " " for i in game.dis[:30])+"-"
            else:
                msg = "".join(i + " " for i in game.dis[:30])
            toGuess = FONT_70.render(msg, True, LIGHT_BLACK)
            screen.blit(toGuess, (20, 20))

            msg = "".join(i + " " for i in game.dis[30:])
            toGuess = FONT_70.render(msg, True, LIGHT_BLACK)
            screen.blit(toGuess, (20, 100))

        left = FONT_180.render(str(10 - len(game.guess_wrong)), True, LIGHT_BLACK)
        screen.blit(left, (1120, 580))

        guessesLeft = FONT_80.render("Guesses Left:", True, LIGHT_BLACK)
        screen.blit(guessesLeft, (740, 620))

        for i in range(len(greyarr)):
            pygame.draw.rect(screen, GREY, greyarr[i])
            pygame.draw.rect(screen, LIGHT_GREY, color1arr[i])
            img = FONT_80.render(curLetters[0], True, LIGHT_BLACK)

            curLetters.pop(0)
            screen.blit(img, textarr[i])


        if not hint_used:
            hint = pygame.Rect([450,600,160,80])
            pygame.draw.rect(screen, GREY, hint)
            pygame.draw.rect(screen, LIGHT_GREY, [455,605,150,70])
            img = FONT_70.render("HINT", True, BLACK)
            screen.blit(img, (470,615))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if hint.collidepoint((mx,my)) and not hint_used:
                    hint_used = True
                    index = alphabet.find(game.hint())
                    greyarr.pop(index)
                    color1arr.pop(index)
                    textarr.pop(index)
                    bounds.pop(index)
                    alphabet = alphabet[:index] + alphabet[index + 1:]

                for index, bound in enumerate(bounds):
                    if mx >= bound[0] and mx <= bound[2] and my >= bound[1] and my <= bound[3]:
                        game.checkLetter(alphabet[index])

                        greyarr.pop(index)
                        color1arr.pop(index)
                        textarr.pop(index)
                        bounds.pop(index)
                        alphabet = alphabet[:index] + alphabet[index + 1:]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


def dictSelect():
    root =Tk()
    root.withdraw()
    name = dict_name=askopenfilename()
    root.destroy()
    if name and name != "()":
        main_window(dict_name=name)
    else:
        main_menu()


def loss_screen(game_obj):

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint((mx, my)):
                    running = False
                    main_menu()
        screen.fill(BG_COLOUR)

        img = FONT_180.render("You Lost!", True, RED)
        screen.blit(img, (350,50))

        text = "The word was:"
        img = FONT_70.render(text, True, LIGHT_BLACK)
        location = img.get_rect(center=screen.get_rect().center)
        location.move_ip(0, -150)
        screen.blit(img, location)


        text = game_obj.string
        if len(text) <=30:
            img = FONT_70.render(text, True, LIGHT_BLACK)
            location = img.get_rect(center=screen.get_rect().center)
            location.move_ip(0, -100)
            screen.blit(img, location)

        elif len(text) >30 and len(text) <=60:
            if text[30]!=" " and text[29]!=" ":
                img = FONT_70.render(text[:30]+'-', True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -100)
                screen.blit(img, location)

                img = FONT_70.render(text[30:], True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -30)
                screen.blit(img, location)
            else:
                img = FONT_70.render(text[:30], True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -100)
                screen.blit(img, location)

                img = FONT_70.render(text[30:], True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -30)
                screen.blit(img, location)

        back = pygame.Rect(0, 0, 300, 130)
        back.center = (640, 550)
        front = pygame.Rect(0, 0, 290, 120)
        front.center = (640, 550)

        pygame.draw.rect(screen, LIGHT_BLACK, back)
        pygame.draw.rect(screen, BG_COLOUR, front)
        ToMenu = FONT_100.render("To Menu", True, LIGHT_BLACK)
        TMlocation = ToMenu.get_rect(center=screen.get_rect().center)
        TMlocation.move_ip(0, 190)
        screen.blit(ToMenu, TMlocation)

        if back.collidepoint((mx, my)):
            pygame.draw.rect(screen, LIGHT_BLACK, front)
            ToMenu = FONT_100.render("To Menu", True, WHITE)
            TMlocation = ToMenu.get_rect(center=screen.get_rect().center)
            TMlocation.move_ip(0, 190)
            screen.blit(ToMenu, TMlocation)



        image = pygame.image.load('assets/10.png')
        screen.blit(image, (900,350))
        
        img = FONT_60.render("R.I.P.", True, RED)
        screen.blit(img, (1030, 665))

        pygame.display.update()



def win_screen(game_obj):
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()


        screen.fill(BG_COLOUR)

        img = FONT_180.render("You Won!", True, GREEN)
        screen.blit(img, (350, 50))

        img = FONT_70.render("Well done for guessing:", True, LIGHT_BLACK)
        location = img.get_rect(center=screen.get_rect().center)
        location.move_ip(0, -150)
        screen.blit(img, location)

        text = game_obj.string
        if len(text) <= 30:
            img = FONT_70.render(text, True, LIGHT_BLACK)
            location = img.get_rect(center=screen.get_rect().center)
            location.move_ip(0, -80)
            screen.blit(img, location)

        elif len(text) > 30 and len(text) <= 60:
            if text[30] != " " and text[29] != " ":
                img = FONT_70.render(text[:30] + '-', True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -80)
                screen.blit(img, location)

                img = FONT_70.render(text[30:], True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -30)
                screen.blit(img, location)
            else:
                img = FONT_70.render(text[:30], True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -80)
                screen.blit(img, location)

                img = FONT_70.render(text[30:], True, LIGHT_BLACK)
                location = img.get_rect(center=screen.get_rect().center)
                location.move_ip(0, -30)
                screen.blit(img, location)


        back = pygame.Rect(0, 0, 300, 130)
        back.center = (640, 550)
        front = pygame.Rect(0, 0, 290, 120)
        front.center = (640, 550)

        pygame.draw.rect(screen, LIGHT_BLACK, back)
        pygame.draw.rect(screen, BG_COLOUR, front)
        ToMenu = FONT_100.render("To Menu", True, LIGHT_BLACK)
        TMlocation = ToMenu.get_rect(center=screen.get_rect().center)
        TMlocation.move_ip(0, 190)
        screen.blit(ToMenu, TMlocation)

        if back.collidepoint((mx,my)):
            pygame.draw.rect(screen, LIGHT_BLACK, front)
            ToMenu = FONT_100.render("To Menu", True, WHITE)
            TMlocation = ToMenu.get_rect(center = screen.get_rect().center)
            TMlocation.move_ip(0,190)
            screen.blit(ToMenu, TMlocation)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint((mx, my)):
                    running = False
                    main_menu()
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
        screen.fill(BG_COLOUR)

        pygame.display.update()


def pull_words():
    pass


def main_menu():
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()

        screen.fill(BG_COLOUR)

        gitlink = FONT_30.render("Made By: github.com/AlexDavicenko", True, LIGHT_BLACK)
        gitlinkRect = gitlink.get_rect()
        gitlinkRect.move_ip(10, 690)
        screen.blit(gitlink, (10, 690))

        title = FONT_200.render('HANGMAN', True, ORANGE_RED)
        titleRect = title.get_rect()
        titleRect.move_ip(250, 20)
        if titleRect.collidepoint((mx,my)):
            title = FONT_200.render('HANGMAN', True, RED)
        screen.blit(title, (250, 20))

        optionSP = pygame.Rect(0,0,320,150)
        optionMP = pygame.Rect(0,0,320,150)
        optionAD = pygame.Rect(0,0,320,150)

        optionSPw = pygame.Rect(0,0,310,140)
        optionMPw = pygame.Rect(0,0,310,140)
        optionADw = pygame.Rect(0,0,310,140)

        optionSP.center = (640,240)
        optionMP.center = (640,420)
        optionAD.center = (640,600)
        optionSPw.center = (640,240)
        optionMPw.center = (640,420)
        optionADw.center = (640,600)

        pygame.draw.rect(screen, LIGHT_BLACK, optionSP)
        pygame.draw.rect(screen, LIGHT_BLACK, optionMP)
        pygame.draw.rect(screen, LIGHT_BLACK, optionAD)
        pygame.draw.rect(screen, BG_COLOUR, optionSPw)
        pygame.draw.rect(screen, BG_COLOUR, optionMPw)
        pygame.draw.rect(screen, BG_COLOUR, optionADw)





        SPcaption = FONT_60.render("Singleplayer", True, LIGHT_BLACK)
        SPlocation = SPcaption.get_rect(center = screen.get_rect().center)
        SPlocation.move_ip(0,-120)
        screen.blit(SPcaption, SPlocation)

        MPcaption = FONT_60.render("Multiplayer", True, LIGHT_BLACK)
        MPlocation = MPcaption.get_rect(center = screen.get_rect().center)
        MPlocation.move_ip(0,60)
        screen.blit(MPcaption, MPlocation)

        ADcaption = FONT_60.render("Add Dictionary", True, LIGHT_BLACK)
        ADlocation = ADcaption.get_rect(center=screen.get_rect().center)
        ADlocation.move_ip(0, 240)
        screen.blit(ADcaption, ADlocation)


        if optionSP.collidepoint((mx,my)):
            pygame.draw.rect(screen, LIGHT_BLACK, optionSPw)
            SPcaption = FONT_60.render("Singleplayer", True, WHITE)
            SPlocation = SPcaption.get_rect(center = screen.get_rect().center)
            SPlocation.move_ip(0,-120)
            screen.blit(SPcaption, SPlocation)
            


        if optionMP.collidepoint((mx,my)):
            pygame.draw.rect(screen, LIGHT_BLACK, optionMPw)
            MPcaption = FONT_60.render("Multiplayer", True, WHITE)
            MPlocation = MPcaption.get_rect(center = screen.get_rect().center)
            MPlocation.move_ip(0,60)
            screen.blit(MPcaption, MPlocation)

        if optionAD.collidepoint((mx,my)):
            pygame.draw.rect(screen, LIGHT_BLACK, optionADw)
            ADcaption = FONT_60.render("Add Dictionary", True, WHITE)
            ADlocation = ADcaption.get_rect(center = screen.get_rect().center)
            ADlocation.move_ip(0,240)
            screen.blit(ADcaption, ADlocation)



        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if optionSP.collidepoint((mx, my)):
                    dictSelect()
                if optionMP.collidepoint((mx, my)):
                    word_enter()
                if optionAD.collidepoint((mx, my)):
                    pull_words()
                if gitlinkRect.collidepoint((mx, my)):
                    webbrowser.open('http://github.com/AlexDavicenko')

        pygame.display.update()
main_menu()