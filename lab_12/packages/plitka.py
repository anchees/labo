def calculate_tile(width, height, length):
    tile_size = 0.3
    area = (width * height * 2) + (length * height * 2)
    num_tiles = area / (tile_size * tile_size)
    cost = num_tiles * 50 
    
    return {"quantity": int(num_tiles), "cost": cost}
