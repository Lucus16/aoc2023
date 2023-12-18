import sys

sections = sys.stdin.read().split("\n\n")
seeds = [int(seed) for seed in sections[0].split(":")[1].split()]
maps = [
    [[int(x) for x in xs.split()] for xs in section.splitlines()[1:]]
    for section in sections[1:]
]


def maplookup(m, x):
    for dst_start, src_start, size in m:
        if src_start <= x < src_start + size:
            return x - src_start + dst_start
    return x


def mapslookup(maps, x):
    for m in maps:
        x = maplookup(m, x)
    return x


print(min(mapslookup(maps, seed) for seed in seeds))


def maprangepartial(m, r_start, r_size):
    for dst_start, src_start, m_size in m:
        src_end = src_start + m_size
        dst_end = dst_start + m_size
        if src_start <= r_start < src_end:
            y_start = r_start - src_start + dst_start
            y_size = min(r_size, src_end - r_start)
            return (y_start, y_size)
    y_size = r_size
    for _, src_start, _ in m:
        if src_start > r_start:
            y_size = min(y_size, src_start - r_start)
    return (r_start, y_size)


def mapranges(m, ranges):
    for r_start, r_size in ranges:
        while r_size > 0:
            y_start, y_size = maprangepartial(m, r_start, r_size)
            yield (y_start, y_size)
            r_start += y_size
            r_size -= y_size


def mapsranges(maps, ranges):
    for m in maps:
        ranges = list(mapranges(m, ranges))
    return ranges


seed_ranges = list(zip(seeds[0::2], seeds[1::2]))
print(min(start for start, size in mapsranges(maps, seed_ranges)))
