import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1100, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Speed Click")

# Colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 100, 0)
GREY = (128, 128, 128)
BROWN = (165, 42, 42)
INDIGO = (75, 0, 130)
MAROON = (128, 0, 0)

# GOLD = (255, 215, 0)

# Fonts

small_game_font = pygame.font.Font("pixelex.ttf", 25)
game_font = pygame.font.Font("pixelex.ttf", 50)
big_game_font = pygame.font.Font("pixelex.ttf", 75)

# small_game_font = pygame.font.Font("8-BIT WONDER.ttf", 25)
# game_font = pygame.font.Font("8-BIT WONDER.ttf", 50)
# big_game_font = pygame.font.Font("8-BIT WONDER.ttf", 75)

# Holes

hole = pygame.Rect(75, 150, 200, 200)
hole2 = pygame.Rect(0, 0, 180, 180)
hole2.center = hole.center
hole3 = pygame.Rect(325, 150, 200, 200)
hole4 = pygame.Rect(0, 0, 180, 180)
hole4.center = hole3.center
hole5 = pygame.Rect(575, 150, 200, 200)
hole6 = pygame.Rect(0, 0, 180, 180)
hole6.center = hole5.center
hole7 = pygame.Rect(825, 150, 200, 200)
hole8 = pygame.Rect(0, 0, 180, 180)
hole8.center = hole7.center
hole9 = pygame.Rect(75, 450, 200, 200)
hole10 = pygame.Rect(0, 0, 180, 180)
hole10.center = hole9.center
hole11 = pygame.Rect(325, 450, 200, 200)
hole12 = pygame.Rect(0, 0, 180, 180)
hole12.center = hole11.center
hole13 = pygame.Rect(575, 450, 200, 200)
hole14 = pygame.Rect(0, 0, 180, 180)
hole14.center = hole13.center
hole15 = pygame.Rect(825, 450, 200, 200)
hole16 = pygame.Rect(0, 0, 180, 180)
hole16.center = hole15.center
ball = pygame.Rect(0, 0, 50, 50)
ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                            hole9.center, hole11.center, hole13.center, hole15.center))

# Clock

clock = pygame.time.Clock()

# Text

title_text = big_game_font.render(f"Whack A Mole", True, WHITE)
title_text_rect = title_text.get_rect(center=(WIDTH/2, 200))

start_text = game_font.render(f"START", True, WHITE)
start_text_rect = start_text.get_rect(center=(WIDTH/2, 400))

options_text = game_font.render(f"OPTIONS", True, WHITE)
options_text_rect = options_text.get_rect(center=(WIDTH/2, 500))

info_text = game_font.render(f"INFO", True, WHITE)
info_text_rect = info_text.get_rect(center=(WIDTH/2, 600))

levels_text = game_font.render(f"LEVELS", True, WHITE)
levels_text_rect = levels_text.get_rect(center=(WIDTH/2, 400))

practice_text = game_font.render(f"Practice", True, WHITE)
practice_text_rect = practice_text.get_rect(center=(WIDTH / 2, 500))

speed_click_text = game_font.render(f"Speed Click", True, WHITE)
speed_click_text_rect = speed_click_text.get_rect(center=(WIDTH / 2, 600))

return_instructions = small_game_font.render(f"Go Back (BACKSPACE)", True, WHITE)
return_instructions_rect = return_instructions.get_rect(center=(240, HEIGHT - 25))

pause_instructions = small_game_font.render(f"Pause (Spacebar)", True, WHITE)
pause_instructions_rect = pause_instructions.get_rect(center=(WIDTH - 205, HEIGHT - 25))

reset_instructions = small_game_font.render(f"Reset (R)", True, WHITE)
reset_instructions_rect = reset_instructions.get_rect(center=(WIDTH - 205, HEIGHT - 60))

escape_instructions = small_game_font.render(f"Quit (ESC)", True, WHITE)
escape_instructions_rect = escape_instructions.get_rect(center=(240, HEIGHT - 60))

three_pauses_text = small_game_font.render(f"You can only pause 3 times per game", True, WHITE)
three_pauses_text_rect = three_pauses_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))

you_lost_text = game_font.render(f"Game Over You Lose", True, WHITE)
you_lost_text_rect = you_lost_text.get_rect(center=(WIDTH/2, HEIGHT/2))

you_won_text = game_font.render(f"Game Over You Win", True, WHITE)
you_won_text_rect = you_won_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))

click_to_continue_text = small_game_font.render(f"Press Any Key to Continue", True, WHITE)
click_to_continue_text_rect = click_to_continue_text.get_rect(center=(300, 25))

options_title_text = big_game_font.render(f"Options", True, WHITE)
options_title_text_rect = options_title_text.get_rect(center=(WIDTH/2, 200))

colours_title_text = big_game_font.render(f"Colours", True, WHITE)
colours_title_text_rect = colours_title_text.get_rect(center=(WIDTH/2, 100))

ball_colour_text = game_font.render(f"Ball Colour", True, WHITE)
ball_colour_text_rect = ball_colour_text.get_rect(center=(WIDTH/2, 400))

circle_colour_text = game_font.render(f"Circle Colour", True, WHITE)
circle_colour_text_rect = circle_colour_text.get_rect(center=(WIDTH/2, 500))

colour_red_text = game_font.render(f"RED", True, RED)
colour_red_text_rect = colour_red_text.get_rect(center=(WIDTH/2, 200))

colour_green_text = game_font.render(f"GREEN", True, GREEN)
colour_green_text_rect = colour_green_text.get_rect(center=(WIDTH/2, 300))

colour_blue_text = game_font.render(f"BLUE", True, BLUE)
colour_blue_text_rect = colour_blue_text.get_rect(center=(WIDTH/2, 400))

colour_yellow_text = game_font.render(f"YELLOW", True, YELLOW)
colour_yellow_text_rect = colour_yellow_text.get_rect(center=(WIDTH/2, 500))

colour_magenta_text = game_font.render(f"MAGENTA", True, MAGENTA)
colour_magenta_text_rect = colour_magenta_text.get_rect(center=(WIDTH / 2, 600))

colour_cyan_text = game_font.render(f"CYAN", True, CYAN)
colour_cyan_text_rect = colour_cyan_text.get_rect(center=(WIDTH/2, 700))

colour_white_text = game_font.render(f"WHITE", True, WHITE)
colour_white_text_rect = colour_white_text.get_rect(center=(275, 200))

colour_orange_text = game_font.render(f"ORANGE", True, ORANGE)
colour_orange_text_rect = colour_orange_text.get_rect(center=(275, 300))

colour_grey_text = game_font.render(f"GREY", True, GREY)
colour_grey_text_rect = colour_grey_text.get_rect(center=(275, 400))

colour_brown_text = game_font.render(f"BROWN", True, BROWN)
colour_brown_text_rect = colour_brown_text.get_rect(center=(825, 200))

colour_indigo_text = game_font.render(f"INDIGO", True, INDIGO)
colour_indigo_text_rect = colour_indigo_text.get_rect(center=(825, 300))

colour_maroon_text = game_font.render(f"MAROON", True, MAROON)
colour_maroon_text_rect = colour_maroon_text.get_rect(center=(825, 400))

