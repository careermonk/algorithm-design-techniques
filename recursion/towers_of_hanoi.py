def move_tower(height,fromTower, toTower, withTower):
    if height >= 1:
        move_tower(height-1,fromTower,withTower,toTower)
        move_disk(fromTower,toTower)
        move_tower(height-1,withTower,toTower,fromTower)

def move_disk(fromTower,toTower):
    print("Moving disk from ",fromTower," to ",toTower)

move_tower(3,"Source","Destination","Auxiliary")
