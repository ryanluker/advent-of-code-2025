# Day 8 Playground
# Minimal setup with little imports

junctions = []
with open('example-input.txt', 'r') as f:
    for line in f.readlines():
        x, y, z = (int(k) for k in line.split(','))
        junctions.append((x, y, z))

def dist_calc(junc1, junc2):
    return sum((junc1[k] - junc2[k])**2 for k in range(3))

breakpoint()
union_map = {}
class Union:
    def __init__(self, members):
        self.members = members
        for mem in members:
            union_map[mem] = self
    def union(self, other):
        new_members = self.members | other.members
        return Union(new_members)

breakpoint()
for junc in junctions:
    Union({junc})

all_point_pairs = []
for index, point in enumerate(junctions):
    for junc_index in range(index + 1, len(junctions)):
        junc = junctions[junc_index]
        all_point_pairs.append((point, junc))
all_point_pairs.sort(key=lambda pair: dist_calc(pair[0], pair[1]))
breakpoint()