ball_size_title_text = big_game_font.render(f"Ball Size", True, WHITE)
ball_size_title_text_rect = ball_size_title_text.get_rect(center=(WIDTH/2, 100))

ball_size_text = game_font.render(f"BALL SIZE", True, WHITE)
ball_size_text_rect = ball_size_text.get_rect(center=(WIDTH/2, 600))

ball_size_small_text = game_font.render(f"SMALL", True, WHITE)
ball_size_small_text_rect = ball_size_small_text.get_rect(center=(WIDTH/2, 300))

# text(f"SMALL", "medium", WHITE, WIDTH/2, 300)
# text(f"MEDIUM", "medium", WHITE, WIDTH/2, 400)
# text(f"BIG", "medium", WHITE, WIDTH/2, 500)
# text(f"HUGE", "medium", WHITE, WIDTH/2, 600)

ball_size_medium_text = game_font.render(f"MEDIUM", True, WHITE)
ball_size_medium_text_rect = ball_size_medium_text.get_rect(center=(WIDTH/2, 400))

ball_size_big_text = game_font.render(f"BIG", True, WHITE)
ball_size_big_text_rect = ball_size_big_text.get_rect(center=(WIDTH/2, 500))

ball_size_huge_text = game_font.render(f"HUGE", True, WHITE)
ball_size_huge_text_rect = ball_size_huge_text.get_rect(center=(WIDTH/2, 600))

info_title_text = big_game_font.render(f"Info", True, WHITE)
info_title_text_rect = info_title_text.get_rect(center=(WIDTH/2, 200))

rules_text = game_font.render(f"Rules", True, WHITE)
rules_text_rect = rules_text.get_rect(center=(WIDTH/2, 400))

rules_title_text = big_game_font.render(f"Rules", True, WHITE)
rules_title_text_rect = rules_title_text.get_rect(center=(WIDTH/2, 100))

keybinds_text = game_font.render(f"Keybinds", True, WHITE)
keybinds_text_rect = keybinds_text.get_rect(center=(WIDTH/2, 500))

keybinds_title_text = big_game_font.render(f"KEYBINDS", True, WHITE)
keybinds_title_text_rect = keybinds_title_text.get_rect(center=(WIDTH/2, 100))

keybinds_backspace_text = game_font.render(f"Go Back (Backspace)", True, WHITE)
keybinds_backspace_text_rect = keybinds_backspace_text.get_rect(center=(WIDTH/2, 200))

keybinds_pause_text = game_font.render(f"Pause (Spacebar)", True, WHITE)
keybinds_pause_text_rect = keybinds_pause_text.get_rect(center=(WIDTH/2, 300))

keybinds_reset_text = game_font.render(f"Reset (R)", True, WHITE)
keybinds_reset_text_rect = keybinds_reset_text.get_rect(center=(WIDTH/2, 400))

keybinds_escape_text = game_font.render(f"Escape (ESC)", True, WHITE)
keybinds_escape_text_rect = keybinds_escape_text.get_rect(center=(WIDTH/2, 500))

o_text = small_game_font.render(f"o", True, WHITE)
p_text = small_game_font.render(f"p", True, WHITE)
t_text = small_game_font.render(f"t", True, WHITE)
i_text = small_game_font.render(f"i", True, WHITE)
n_text = small_game_font.render(f"n", True, WHITE)
s_text = small_game_font.render(f"s", True, WHITE)

f_text = small_game_font.render(f"f", True, WHITE)

o_text_rect = o_text.get_rect(center=(WIDTH - 25, HEIGHT/2 - 90))
p_text_rect = p_text.get_rect(center=(WIDTH - 25, HEIGHT/2 - 60))
t_text_rect = t_text.get_rect(center=(WIDTH - 25, HEIGHT/2 - 30))
i_text_rect = i_text.get_rect(center=(WIDTH - 25, HEIGHT/2))
o_text_rect2 = o_text.get_rect(center=(WIDTH - 25, HEIGHT/2 + 30))
n_text_rect = n_text.get_rect(center=(WIDTH - 25, HEIGHT/2 + 60))
s_text_rect = s_text.get_rect(center=(WIDTH - 25, HEIGHT/2 + 90))

i2_text_rect = i_text.get_rect(center=(25, HEIGHT/2 - 45))
n2_text_rect = n_text.get_rect(center=(25, HEIGHT/2 - 15))
f2_text_rect = f_text.get_rect(center=(25, HEIGHT/2 + 15))
o2_text_rect = o_text.get_rect(center=(25, HEIGHT/2 + 45))

# Game Variables

score_goal = 0
pause_count = 0
streak = 0
click_counter = 0
i = 30
h = 0
mouse_pos = (0, 0)
speed_test = False
level_1, level_2, level_3, level_4, level_5, level_6 = 0, 0, 0, 0, 0, 0

b = 0
f = False
z = True

BALL_COLOUR = MAGENTA
CIRCLE_COLOUR = CYAN

practice_high_score = 0

speed_click_high_score = 0


# ball spawns in a random hole
# click ball to get points
# clear level by getting points in time
# ball disappears after 1 second
# if you misclick, you lose 5 points


def text(words, size, colour, center_x, center_y):
   if size == "small":
       texts = small_game_font.render(words, True, colour)
   elif size == "medium":
       texts = game_font.render(words, True, colour)
   elif size == "big":
       texts = big_game_font.render(words, True, colour)

   texts_rect = texts.get_rect(center=(center_x, center_y))
   screen.blit(texts, texts_rect)


