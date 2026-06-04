# Day 8 Playground
# Minimal setup with little imports

junctions = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y, z = (int(k) for k in line.split(','))
        junctions.append((x, y, z))

def dist_calc(junc1, junc2):
    return sum((junc1[k] - junc2[k])**2 for k in range(3))

union_map = {}
class Union:
    def __init__(self, members):
        self.members = members
        for mem in members:
            union_map[mem] = self
    def union(self, other):
        new_members = self.members | other.members
        return Union(new_members)

for junc in junctions:
    Union({junc})

all_point_pairs = []
for index, point in enumerate(junctions):
    for junc_index in range(index + 1, len(junctions)):
        junc = junctions[junc_index]
        all_point_pairs.append((point, junc))
all_point_pairs.sort(key=lambda pair: dist_calc(pair[0], pair[1]))

# Part 1
# Puzzle includes an iteration cap of 1000
iteration_cap = 1000
for index, (point_one, point_two) in enumerate(all_point_pairs):
    if index == iteration_cap:
        unions = set()
        for junc in junctions:
            unions.add(union_map[junc])
        unions = list(sorted(unions, key=lambda union: len(union.members), reverse=True))
        breakpoint()
        circuit_one = unions[0].members
        circuit_two = unions[1].members
        circuit_three = unions[2].members
        print(f"Largest Circuits: {len(circuit_one)}, {len(circuit_two)}, {len(circuit_three)}") 
        break
    
    # We have found the duplicate entry in the map, continue looping
    if union_map[point_one] == union_map[point_two]:
        continue
    
    # We want to merge these two maps as their circuits are now connected
    union = union_map[point_one].union(union_map[point_two])

    # Part 2
    # If we have reached a one circuit scenario, print the x/y
    if len(union.members) == len(junctions):
        print(f"Last connected junctions: {point_one} {point_two}")
        break

