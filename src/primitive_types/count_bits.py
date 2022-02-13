def count_bits(x: int) -> int:
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count