def practice():
   global i
   global click_counter
   global h
   global BALL_COLOUR
   global speed_test
   global practice_high_score
   cpm = 0

   click_counter = 0
   i = 100
   p = True
   while speed_test:

       global mouse_pos
       mouse_pos = pygame.mouse.get_pos()

       screen.fill(BLACK)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole)
       pygame.draw.ellipse(screen, BLACK, hole2)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole3)
       pygame.draw.ellipse(screen, BLACK, hole4)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole5)
       pygame.draw.ellipse(screen, BLACK, hole6)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole7)
       pygame.draw.ellipse(screen, BLACK, hole8)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole9)
       pygame.draw.ellipse(screen, BLACK, hole10)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole11)
       pygame.draw.ellipse(screen, BLACK, hole12)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole13)
       pygame.draw.ellipse(screen, BLACK, hole14)
       pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole15)
       pygame.draw.ellipse(screen, BLACK, hole16)
       pygame.draw.ellipse(screen, BALL_COLOUR, ball)

       text(f"{click_counter}", "medium", WHITE, WIDTH/2, 50)
       text(f"Score {click_counter}", "small", WHITE, 125, 60)
       text(f"{h}", "small", WHITE, 125, 100)
       text(f"HIGH SCORE {practice_high_score}", "small", WHITE, WIDTH - 150, 100)

       # big_click_counter_text = game_font.render(f"{click_counter}", True, WHITE)
       # big_click_counter_text_rect = big_click_counter_text.get_rect(center=(WIDTH / 2, 50))
       # screen.blit(big_click_counter_text, big_click_counter_text_rect)

       # click_counter_text = small_game_font.render(f"Score {click_counter}", True, WHITE)
       # click_counter_text_rect = click_counter_text.get_rect(center=(125, 60))
       # screen.blit(click_counter_text, click_counter_text_rect)

       # time_text = small_game_font.render(f"{h}", True, WHITE)
       # time_text_rect = time_text.get_rect(center=(125, 100))
       # screen.blit(time_text, time_text_rect)

       # practice_high_score_text = small_game_font.render(f"HIGH SCORE {practice_high_score}", True, WHITE)
       # practice_high_score_text_rect = practice_high_score_text.get_rect(center=(WIDTH - 150, 100))
       # screen.blit(practice_high_score_text, practice_high_score_text_rect)

       screen.blit(return_instructions, return_instructions_rect)

       screen.blit(escape_instructions, escape_instructions_rect)

       pygame.display.update()

       if h < 100:
           cps_text = small_game_font.render(f"CPM {cpm}", True, WHITE)
           cps_text_rect = cps_text.get_rect(center=(WIDTH - 150, 60))
           screen.blit(cps_text, cps_text_rect)
       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
               if event.key == pygame.K_BACKSPACE:
                   game_reset()
                   # menu()
                   speed_test = False
                   i = 30
           if event.type == pygame.MOUSEBUTTONDOWN:
               if ball.right > mouse_pos[0] > ball.left \
                       and ball.top < mouse_pos[1] < ball.bottom:
                   ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center, hole10.center,
                                                hole12.center, hole14.center, hole16.center))
                   click_counter += 1
                   if click_counter > practice_high_score:
                       practice_high_score += 1

       clock.tick(60)
       i -= 1/60
       # h = round(i)
       h = int(i * 10) / 10
       cpm = int(click_counter/(100 - h)*60)
       if cpm > practice_high_score:
           practice_high_score = cpm

       if h == 0:
           while p:
               screen.fill(BLACK)
               text(f"Speed was {(int((click_counter / 100) * 60) * 10)/10}", "small", WHITE, WIDTH/2, 500)
               screen.blit(return_instructions, return_instructions_rect)
               pygame.display.update()
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_ESCAPE:
                           pygame.quit()
                           sys.exit()
                       if event.key == pygame.K_BACKSPACE:
                           p = False
                           i = 100


def speed_click():
   global click_counter
   global h
   global i
   i = 15
   click_counter = 0

   v = True
   while v:
       j = True
       # mouse_pos == pygame.mouse.get_pos()
       screen.fill(BLACK)
       text(f"{click_counter}", "medium", WHITE, WIDTH/2, 50)
       text(f"{h}", "small", WHITE, 125, 100)

       screen.blit(return_instructions, return_instructions_rect)
       screen.blit(escape_instructions, escape_instructions_rect)

       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               click_counter += 1
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_BACKSPACE:
                   click_counter = 0
                   v = False
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()

       clock.tick(60)
       i -= 1 / 60
       h = int(i * 10) / 10
       # h = round(i)

       if h == 0:
           screen.fill(BLACK)
           text(f"Your Speed was {(int(click_counter * 10 / 15))/ 10}",  "small", WHITE, WIDTH/2, 500)
           screen.blit(click_to_continue_text, click_to_continue_text_rect)
           pygame.display.update()
           while j:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
                   if event.type == pygame.KEYDOWN:
                       j = False
                       i = 15
                       click_counter = 0


def menu():
   global speed_test

   run = True
   while run:
       screen.fill(BLACK)
       screen.blit(title_text, title_text_rect)
       screen.blit(levels_text, levels_text_rect)
       screen.blit(practice_text, practice_text_rect)
       screen.blit(speed_click_text, speed_click_text_rect)
       screen.blit(return_instructions, return_instructions_rect)
       screen.blit(escape_instructions, escape_instructions_rect)
       pygame.display.update()

       mouse_pos = pygame.mouse.get_pos()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_BACKSPACE:
                   main_menu()
                   # menu()
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if levels_text_rect.right > mouse_pos[0] > levels_text_rect.left \
                       and levels_text_rect.bottom > mouse_pos[1] > levels_text_rect.top:
                   run = False
               elif practice_text_rect.right > mouse_pos[0] > practice_text_rect.left \
                       and practice_text_rect.bottom > mouse_pos[1] > practice_text_rect.top:
                   speed_test = True
                   practice()
               elif speed_click_text_rect.right > mouse_pos[0] > speed_click_text_rect.left \
                       and speed_click_text_rect.bottom > mouse_pos[1] > speed_click_text_rect.top:
                   speed_click()
               else:
                   continue


def colours(colour, colour_input, colour_center_x, colour_center_y):
   colour_text = game_font.render(f"{colour}", True, colour_input)
   colour_text_rect = colour_text.get_rect(center=(colour_center_x, colour_center_y))
   screen.blit(colour_text, colour_text_rect)
   pygame.display.update()


