from groups import Dihedral as D

d6 = D(6)
d3 = D(3)

assert d3.vertices() == [0, 1, 2]
assert d6.vertices() == [0, 1, 2, 3, 4, 5]
assert d3.apply(d3.r[2]) == [2, 0, 1]
assert d3.apply(d3.r[1], [0]) == [1]
assert d3.apply(d3.s[0]) == [1, 0, 2]
assert d6.has_subgroup(d3)
assert not(d3.has_subgroup(d6))
assert d3.has_subgroup([d3.r[0]])
assert d6.has_subgroup([r for r in d6.r])
assert d3.has_subgroup([d3.r[0], d3.s[0]])
assert not(d3.has_subgroup([d3.s[0]]))

assert d3.subgroups() == [["r0"], ["r0", "s0"], ["r0", "s1"], ["r0", "s2"], ["r0", "r1", "r2"], ["r0", "r1", "r2", "s0", "s1", "s2"]]

print("All tests passed!")