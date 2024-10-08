def calculate_pyramid_height(number_of_blocks):
    height = 0
    total = 0
    while total + (height + 1) <= number_of_blocks:
        height += 1
        total = height + total
    return height