def options():
   global BALL_COLOUR
   global CIRCLE_COLOUR
   global ball
   global f

   f = True

   while f:
       o = True
       d = True
       x = True

       screen.fill(BLACK)
       screen.blit(options_title_text, options_title_text_rect)
       screen.blit(ball_colour_text, ball_colour_text_rect)
       screen.blit(circle_colour_text, circle_colour_text_rect)
       screen.blit(ball_size_text, ball_size_text_rect)
       screen.blit(return_instructions, return_instructions_rect)
       screen.blit(escape_instructions, escape_instructions_rect)
       pygame.display.update()

       mouse_pos = pygame.mouse.get_pos()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
               if event.key == pygame.K_BACKSPACE:
                   f = False
           if event.type == pygame.MOUSEBUTTONDOWN:
               if ball_colour_text_rect.right > mouse_pos[0] > ball_colour_text_rect.left \
                       and ball_colour_text_rect.bottom > mouse_pos[1] > ball_colour_text_rect.top:
                   screen.fill(BLACK)
                   screen.blit(colours_title_text, colours_title_text_rect)
                   colours("RED", RED, WIDTH / 2, 200)
                   colours("GREEN", GREEN, WIDTH / 2, 300)
                   colours("BLUE", BLUE, WIDTH / 2, 400)
                   colours("YELLOW", YELLOW, WIDTH / 2, 500)
                   colours("MAGENTA", MAGENTA, WIDTH / 2, 600)
                   colours("CYAN", CYAN, WIDTH / 2, 700)
                   colours("WHITE", WHITE, 275, 200)
                   colours("ORANGE", ORANGE, 275, 300)
                   colours("GREY", GREY, 275, 400)
                   colours("BROWN", BROWN, 825, 200)
                   colours("INDIGO", INDIGO, 825, 300)
                   colours("MAROON", MAROON, 825, 400)
                   screen.blit(return_instructions, return_instructions_rect)
                   screen.blit(escape_instructions, escape_instructions_rect)
                   pygame.display.update()

                   # screen.blit(colour_red_text, colour_red_text_rect)
                   # screen.blit(colour_green_text, colour_green_text_rect)
                   # screen.blit(colour_blue_text, colour_blue_text_rect)
                   # screen.blit(colour_yellow_text, colour_yellow_text_rect)
                   # screen.blit(colour_magenta_text, colour_magenta_text_rect)
                   # screen.blit(colour_cyan_text, colour_cyan_text_rect)
                   # screen.blit(colour_white_text, colour_white_text_rect)
                   # screen.blit(colour_orange_text, colour_orange_text_rect)
                   # screen.blit(colour_grey_text, colour_grey_text_rect)
                   # screen.blit(colour_brown_text, colour_brown_text_rect)
                   # screen.blit(colour_indigo_text, colour_indigo_text_rect)
                   # screen.blit(colour_maroon_text, colour_maroon_text_rect)

                   while o:
                       mouse_pos = pygame.mouse.get_pos()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               if event.key == pygame.K_ESCAPE:
                                   pygame.quit()
                                   sys.exit()
                               if event.key == pygame.K_BACKSPACE:
                                   o = False
                           if event.type == pygame.MOUSEBUTTONDOWN:
                               if colour_red_text_rect.right > mouse_pos[0] > \
                                       colour_red_text_rect.left and \
                                       colour_red_text_rect.bottom > \
                                       mouse_pos[1] > colour_red_text_rect.top:
                                   BALL_COLOUR = RED
                               elif colour_green_text_rect.right > mouse_pos[0] > \
                                       colour_green_text_rect.left and \
                                       colour_green_text_rect.bottom > \
                                       mouse_pos[1] > colour_green_text_rect.top:
                                   BALL_COLOUR = GREEN
                               elif colour_blue_text_rect.right > mouse_pos[0] > \
                                       colour_blue_text_rect.left and \
                                       colour_blue_text_rect.bottom > \
                                       mouse_pos[1] > colour_blue_text_rect.top:
                                   BALL_COLOUR = BLUE
                               elif colour_yellow_text_rect.right > mouse_pos[0] > \
                                       colour_yellow_text_rect.left and \
                                       colour_yellow_text_rect.bottom > \
                                       mouse_pos[1] > colour_yellow_text_rect.top:
                                   BALL_COLOUR = YELLOW
                               elif colour_magenta_text_rect.right > mouse_pos[0] > \
                                       colour_magenta_text_rect.left and \
                                       colour_magenta_text_rect.bottom > \
                                       mouse_pos[1] > colour_magenta_text_rect.top:
                                   BALL_COLOUR = MAGENTA
                               elif colour_cyan_text_rect.right > mouse_pos[0] > \
                                       colour_cyan_text_rect.left and \
                                       colour_cyan_text_rect.bottom > \
                                       mouse_pos[1] > colour_cyan_text_rect.top:
                                   BALL_COLOUR = CYAN
                               elif colour_white_text_rect.right > mouse_pos[0] > \
                                       colour_white_text_rect.left and \
                                       colour_white_text_rect.bottom > \
                                       mouse_pos[1] > colour_white_text_rect.top:
                                   BALL_COLOUR = WHITE
                               elif colour_orange_text_rect.right > mouse_pos[0] > \
                                       colour_orange_text_rect.left and \
                                       colour_orange_text_rect.bottom > \
                                       mouse_pos[1] > colour_orange_text_rect.top:
                                   BALL_COLOUR = ORANGE
                               elif colour_grey_text_rect.right > mouse_pos[0] > \
                                       colour_grey_text_rect.left and \
                                       colour_grey_text_rect.bottom > \
                                       mouse_pos[1] > colour_grey_text_rect.top:
                                   BALL_COLOUR = GREY
                               elif colour_brown_text_rect.right > mouse_pos[0] > \
                                       colour_brown_text_rect.left and \
                                       colour_brown_text_rect.bottom > \
                                       mouse_pos[1] > colour_brown_text_rect.top:
                                   BALL_COLOUR = BROWN
                               elif colour_indigo_text_rect.right > mouse_pos[0] > \
                                       colour_indigo_text_rect.left and \
                                       colour_indigo_text_rect.bottom > \
                                       mouse_pos[1] > colour_indigo_text_rect.top:
                                   BALL_COLOUR = INDIGO
                               elif colour_maroon_text_rect.right > mouse_pos[0] > \
                                       colour_maroon_text_rect.left and \
                                       colour_maroon_text_rect.bottom > \
                                       mouse_pos[1] > colour_maroon_text_rect.top:
                                   BALL_COLOUR = MAROON

                               # o = False
               elif circle_colour_text_rect.right > mouse_pos[0] > circle_colour_text_rect.left \
                       and circle_colour_text_rect.bottom > mouse_pos[1] > circle_colour_text_rect.top:
                   screen.fill(BLACK)
                   screen.blit(colours_title_text, colours_title_text_rect)
                   colours("RED", RED, WIDTH / 2, 200)
                   colours("GREEN", GREEN, WIDTH / 2, 300)
                   colours("BLUE", BLUE, WIDTH / 2, 400)
                   colours("YELLOW", YELLOW, WIDTH / 2, 500)
                   colours("MAGENTA", MAGENTA, WIDTH / 2, 600)
                   colours("CYAN", CYAN, WIDTH / 2, 700)
                   colours("WHITE", WHITE, 275, 200)
                   colours("ORANGE", ORANGE, 275, 300)
                   colours("GREY", GREY, 275, 400)
                   colours("BROWN", BROWN, 825, 200)
                   colours("INDIGO", INDIGO, 825, 300)
                   colours("MAROON", MAROON, 825, 400)
                   screen.blit(return_instructions, return_instructions_rect)
                   screen.blit(escape_instructions, escape_instructions_rect)
                   pygame.display.update()

                   # colours("RED", WIDTH / 2, 200)
                   # colours("GREEN", WIDTH / 2, 300)
                   # colours("BLUE", WIDTH / 2, 400)
                   # colours("YELLOW", WIDTH / 2, 500)
                   # colours("MAGENTA", WIDTH / 2, 600)
                   # colours("CYAN", WIDTH / 2, 700)
                   # colours("WHITE", 275, 200)
                   # colours("ORANGE", 275, 300)
                   # colours("GREY", 275, 400)
                   # colours("BROWN", 825, 200)
                   # colours("MAROON", 825, 400)
                   # colours("INDIGO", 825, 300)

                   while d:
                       mouse_pos = pygame.mouse.get_pos()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               if event.key == pygame.K_ESCAPE:
                                   pygame.quit()
                                   sys.exit()
                               if event.key == pygame.K_BACKSPACE:
                                   d = False
                           if event.type == pygame.MOUSEBUTTONDOWN:
                               if colour_red_text_rect.right > mouse_pos[0] > \
                                       colour_red_text_rect.left and \
                                       colour_red_text_rect.bottom > \
                                       mouse_pos[1] > colour_red_text_rect.top:
                                   CIRCLE_COLOUR = RED
                               elif colour_green_text_rect.right > mouse_pos[0] > \
                                       colour_green_text_rect.left and \
                                       colour_green_text_rect.bottom > \
                                       mouse_pos[1] > colour_green_text_rect.top:
                                   CIRCLE_COLOUR = GREEN
                               elif colour_blue_text_rect.right > mouse_pos[0] > \
                                       colour_blue_text_rect.left and \
                                       colour_blue_text_rect.bottom > \
                                       mouse_pos[1] > colour_blue_text_rect.top:
                                   CIRCLE_COLOUR = BLUE
                               elif colour_yellow_text_rect.right > mouse_pos[0] > \
                                       colour_yellow_text_rect.left and \
                                       colour_yellow_text_rect.bottom > \
                                       mouse_pos[1] > colour_yellow_text_rect.top:
                                   CIRCLE_COLOUR = YELLOW
                               elif colour_magenta_text_rect.right > mouse_pos[0] > \
                                       colour_magenta_text_rect.left and \
                                       colour_magenta_text_rect.bottom > \
                                       mouse_pos[1] > colour_magenta_text_rect.top:
                                   CIRCLE_COLOUR = MAGENTA
                               elif colour_cyan_text_rect.right > mouse_pos[0] > \
                                       colour_cyan_text_rect.left and \
                                       colour_cyan_text_rect.bottom > \
                                       mouse_pos[1] > colour_cyan_text_rect.top:
                                   CIRCLE_COLOUR = CYAN
                               elif colour_white_text_rect.right > mouse_pos[0] > \
                                       colour_white_text_rect.left and \
                                       colour_white_text_rect.bottom > \
                                       mouse_pos[1] > colour_white_text_rect.top:
                                   CIRCLE_COLOUR = WHITE
                               elif colour_orange_text_rect.right > mouse_pos[0] > \
                                       colour_orange_text_rect.left and \
                                       colour_orange_text_rect.bottom > \
                                       mouse_pos[1] > colour_orange_text_rect.top:
                                   CIRCLE_COLOUR = ORANGE
                               elif colour_grey_text_rect.right > mouse_pos[0] > \
                                       colour_grey_text_rect.left and \
                                       colour_grey_text_rect.bottom > \
                                       mouse_pos[1] > colour_grey_text_rect.top:
                                   CIRCLE_COLOUR = GREY
                               elif colour_brown_text_rect.right > mouse_pos[0] > \
                                       colour_brown_text_rect.left and \
                                       colour_brown_text_rect.bottom > \
                                       mouse_pos[1] > colour_brown_text_rect.top:
                                   CIRCLE_COLOUR = BROWN
                               elif colour_indigo_text_rect.right > mouse_pos[0] > \
                                       colour_indigo_text_rect.left and \
                                       colour_indigo_text_rect.bottom > \
                                       mouse_pos[1] > colour_indigo_text_rect.top:
                                   CIRCLE_COLOUR = INDIGO
                               elif colour_maroon_text_rect.right > mouse_pos[0] > \
                                       colour_maroon_text_rect.left and \
                                       colour_maroon_text_rect.bottom > \
                                       mouse_pos[1] > colour_maroon_text_rect.top:
                                   CIRCLE_COLOUR = MAROON
               if ball_size_text_rect.right > mouse_pos[0] > ball_size_text_rect.left \
                       and ball_size_text_rect.bottom > mouse_pos[1] > ball_size_text_rect.top:
                   screen.fill(BLACK)
                   screen.blit(ball_size_title_text, ball_size_title_text_rect)
                   screen.blit(ball_size_small_text, ball_size_small_text_rect)
                   screen.blit(ball_size_medium_text, ball_size_medium_text_rect)
                   screen.blit(ball_size_big_text, ball_size_big_text_rect)
                   screen.blit(ball_size_huge_text , ball_size_huge_text_rect)
                   screen.blit(return_instructions, return_instructions_rect)
                   screen.blit(escape_instructions, escape_instructions_rect)
                   pygame.display.update()
                   while x:
                       mouse_pos = pygame.mouse.get_pos()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               if event.key == pygame.K_ESCAPE:
                                   pygame.quit()
                                   sys.exit()
                               if event.key == pygame.K_BACKSPACE:
                                   x = False
                           if event.type == pygame.MOUSEBUTTONDOWN:
                               if ball_size_small_text_rect.right > mouse_pos[0] > \
                                       ball_size_small_text_rect.left \
                                       and ball_size_small_text_rect.bottom > \
                                       mouse_pos[1] > ball_size_small_text_rect.top:
                                   ball = pygame.Rect(0, 0, 50, 50)
                               if ball_size_medium_text_rect.right > mouse_pos[0] > \
                                       ball_size_medium_text_rect.left \
                                       and ball_size_medium_text_rect.bottom > \
                                       mouse_pos[1] > ball_size_medium_text_rect.top:
                                   ball = pygame.Rect(0, 0, 75, 75)
                               if ball_size_big_text_rect.right > mouse_pos[0] > \
                                       ball_size_big_text_rect.left \
                                       and ball_size_big_text_rect.bottom > \
                                       mouse_pos[1] > ball_size_big_text_rect.top:
                                   ball = pygame.Rect(0, 0, 100, 100)
                               if ball_size_huge_text_rect.right > mouse_pos[0] > \
                                       ball_size_huge_text_rect.left \
                                       and ball_size_huge_text_rect.bottom > \
                                       mouse_pos[1] > ball_size_huge_text_rect.top:
                                   ball = pygame.Rect(0, 0, 180, 180)


