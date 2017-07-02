def move_tower(numberOfDisks,fromTower, toTower, withTower):
    if numberOfDisks >= 1:
        move_tower(numberOfDisks-1,fromTower,withTower,toTower)
        move_disk(fromTower,toTower)
        move_tower(numberOfDisks-1,withTower,toTower,fromTower)

def move_disk(fromTower,toTower):
    print("Moving disk from ",fromTower," to ",toTower)

move_tower(3,"Source","Destination","Auxiliary")
