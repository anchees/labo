def calculate_laminate(width, length):
    plank_area = 0.2  
    room_area = width * length
    num_planks = room_area / plank_area
    cost = num_planks * 300  
    
    return {"quantity": int(num_planks), "cost": cost}