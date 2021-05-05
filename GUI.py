import pygame
import string
import sys
from hangman import *
from tkinter import *
from tkinter.filedialog import *
pygame.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption('HANGMAN')


#constants
color1 = (214, 195, 191)
grey = (122, 117, 116)
black = (41, 36, 35)
dark_blue = (10, 7, 61)
dark_green = (0, 28, 9)
red = (179, 36, 7)
white = (255,255,255)
green =(38, 156, 14)
normal_red = (255, 0, 0)
letter_font = pygame.font.SysFont(None, 80)
title_font = pygame.font.SysFont(None, 200)
option_font = pygame.font.SysFont(None, 60)
guessed_font = pygame.font.SysFont(None, 70)
guess_font = pygame.font.SysFont(None, 100)
left_font = pygame.font.SysFont(None, 180)
git_font = pygame.font.SysFont(None, 30)

def word_enter():
    showError = False
    def start(text):
        if all([True if i in Hangman.allowed else False for i in text]):
            root.destroy()
            main_window(text)
        else:
            label2 = Label(root, text="Choose a different word")
            label2.pack(anchor='center')
        
    root = Tk()
    root.title("Word Select")
    root.geometry("150x100")
    root.resizable(False, False)

    label = Label(root, text="Type a Word/Phrase")
    entry = Entry(root)
    button = Button(root, text="Start",command = lambda: start(entry.get()))


    label.pack(anchor='center')
    entry.pack(anchor='center')
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
    textarr = [(60, 215), (160, 215), (260, 215), (360, 215), (460, 215), (560, 215), (60, 315), (160, 315), (260, 315),
               (360, 315), (460, 315), (560, 315), (60, 415), (160, 415), (260, 415), (360, 415), (460, 415),
               (560, 415), (60, 515), (160, 515), (260, 515), (360, 515), (460, 515), (560, 515), (60, 615), (160, 615)]
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

    while running:
        if len(game.guess_wrong) >= 10:
            running = False
            loss_screen(game)

        if game.check_win():
            running = False
            win_screen(game)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for index, bound in enumerate(bounds):
                    if mouse[0] >= bound[0] and mouse[0] <= bound[2] and mouse[1] >= bound[1] and mouse[1] <= bound[3]:
                        game.checkLetter(alphabet[index])

                        greyarr.pop(index)
                        color1arr.pop(index)
                        textarr.pop(index)
                        bounds.pop(index)
                        alphabet = alphabet[:index] + alphabet[index + 1:]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        curLetters = list(alphabet)

        screen.fill(white)

        try:
            image = pygame.image.load(f'assets/{len(game.guess_wrong)}.png')
            screen.blit(image, (800,100))
        except FileNotFoundError:
            pass


        toGuess = guess_font.render("".join(i + " " for i in game.dis), True, black)
        screen.blit(toGuess, (20, 20))

        left = left_font.render(str(10 - len(game.guess_wrong)), True, black)
        screen.blit(left, (1120, 580))

        guessesLeft = letter_font.render("Guesses Left:", True, black)
        screen.blit(guessesLeft, (740, 620))

        for i in range(len(greyarr)):
            pygame.draw.rect(screen, grey, greyarr[i])
            pygame.draw.rect(screen, color1, color1arr[i])
            img = letter_font.render(curLetters[0], True, black)

            curLetters.pop(0)
            screen.blit(img, textarr[i])

        pygame.display.update()


def dictSelect():
    root =Tk()
    root.withdraw()
    name = dict_name=askopenfilename()
    root.destroy()
    main_window(dict_name=name)


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
        screen.fill(white)

        img = left_font.render("You Lost!", True, normal_red)
        screen.blit(img, (350,50))

        img = guessed_font.render(f"The word was: {game_obj.string}", True, black)
        screen.blit(img, (300, 230))
        back = pygame.Rect(530, 380, 155, 85)
        pygame.draw.rect(screen, black, back)
        pygame.draw.rect(screen, white, [535, 385, 145, 75])
        img = guess_font.render("Exit", True, black)
        screen.blit(img, (540, 390))


        image = pygame.image.load('assets/10.png')
        screen.blit(image, (800,250))
        
        img = option_font.render("R.I.P.", True, normal_red)
        screen.blit(img, (900, 550))

        pygame.display.update()



def win_screen(game_obj):
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
        screen.fill(white)

        img = left_font.render("You Won!", True, green)
        screen.blit(img, (350, 50))
        img = guessed_font.render(f"You guessed \"{game_obj.string}\" correctly", True, black)
        screen.blit(img, (150, 230))
        back = pygame.Rect(530, 380, 155, 85)
        pygame.draw.rect(screen, black, back)
        pygame.draw.rect(screen, white, [535, 385, 145, 75])
        img = guess_font.render("Exit", True, black)
        screen.blit(img, (540, 390))

        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
        screen.fill(white)

        pygame.display.update()


def main_menu():
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()

        screen.fill((255, 255, 255))

        img = git_font.render("Made By: github.com/AlexDavicenko", True, black)
        screen.blit(img, (10, 690))
        img = title_font.render('HANGMAN', True, red)

        screen.blit(img, (250, 20))


        optionSP = pygame.Rect(300,200,320,180)
        optionMP = pygame.Rect(660,200,320,180)
        optionSPd = pygame.draw.rect(screen, black, optionSP)
        optionMPd = pygame.draw.rect(screen, black, optionMP)
        optionSPw = pygame.draw.rect(screen, white, [305, 205, 310, 170])
        optionMPw = pygame.draw.rect(screen, white, [665, 205, 310, 170])

        SPcaption = option_font.render("Singleplayer", True, black)
        screen.blit(SPcaption, (330, 255))
        MPcaption = option_font.render("Multiplayer", True, black)
        screen.blit(MPcaption, (710, 255))

        if optionSP.collidepoint((mx,my)):
            optionSPw = pygame.draw.rect(screen, black, [305, 205, 310, 170])
            SPcaption = option_font.render("Singleplayer", True, white)
            screen.blit(SPcaption, (330, 255))
        if optionMP.collidepoint((mx,my)):
            optionMPw = pygame.draw.rect(screen, black, [665, 205, 310, 170])
            MPcaption = option_font.render("Multiplayer", True, white)
            screen.blit(MPcaption, (710, 255))





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if optionSP.collidepoint((mx, my)):
                    dictSelect()
                if optionMP.collidepoint((mx, my)):
                    word_enter()

        pygame.display.update()
main_menu()