def info():

   t = True

   while t:
       k = True
       n = True

       screen.fill(BLACK)
       screen.blit(info_title_text, info_title_text_rect)
       screen.blit(rules_text, rules_text_rect)
       screen.blit(keybinds_text, keybinds_text_rect)
       screen.blit(return_instructions, return_instructions_rect)
       screen.blit(escape_instructions, escape_instructions_rect)
       pygame.display.update()

       mouse_pos = pygame.mouse.get_pos()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
               if event.key == pygame.K_BACKSPACE:
                   t = False
           if event.type == pygame.MOUSEBUTTONDOWN:
               if rules_text_rect.right > mouse_pos[0] > rules_text_rect.left\
                       and rules_text_rect.bottom > mouse_pos[1] > rules_text_rect.top:
                   screen.fill(BLACK)
                   screen.blit(rules_title_text, rules_title_text_rect)
                   text("Ball appears at random position", "small", WHITE, WIDTH/2, 200)
                   text("Click Ball to get points", "small", WHITE, WIDTH/2, 250)
                   text("Ball disappears after 1 second", "small", WHITE, WIDTH/2, 300)
                   text("Clear level by getting points in time", "small", WHITE, WIDTH/2, 350)
                   text("Misclick = -5 Points", "small", WHITE, WIDTH/2, 400)
                   screen.blit(return_instructions, return_instructions_rect)
                   screen.blit(escape_instructions, escape_instructions_rect)
                   pygame.display.update()
                   while n:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               if event.key == pygame.K_ESCAPE:
                                   pygame.quit()
                                   sys.exit()
                               if event.key == pygame.K_BACKSPACE:
                                   n = False
               if keybinds_text_rect.right > mouse_pos[0] > keybinds_text_rect.left\
                       and keybinds_text_rect.bottom > mouse_pos[1] > keybinds_text_rect.top:
                   screen.fill(BLACK)
                   screen.blit(keybinds_title_text, keybinds_title_text_rect)
                   screen.blit(keybinds_backspace_text, keybinds_backspace_text_rect)
                   screen.blit(keybinds_pause_text, keybinds_pause_text_rect)
                   screen.blit(keybinds_reset_text, keybinds_reset_text_rect)
                   screen.blit(keybinds_escape_text, keybinds_escape_text_rect)
                   screen.blit(return_instructions, return_instructions_rect)
                   screen.blit(escape_instructions, escape_instructions_rect)
                   pygame.display.update()
                   while k:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               if event.key == pygame.K_ESCAPE:
                                   pygame.quit()
                                   sys.exit()
                               if event.key == pygame.K_BACKSPACE:
                                   k = False


