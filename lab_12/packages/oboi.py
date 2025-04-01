def calculate_wallpaper(width, height, length):
    roll_width = 1.06 
    roll_length = 10   
    
    perimeter = 2 * (width + length)
    num_strips = perimeter // roll_width
    num_rolls = (num_strips * height) // roll_length
    cost = num_rolls * 500  
    
    return {"quantity": int(num_rolls), "cost": cost}