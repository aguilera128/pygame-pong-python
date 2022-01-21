import pygame
pygame.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen_size_width = 800
screen_size_height = 600
screen_size = (screen_size_width, screen_size_height)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - (player_height / 2)
player1_y_speed = 0

# coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - (player_height / 2)
player2_y_speed = 0

# Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 1.5
pelota_speed_y = 1.5

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w and player1_y_coor > 5:
                player1_y_speed = -3
            if event.key == pygame.K_s and player1_y_coor < 595:
                player1_y_speed = 3
            # Jugador 2
            if event.key == pygame.K_UP and player1_y_coor > 5:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN and player1_y_coor < 595:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

        print(event)

    if pelota_y > 590 or pelota_y <10:
        pelota_speed_y *= -1

    # Revisa si la pelota sale del lado derecho o izquierdo y la devuelve a centro
    if pelota_x > 800 or pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        # Si sale de la pantall, invierte dirección
        pelota_speed_x *= -1
        pelota_speed_y *= -1
    
    # Modifica las coordenadas para dar mov. a los jugadores/pelota.    
    player2_y_coor += player2_y_speed
    player1_y_coor += player1_y_speed

    # Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    # Para evitar que los jugadores salgan de la ventana
    if player1_y_coor < 5 or player1_y_coor + player_height > 600 - 5:
        player1_y_speed = 0        

    if player2_y_coor < 5 or player2_y_coor + player_height > 600 -5:
        player2_y_speed = 0

    screen.fill(BLACK)

    # ··· ZONA DE DIBUJO ···
    linea_divisora = pygame.draw.line(screen, WHITE, (400, 0), (400, 600), 1) # (coor star), (coor end), (width line)
    jugador1 = pygame.draw.rect(screen, WHITE, (player1_x_coor, player1_y_coor, player_width, player_height))
    juagodr2 = pygame.draw.rect(screen, WHITE, (player2_x_coor, player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, WHITE, (pelota_x, pelota_y), 10)

    # Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(juagodr2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(120)

pygame.quit()