def main_menu():

   global f
   global BALL_COLOUR
   global CIRCLE_COLOUR
   global ball

   m = True
   while m:

       screen.fill(BLACK)
       screen.blit(title_text, title_text_rect)
       screen.blit(start_text, start_text_rect)
       screen.blit(options_text, options_text_rect)
       screen.blit(info_text, info_text_rect)
       pygame.display.update()
       mouse_pos = pygame.mouse.get_pos()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if start_text_rect.right > mouse_pos[0] > start_text_rect.left \
                       and start_text_rect.bottom > mouse_pos[1] > start_text_rect.top:
                   m = False
                   break
               elif options_text_rect.right > mouse_pos[0] > options_text_rect.left \
                       and options_text_rect.bottom > mouse_pos[1] > options_text_rect.top:
                   options()

               elif info_text_rect.right > mouse_pos[0] > info_text_rect.left \
                       and info_text_rect.bottom > mouse_pos[1] > info_text_rect.top:
                   info()


def main_screen():
   global mouse_pos
   global BALL_COLOUR

   mouse_pos = pygame.mouse.get_pos()

   screen.fill(BLACK)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole)
   pygame.draw.ellipse(screen, BLACK, hole2)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole3)
   pygame.draw.ellipse(screen, BLACK, hole4)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole5)
   pygame.draw.ellipse(screen, BLACK, hole6)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole7)
   pygame.draw.ellipse(screen, BLACK, hole8)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole9)
   pygame.draw.ellipse(screen, BLACK, hole10)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole11)
   pygame.draw.ellipse(screen, BLACK, hole12)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole13)
   pygame.draw.ellipse(screen, BLACK, hole14)
   pygame.draw.ellipse(screen, CIRCLE_COLOUR, hole15)
   pygame.draw.ellipse(screen, BLACK, hole16)

   pygame.draw.ellipse(screen, BALL_COLOUR, ball)

   text(f"Score {click_counter}", "small", WHITE, 125, 60)
   text(f"{click_counter}", "medium", WHITE, WIDTH / 2, 50)
   text(f"{h}", "small", WHITE, 125, 100)
   text(f"Goal {score_goal}", "small", WHITE, WIDTH - 150, 60)
   text(f"Streak {streak}", "small", WHITE, WIDTH - 150, 100)

   # click_counter_text = small_game_font.render(f"Score {click_counter}", True, WHITE)
   # click_counter_text_rect = click_counter_text.get_rect(center=(125, 60))
   # screen.blit(click_counter_text, click_counter_text_rect)

   # big_click_counter_text = game_font.render(f"{click_counter}", True, WHITE)
   # big_click_counter_text_rect = big_click_counter_text.get_rect(center=(WIDTH/2, 50))
   # screen.blit(big_click_counter_text, big_click_counter_text_rect)

   # time_text = small_game_font.render(f"{h}", True, WHITE)
   # time_text_rect = time_text.get_rect(center=(125, 100))
   # screen.blit(time_text, time_text_rect)

   # score_goal_text = small_game_font.render(f"GOAL {score_goal}", True, WHITE)
   # score_goal_text_rect = score_goal_text.get_rect(center=(WIDTH - 150, 60))
   # screen.blit(score_goal_text, score_goal_text_rect)

   screen.blit(pause_instructions, pause_instructions_rect)

   # streak_text = small_game_font.render(f"Streak {streak}", True, WHITE)
   # streak_text_rect = streak_text.get_rect(center=(WIDTH - 150, 100))
   # screen.blit(streak_text, streak_text_rect)

   screen.blit(return_instructions, return_instructions_rect)

   screen.blit(reset_instructions, reset_instructions_rect)

   screen.blit(escape_instructions, escape_instructions_rect)

   # screen.blit(o_text, o_text_rect)
   # screen.blit(p_text, p_text_rect)
   # screen.blit(t_text, t_text_rect)
   # screen.blit(i_text, i_text_rect)
   # screen.blit(o_text, o_text_rect2)
   # screen.blit(n_text, n_text_rect)
   # screen.blit(s_text, s_text_rect)

   # screen.blit(i_text, i2_text_rect)
   # screen.blit(n_text, n2_text_rect)
   # screen.blit(f_text, f2_text_rect)
   # screen.blit(o_text, o2_text_rect)

   pygame.display.update()


def game_reset():
   global click_counter
   global streak
   global score_goal
   global pause_count
   global b
   click_counter = 0
   streak = 0
   pause_count = 0
   b = 0


def pause():
   global pause_count
   pause_count += 1
   paused = True
   while paused:
       mouse_pos = pygame.mouse.get_pos()
       paused_text = game_font.render(f"PAUSED", True, WHITE)
       paused_text_rect = paused_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
       screen.blit(paused_text, paused_text_rect)
       screen.blit(o_text, o_text_rect)
       screen.blit(p_text, p_text_rect)
       screen.blit(t_text, t_text_rect)
       screen.blit(i_text, i_text_rect)
       screen.blit(o_text, o_text_rect2)
       screen.blit(n_text, n_text_rect)
       screen.blit(s_text, s_text_rect)

       screen.blit(i_text, i2_text_rect)
       screen.blit(n_text, n2_text_rect)
       screen.blit(f_text, f2_text_rect)
       screen.blit(o_text, o2_text_rect)
       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
               if event.key == pygame.K_SPACE:
                   paused = False
           if event.type == pygame.MOUSEBUTTONDOWN:
               if o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                       and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                   info()
                   screen.fill(BLACK)
                   main_screen()

               elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                       and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                   options()
                   screen.fill(BLACK)
                   main_screen()


def levels_true():
   global level_1, level_2, level_3, level_4, level_5, level_6
   level_1, level_2, level_3, level_4, level_5 = True, True, True, True, True
   level_6 = True


def levels_false():
   global level_1, level_2, level_3, level_4, level_5, level_6
   level_1, level_2, level_3, level_4, level_5 = False, False, False, False, False
   level_6 = False


def levels(level_number):
   level_text = game_font.render(f"LEVEL {level_number}", True, WHITE)
   level_text_rect = level_text.get_rect(center=(WIDTH/2, 300))
   screen.blit(level_text, level_text_rect)


def levels_info(points, seconds):
   level_info_text = small_game_font.render(f"{points} Points in {seconds} Seconds", True, WHITE)
   level_info_text_rect = level_info_text.get_rect(center=(WIDTH/2, 400))
   screen.blit(level_info_text, level_info_text_rect)


