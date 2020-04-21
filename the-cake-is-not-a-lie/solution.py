def solution(cake):
    cake_size = len(cake)
    for slice_size in range(1, cake_size + 1):
        if cake_size % slice_size == 0 and are_slices_same(cake, slice_size):
            return cake_size / slice_size

def are_slices_same(cake, slice_size):
    cake_size = len(cake)
    unique_slices = set()
    for start in range(0, cake_size, slice_size):
        unique_slices.add(cake[start:start + slice_size])
    return len(unique_slices) == 1
