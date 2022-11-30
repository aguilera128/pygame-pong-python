import random
import winsound
import pygame

pygame.init()
pygame.font.init()

# Marcadores
marcador_jugador1 = 0
marcador_jugador2 = 0

# Tipo de letra
myfont = pygame.font.SysFont('Console', 30)

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (105, 105, 105)
color_jugador1 = WHITE
color_jugador2 = WHITE

# Tamaño ventana
screen_size_width = 1200
screen_size_height = 800
screen_size = (screen_size_width, screen_size_height)

# Tamaño jugadores
player_width = 15
player_height = 90

# Tamaño pelota
radio_pelota = 10

def sound():
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 10  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def sound_punto():
    frequency = 500
    duration = 300
    winsound.Beep(frequency, duration)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


# coordenadas y velocidad del jugador 1
player1_x_coor = screen_size_width * 0.05
player1_y_coor = screen_size_height / 2 - (player_height / 2)
player1_y_speed = 0

# coordenadas y velocidad del jugador 2
player2_x_coor = screen_size_width - (screen_size_width * 0.05) - player_width
player2_y_coor = screen_size_height / 2 - (player_height / 2)
player2_y_speed = 0

# Coordenadas y velocidad de la pelota
pelota_x = screen_size_width / 2
pelota_y = screen_size_height / 2

pelota_speed_x = 0
pelota_speed_y = 0

game_over = False

while not game_over: # Mientras game_over sea False se repite el while
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            # Movimento Jugador 1
            if event.key == pygame.K_w and player1_y_coor > 5:
                player1_y_speed = -3
            if event.key == pygame.K_s and player1_y_coor < screen_size_height - 5:
                player1_y_speed = 3
            # Movimiento Jugador 2
            if event.key == pygame.K_UP and player1_y_coor > 5:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN and player1_y_coor < screen_size_height - 5:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # Moviemiento Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            # Movimiento Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

        # Presionar SPACE para empezar la partida
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pelota_speed_x == 0:
                pelota_speed_y = random.choice([-2.5, 2.5])
                pelota_speed_x = random.choice([-2.5, 2.5])

        print(event)

    # Rebote arriba y abajo de la pelota
    if pelota_y > screen_size_height - 10 or pelota_y < 10:
        pelota_speed_y *= -1
        sound()

    # Revisa si la pelota sale del lado derecho o izquierdo y la devuelve a centro
    if pelota_x > screen_size_width or pelota_x < 0:
        pelota_x = screen_size_width / 2
        pelota_y = screen_size_height / 2
        # Si sale de la pantalla, invierte dirección
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    # Incremeto marcador
    if pelota_x > screen_size_width - 5:
        sound_punto()
        marcador_jugador1 += 1
        pelota_x = screen_size_width / 2
        pelota_y = screen_size_height / 2
        pelota_speed_x = 0
        pelota_speed_y = 0
    if pelota_x < 5:
        sound_punto()
        marcador_jugador2 += 1
        pelota_x = screen_size_width / 2
        pelota_y = screen_size_height / 2
        pelota_speed_x = 0
        pelota_speed_y = 0

    # Modifica las coordenadas para dar mov. a los jugadores/pelota.
    player2_y_coor += player2_y_speed
    player1_y_coor += player1_y_speed

    # Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    # Para evitar que los jugadores salgan de la ventana
    if player1_y_coor < 5 or player1_y_coor + player_height > screen_size_height - 5:
        player1_y_speed = 0

    if player2_y_coor < 5 or player2_y_coor + player_height > screen_size_height - 5:
        player2_y_speed = 0

    screen.fill(BLACK)

    # ··· ZONA DE DIBUJO ···
    linea_divisora = pygame.draw.line(screen, GREY, (screen_size_width / 2, 0), (screen_size_width / 2, screen_size_height), 1) # (coor star), (coor end), (width line)
    jugador1 = pygame.draw.rect(screen, color_jugador1, (player1_x_coor, player1_y_coor, player_width, player_height))
    juagodr2 = pygame.draw.rect(screen, color_jugador2, (player2_x_coor, player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, WHITE, (pelota_x, pelota_y), radio_pelota)
    text_marcador = myfont.render(f"{marcador_jugador1}  {marcador_jugador2}", False, WHITE)
    marcador = screen.blit(text_marcador,(screen_size_width / 2 - text_marcador.get_rect().width / 2, 10))

    # Muestra el texto antes de empezar a jugar
    if pelota_speed_y == 0:
        text_star = myfont.render("PRESS SPACE KEY TO PLAY", False, WHITE)
        screen.blit(text_star, (screen_size_width / 2 - text_star.get_rect().width / 2, screen_size_height / 3 - text_star.get_rect().height / 2))

    # Colisiones pelota
    if pelota.colliderect(jugador1):
        pelota_speed_x *= -1
        color_jugador1 = RED
        sound()

    if pelota.colliderect(juagodr2):
        pelota_speed_x *= -1
        color_jugador2 = RED
        sound()

    # Devuelve el jugador al color blanco
    if pelota_x > 100 and pelota_x < (screen_size_width - 100):
        color_jugador1 = WHITE
        color_jugador2 = WHITE

    pygame.display.flip()
    clock.tick(120)

pygame.quit()