
def draw_rhombus(width, height):
    for i in range(height):
        spaces = abs(height // 2 - i)
        stars = width - 2 * spaces

        if stars > 0:
            print(" " * spaces + "*" * stars)


draw_rhombus(7, 7)
