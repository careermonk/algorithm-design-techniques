from collections import namedtuple
from itertools import permutations

box = namedtuple("Box", "height depth width")

def create_rotation(given_boxs):
    for current_box in given_boxs:
        for (height, depth, width) in permutations((current_box.height, current_box.depth, current_box.width)):
            if depth >= width:
                yield box(height, depth, width)

def sort_by_decreasing_base_area(rotations):
    return sorted(rotations, key=lambda box: box.depth * box.width, reverse=True)

def can_stack(box1, box2):
    return box1.depth < box2.depth and box1.width < box2.width

def tallest_box_stack(boxs):
    #create boxes and sort them with base area in decreasing order 
    boxes = sort_by_decreasing_base_area([rotation for rotation in create_rotation(boxs)])
    num_boxes = len(boxes)
    T = [rotation.height for rotation in boxes]
    R = [i for i in range(num_boxes)]

    for i in range(1, num_boxes):
        for j in range(0, i):
            if can_stack(boxes[i], boxes[j]):
                stacked_height = T[j] + boxes[i].height
                if stacked_height > T[i]:
                    T[i] = stacked_height
                    R[i] = j

    max_height = max(T)
    start_index = T.index(max_height)

    # Prints the boxs which were stored in R list.
    while True:
        print boxes[start_index]
        next_index = R[start_index]
        if next_index == start_index:
            break
        start_index = next_index

    return max_height


b1 = box(3, 2, 5)
b2 = box(1, 2, 4)
#b3 = box(7, 8, 3)
print tallest_box_stack([b1, b2])
#print tallest_box_stack([b1, b2, b3])

# Reference: Mission-Peace
