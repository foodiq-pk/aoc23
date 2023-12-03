from typing import Any
import numpy as np

class EnginePart:
    def __init__(self, number: int, location: [(int,int)]) -> None:
        self.number = number
        self.location = location

    def __str__(self):
        return f"Part {self.number} at {self.location}"
    
    def __repr__(self):
        return self.__str__()
    
    def is_engine_part(self,schematics: np.array) -> bool:
        box = get_box_for_part(self, schematics)
        return any([True for loc in box.flatten() if not (loc.isdigit() or loc == ".")])

    def is_potential_gear(self, schematics: np.array) -> Any:
        return any([True for loc in get_box_for_part(self, schematics).flatten() if loc == "*"])
    
    def gear_location(self, schematics: np.array) -> (int, int):
        box_corners = get_box_boundaries_for_part(self, schematics.shape)
        if self.is_potential_gear(schematics):
            box = get_box_for_part(self, schematics)
            for i in range(box.shape[0]):
                for j in range(box.shape[1]):
                    if box[i,j] == "*":
                        return (i+box_corners[0][0],j+box_corners[0][1])     


def get_array_from_file(file):
    with open(file) as f:
        a = np.array([[i for i in line.strip()] for line in f])
        # a[a == "."] = ""
        return a
    
def find_parts(a) -> list[EnginePart]:
    parts = []
    for i in range(a.shape[0]):
        current_part = ""
        locations = []
        for j in range(a.shape[1]):
            if a[i,j].isdigit():
                current_part += a[i,j]
                locations.append((i,j))
                if j == a.shape[1] - 1:
                    parts.append(ep := EnginePart(int(current_part), locations))
                    # print(ep)
                    current_part = ""
                    locations = []
            else:
                if current_part != "":
                    parts.append(ep := EnginePart(int(current_part), locations))
                    # print(ep)
                    current_part = ""
                    locations = []

    return parts

def get_box_boundaries_for_part(part: EnginePart, a_shape: (int, int)):
    xs = list(zip(*part.location))[0]
    ys = list(zip(*part.location))[1]   
    top_left = (max(min(xs) - 1 , 0), max(min(ys) - 1, 0))
    bottom_right = (min(max(xs) + 1, a_shape[0]), min(max(ys) + 1, a_shape[1]))
    return top_left, bottom_right

def get_box_for_part(part: EnginePart, schematics: np.array) -> np.array:
    b = get_box_boundaries_for_part(part, schematics.shape)
    return schematics[b[0][0]:b[1][0]+1,b[0][1]:b[1][1]+1]

def get_all_stars(schematics: np.array) -> list[(int, int)]:
    return [(i,j) for i in range(schematics.shape[0]) for j in range(schematics.shape[1]) if schematics[i,j] == "*"]


def solve_1(file):
    schematics = get_array_from_file(file)
    parts = find_parts(schematics)
    for part in parts:
        print(part)
        print(part.is_engine_part(schematics))
        print(get_box_for_part(part, schematics))
    print(sum(set([part.number for part in parts if part.is_engine_part(schematics)])))
    print(sum([part.number for part in parts if part.is_engine_part(schematics)]))
    
def solve_2(file):
    schematics = get_array_from_file(file)
    parts = find_parts(schematics)
    stars = get_all_stars(schematics)
    gears = []
    for location in stars:
        parts_for_star = [part for part in parts if part.is_potential_gear(schematics) and part.gear_location(schematics) == location]
        if len(parts_for_star) == 2:
            gears.append(parts_for_star)
    print(sum([parts[0].number * parts[1].number for parts in gears]))

if __name__ == "__main__":
    solve_1("inp_ex")
    solve_1("inp")
    
    solve_2("inp_ex")
    solve_2("inp")
    
    