def main_loop():

   global z
   global i
   global click_counter
   global h
   global score_goal
   global streak
   global pause_count
   global level_1, level_2, level_3, level_4, level_5, level_6
   global b

   pause_count = 0
   level_1 = True

   u = True
   while u:
       levels_true()

       streak = 0
      
       if level_1:
           i = 30
           b = 0
           screen.fill(BLACK)
           levels(1)
           levels_info(25, 30)

           pygame.display.update()
           pygame.time.delay(2000)

           click_counter = 0

           score_goal = 25

           ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                        hole9.center, hole11.center, hole13.center, hole15.center))

       while level_1:

           main_screen()

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   if event.key == pygame.K_r:
                       game_reset()
                       i = 30
                   if event.key == pygame.K_BACKSPACE:
                       game_reset()
                       menu()
                       level_1 = True
                       i = 30
                       levels_false()
                   if event.key == pygame.K_SPACE:
                       if pause_count < 3:
                           pause()
                       else:
                           screen.blit(three_pauses_text, three_pauses_text_rect)
                           pygame.display.update()
                           pygame.time.delay(250)
                           if i >= 1/4:
                               i -= 1/4
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                    if ball.right > mouse_pos[0] > ball.left and ball.top < mouse_pos[1] < ball.bottom:
                        ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center,
                                                        hole10.center, hole12.center, hole14.center, hole16.center))
                        click_counter += 1
                        b = 0
                        # elif o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                        # and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                        # info()
                        # elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                        # and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                        # options()
                    elif click_counter <= 5:
                        click_counter = 0
                    elif click_counter > 5:
                        click_counter -= 5

           clock.tick(60)
           i -= 1/60
           h = int(i * 10) / 10
           # h = round(i)
           b += 1/60

           if b >= 1:
               ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                            hole9.center, hole11.center, hole13.center, hole15.center))
               b = 0

           if h == 0 or click_counter == 25:
               if click_counter < 25:
                   screen.fill(BLACK)
                   screen.blit(you_lost_text, you_lost_text_rect)
                   screen.blit(click_to_continue_text, click_to_continue_text_rect)
                   pygame.display.update()
                   while z:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               z = False
                   z = True
                   screen.fill(BLACK)
                   levels(1)
                   levels_info(25, 30)
                   pygame.display.update()
                   pygame.time.delay(2000)
                   game_reset()
                   i = 30
                   streak = 0
               else:
                   streak += 1
                   e = True
                   while e:
                       screen.fill(BLACK)
                       screen.blit(you_won_text, you_won_text_rect)
                       screen.blit(click_to_continue_text, click_to_continue_text_rect)
                       pygame.display.update()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               e = False
                           else:
                               continue

                   level_1 = False

       pause_count = 0

       if level_2:
           i = 30

           screen.fill(BLACK)
           levels(2)
           levels_info(30, 30)
           pygame.display.update()
           pygame.time.delay(2000)
           click_counter = 0

           score_goal = 30

           ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                        hole9.center, hole11.center, hole13.center, hole15.center))

       while level_2:

           main_screen()

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   if event.key == pygame.K_r:
                       game_reset()
                       i = 30
                   if event.key == pygame.K_BACKSPACE:
                       game_reset()
                       menu()
                       levels_false()
                       i = 30
                       levels_false()
                   if event.key == pygame.K_SPACE:
                       if pause_count < 3:
                           pause()
                       else:
                           screen.blit(three_pauses_text, three_pauses_text_rect)
                           pygame.display.update()
                           pygame.time.delay(250)
                           if i >= 1 / 4:
                               i -= 1 / 4

               if event.type == pygame.MOUSEBUTTONDOWN:
                   if ball.right > mouse_pos[0] > ball.left and ball.top < mouse_pos[1] < ball.bottom:
                       ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center,
                                                    hole10.center, hole12.center, hole14.center, hole16.center))
                       click_counter += 1
                       b = 0
                   # elif o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                       # and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                       # info()
                   # elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                       # and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                       # options()
                   elif click_counter <= 5:
                       click_counter = 0
                   elif click_counter > 5:
                       click_counter -= 5
           clock.tick(60)
           i -= 1 / 60
           h = int(i * 10) / 10
           # h = round(i)
           b += 1 / 60

           if b >= 1:
               ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                            hole9.center, hole11.center, hole13.center, hole15.center))
               b = 0

           if h == 0 or click_counter == 30:
               if click_counter < 30:
                   streak = 0
                   screen.fill(BLACK)
                   screen.blit(you_lost_text, you_lost_text_rect)
                   screen.blit(click_to_continue_text, click_to_continue_text_rect)
                   pygame.display.update()
                   while z:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               z = False
                   z = True
                   screen.fill(BLACK)
                   levels(2)
                   levels_info(30, 30)
                   pygame.display.update()
                   pygame.time.delay(2000)
                   game_reset()
                   i = 30
               else:
                   streak += 1
                   e = True
                   while e:
                       screen.fill(BLACK)
                       screen.blit(you_won_text, you_won_text_rect)
                       screen.blit(click_to_continue_text, click_to_continue_text_rect)
                       pygame.display.update()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               e = False
                           else:
                               continue

                   level_2 = False

       pause_count = 0

       if level_3:
           i = 10

           screen.fill(BLACK)
           levels(3)
           levels_info(10, 10)
           pygame.display.update()
           pygame.time.delay(2000)
           click_counter = 0

           score_goal = 10

           ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                        hole9.center, hole11.center, hole13.center, hole15.center))

       while level_3:
           main_screen()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   if event.key == pygame.K_r:
                       game_reset()
                       i = 10
                   if event.key == pygame.K_BACKSPACE:
                       game_reset()
                       menu()
                       i = 30
                       levels_false()
                   if event.key == pygame.K_SPACE:
                       if pause_count < 3:
                           pause()
                       else:
                           screen.blit(three_pauses_text, three_pauses_text_rect)
                           pygame.display.update()
                           pygame.time.delay(250)
                           if i >= 1 / 4:
                               i -= 1 / 4
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if ball.right > mouse_pos[0] > ball.left and ball.top < mouse_pos[1] < ball.bottom:
                       ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center,
                                                    hole10.center, hole12.center, hole14.center, hole16.center))
                       click_counter += 1
                       b = 0
                       # elif o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                       # and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                       # info()
                       # elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                       # and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                       # options()
                   elif click_counter <= 5:
                       click_counter = 0
                   elif click_counter > 5:
                       click_counter -= 5

           clock.tick(60)
           i -= 1 / 60
           h = int(i * 10) / 10
           # h = round(i)
           b += 1 / 60

           if b >= 1:
               ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                            hole9.center, hole11.center, hole13.center, hole15.center))
               b = 0

           if h == 0 or click_counter == 10:
               if click_counter < 10:
                   streak = 0
                   screen.fill(BLACK)
                   screen.blit(you_lost_text, you_lost_text_rect)
                   screen.blit(click_to_continue_text, click_to_continue_text_rect)
                   pygame.display.update()
                   while z:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               z = False
                   z = True
                   screen.fill(BLACK)
                   levels(3)
                   levels_info(10, 10)
                   pygame.display.update()
                   pygame.time.delay(2000)
                   game_reset()
                   i = 10
               else:
                   streak += 1
                   e = True
                   while e:
                       screen.fill(BLACK)
                       screen.blit(you_won_text, you_won_text_rect)
                       screen.blit(click_to_continue_text, click_to_continue_text_rect)
                       pygame.display.update()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               e = False
                           else:
                               continue
                   level_3 = False

       pause_count = 0

       if level_4:
           i = 30

           screen.fill(BLACK)
           levels(4)
           levels_info(35, 30)
           pygame.display.update()
           pygame.time.delay(2000)
           click_counter = 0

           score_goal = 35

           ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                        hole9.center, hole11.center, hole13.center, hole15.center))

       while level_4:
           main_screen()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   if event.key == pygame.K_r:
                       game_reset()
                       i = 30
                   if event.key == pygame.K_BACKSPACE:
                       game_reset()
                       menu()
                       level_1 = True
                       i = 30
                       levels_false()
                   if event.key == pygame.K_SPACE:
                       if pause_count < 3:
                           pause()
                       else:
                           screen.blit(three_pauses_text, three_pauses_text_rect)
                           pygame.display.update()
                           pygame.time.delay(250)
                           if i >= 1 / 4:
                               i -= 1 / 4
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if ball.right > mouse_pos[0] > ball.left and ball.top < mouse_pos[1] < ball.bottom:
                       ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center,
                                                    hole10.center, hole12.center, hole14.center, hole16.center))
                       click_counter += 1
                       b = 0
                       # elif o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                       # and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                       # info()
                       # elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                       # and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                       # options()
                   elif click_counter <= 5:
                       click_counter = 0
                   elif click_counter > 5:
                       click_counter -= 5

           clock.tick(60)
           i -= 1 / 60
           h = int(i * 10) / 10
           # h = round(i)
           b += 1 / 60

           if b >= 1:
               ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                            hole9.center, hole11.center, hole13.center, hole15.center))
               b = 0

           if h == 0 or click_counter == 35:
               if click_counter < 35:
                   streak = 0
                   screen.fill(BLACK)
                   screen.blit(you_lost_text, you_lost_text_rect)
                   screen.blit(click_to_continue_text, click_to_continue_text_rect)
                   pygame.display.update()
                   while z:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               z = False
                   z = True
                   screen.fill(BLACK)
                   levels(4)
                   levels_info(35, 30)
                   pygame.display.update()
                   pygame.time.delay(2000)
                   game_reset()
                   i = 30
               else:
                   streak += 1
                   e = True
                   while e:
                       screen.fill(BLACK)
                       screen.blit(you_won_text, you_won_text_rect)
                       screen.blit(click_to_continue_text, click_to_continue_text_rect)
                       pygame.display.update()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               e = False
                           else:
                               continue
                   level_4 = False

       pause_count = 0

       if level_5:
           i = 15

           screen.fill(BLACK)
           levels(5)
           levels_info(20, 15)
           pygame.display.update()
           pygame.time.delay(2000)
           click_counter = 0

           score_goal = 20

           ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                        hole9.center, hole11.center, hole13.center, hole15.center))

       while level_5:
           main_screen()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   if event.key == pygame.K_r:
                       game_reset()
                       i = 15
                   if event.key == pygame.K_BACKSPACE:
                       game_reset()
                       menu()
                       level_1 = True
                       i = 30
                       levels_false()
                   if event.key == pygame.K_SPACE:
                       if pause_count < 3:
                           pause()
                       else:
                           screen.blit(three_pauses_text, three_pauses_text_rect)
                           pygame.display.update()
                           pygame.time.delay(250)
                           if i >= 1 / 4:
                               i -= 1 / 4
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if ball.right > mouse_pos[0] > ball.left and ball.top < mouse_pos[1] < ball.bottom:
                       ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center,
                                                    hole10.center, hole12.center, hole14.center, hole16.center))
                       click_counter += 1
                       b = 0
                       # elif o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                       # and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                       # info()
                       # elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                       # and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                       # options()
                   elif click_counter <= 5:
                       click_counter = 0
                   elif click_counter > 5:
                       click_counter -= 5

           clock.tick(60)
           i -= 1 / 60
           h = int(i * 10) / 10
           # h = round(i)
           b += 1 / 60

           if b >= 1:
               ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                            hole9.center, hole11.center, hole13.center, hole15.center))
               b = 0

           if h == 0 or click_counter == 20:
               if click_counter < 20:
                   streak = 0
                   screen.fill(BLACK)
                   screen.blit(you_lost_text, you_lost_text_rect)
                   screen.blit(click_to_continue_text, click_to_continue_text_rect)
                   pygame.display.update()
                   while z:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               z = False
                   z = True
                   screen.fill(BLACK)
                   levels(5)
                   levels_info(20, 15)
                   pygame.display.update()
                   pygame.time.delay(2000)
                   game_reset()
                   i = 15
               else:
                   streak += 1
                   e = True
                   while e:
                       screen.fill(BLACK)
                       screen.blit(you_won_text, you_won_text_rect)
                       screen.blit(click_to_continue_text, click_to_continue_text_rect)
                       pygame.display.update()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               e = False
                           else:
                               continue
                   level_5 = False

       if level_6:
           i = 10
           b = 0
           screen.fill(BLACK)
           levels(6)
           levels_info(15, 10)

           pygame.display.update()
           pygame.time.delay(2000)

           click_counter = 0

           score_goal = 15

           ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                        hole9.center, hole11.center, hole13.center, hole15.center))

       pause_count = 0

       while level_6:

           main_screen()

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   if event.key == pygame.K_r:
                       game_reset()
                       i = 10
                   if event.key == pygame.K_BACKSPACE:
                       game_reset()
                       menu()
                       level_1 = True
                       i = 30
                       levels_false()
                   if event.key == pygame.K_SPACE:
                       if pause_count < 3:
                           pause()
                       else:
                           screen.blit(three_pauses_text, three_pauses_text_rect)
                           pygame.display.update()
                           pygame.time.delay(250)
                           if i >= 1/4:
                               i -= 1/4
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if ball.right > mouse_pos[0] > ball.left and ball.top < mouse_pos[1] < ball.bottom:
                       ball.center = random.choice((hole2.center, hole4.center, hole6.center, hole8.center,
                                                    hole10.center, hole12.center, hole14.center, hole16.center))
                       click_counter += 1
                       b = 0
                       # elif o2_text_rect.right > mouse_pos[0] > o2_text_rect.left \
                       # and o2_text_rect.bottom > mouse_pos[1] > i2_text_rect.top:
                       # info()
                       # elif o_text_rect.right > mouse_pos[0] > o_text_rect.left \
                       # and s_text_rect.bottom > mouse_pos[1] > o_text_rect.top:
                       # options()
                   elif click_counter <= 5:
                       click_counter = 0
                   elif click_counter > 5:
                       click_counter -= 5

           clock.tick(60)
           i -= 1/60
           h = int(i * 10) / 10
           # h = round(i)
           b += 1/60

           if b >= 1:
               ball.center = random.choice((hole.center, hole3.center, hole5.center, hole7.center,
                                            hole9.center, hole11.center, hole13.center, hole15.center))
               b = 0

           if h == 0 or click_counter == 15:
               if click_counter < 15:
                   screen.fill(BLACK)
                   screen.blit(you_lost_text, you_lost_text_rect)
                   screen.blit(click_to_continue_text, click_to_continue_text_rect)
                   pygame.display.update()
                   while z:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               z = False
                   z = True
                   screen.fill(BLACK)
                   levels(6)
                   levels_info(15, 10)
                   pygame.display.update()
                   pygame.time.delay(2000)
                   game_reset()
                   i = 10
                   streak = 0
               else:
                   streak += 1
                   e = True
                   while e:
                       screen.fill(BLACK)
                       screen.blit(you_won_text, you_won_text_rect)
                       screen.blit(click_to_continue_text, click_to_continue_text_rect)
                       pygame.display.update()
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               pygame.quit()
                               sys.exit()
                           if event.type == pygame.KEYDOWN:
                               e = False
                           else:
                               continue

                   level_6 = False


main_menu()

menu()

main_loop()

