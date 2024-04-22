import pygame
import math
import random
import subprocess

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Configurar la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Esfera Giratoria con Iconos")

# Definir colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
other_green = (65, 176, 110)  # Color personalizado
purple = (100, 32, 170)  # Color personalizado

# Definir la clase Icono que representa un bloque de color en la esfera
class Icon:
    def __init__(self, color, position):
        self.color = color
        self.position = position

# Función para dibujar una esfera giratoria con iconos
def draw_sphere(screen, center, radius, angle_x, angle_y):
    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar la esfera
    for theta in range(0, 360, 10):
        for phi in range(-80, 80, 10):
            x = radius * math.cos(theta * math.pi / 180) * math.cos(phi * math.pi / 180)
            y = radius * math.sin(phi * math.pi / 180)
            z = radius * math.sin(theta * math.pi / 180) * math.cos(phi * math.pi / 180)
            projected_x = center[0] + x * math.cos(angle_y) + z * math.sin(angle_y)
            projected_y = center[1] + x * math.sin(angle_x) * math.sin(angle_y) + \
                           y * math.cos(angle_x) - z * math.sin(angle_x) * math.cos(angle_y)
            pygame.draw.circle(screen, green, (int(projected_x), int(projected_y)), 1)

    # Actualizar la pantalla
    pygame.display.flip()

# Función para rotar la esfera según el movimiento del ratón
def rotate_sphere(mouse_pos, center, radius):
    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance > radius:
        angle_x = math.asin(dy / distance)
        angle_y = math.asin(dx / distance)
        return angle_x, angle_y
    else:
        return 0, 0

# Generar posiciones aleatorias para los iconos dentro del rango visible de la esfera
def generate_icon_positions(radius, num_icons):
    positions = []
    for _ in range(num_icons):
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(-math.pi / 2, math.pi / 2)
        x = radius * math.cos(theta) * math.cos(phi)
        y = radius * math.sin(phi)
        z = radius * math.sin(theta) * math.cos(phi)
        positions.append((x, y, z))
    return positions

# Define parámetros de la esfera
sphere_center = (screen_width // 2, screen_height // 2)
sphere_radius = min(screen_width, screen_height) // 3

# Crear iconos en la esfera con colores únicos
icon_positions = generate_icon_positions(sphere_radius, 5)
colors = [red, blue, yellow, purple, other_green]  # Lista de colores disponibles para los iconos
random.shuffle(colors)  # Mezclar los colores para garantizar que no se repitan
icons = [Icon(colors[i], (pos[0], pos[1])) for i, pos in enumerate(icon_positions)]

# Variables para rastrear el estado del clic del ratón
mouse_pressed = False
prev_mouse_pos = pygame.mouse.get_pos()

# Bucle principal
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True
            prev_mouse_pos = pygame.mouse.get_pos()
            # Comprueba si se hizo clic en el icono púrpura y ejecuta tu proyecto .exe
            for icon in icons:
                    if icon.position[0] - 5 <= event.pos[0] <= icon.position[0] + 5 and \
                       icon.position[1] - 5 <= event.pos[1] <= icon.position[1] + 5:
                        if icon.color == purple:
                            subprocess.Popen(["python","terminal.py"])
                            break
                        elif icon.color == blue:
                            subprocess.Popen(["python","To_doList.py"])
                            break
                        elif icon.color == yellow:
                            subprocess.Popen(["python","temporizador.py"])
                            break
                        elif icon.color == red:
                            subprocess.Popen(["python","filesystem.py"])
                            break
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pressed = False

    # Rotar la esfera según el movimiento del ratón
    if mouse_pressed:
        mouse_pos = pygame.mouse.get_pos()
        angle_x, angle_y = rotate_sphere(mouse_pos, sphere_center, sphere_radius)
        prev_mouse_pos = mouse_pos
    else:
        mouse_pos = prev_mouse_pos
        angle_x, angle_y = rotate_sphere(mouse_pos, sphere_center, sphere_radius)

    # Dibujar la esfera giratoria
    draw_sphere(screen, sphere_center, sphere_radius, angle_x, angle_y)

    # Dibujar iconos en la esfera
    for icon, pos in zip(icons, icon_positions):
        x, y, z = pos
        rotated_x = x * math.cos(angle_y) + z * math.sin(angle_y)
        rotated_y = -x * math.sin(angle_y) + z * math.cos(angle_y)
        icon.position = (rotated_x + screen_width // 2, rotated_y + screen_height // 2)

    # Dibujar iconos
    for icon in icons:
        pygame.draw.rect(screen, icon.color, (icon.position[0] - 5, icon.position[1] - 5, 10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
