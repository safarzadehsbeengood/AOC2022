from collections import deque
valves = {}
tunnels = {}
with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    for line in lines:
        a, b = line.split('; ')
        valve = a.split()[1]
        fr = int(a.split('=')[-1])
        leads_to = b.split('to ')[1].split(' ', 1)[1].split(", ")
        valves[valve] = fr 
        tunnels[valve] = leads_to

    dists = {}
    nonempty = []

    for valve in valves:
        # print(valves[valve])
        if valve != 'AA' and not valves[valve]:
            continue
        if valve != 'AA':
            nonempty.append(valve)
        dists[valve] = {valve: 0, 'AA': 0}
        visited = {valve}

        queue = deque([(0, valve)])

        while queue:
            distance, position = queue.popleft()
            for neighbor in tunnels[position]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if valves[neighbor]:
                    dists[valve][neighbor] = distance + 1
                queue.append((distance + 1, neighbor))

        del dists[valve][valve]
        if valve != 'AA':
            del dists[valve]['AA']
    
    indices = {}

    for index, element in enumerate(nonempty):
        indices[element] = index
    
    cache = {}

    def dfs(time, valve, bitmask):
        if (time, valve, bitmask) in cache:
            return cache[(time, valve, bitmask)]
        maxval = 0
        for neighbor in dists[valve]:
            bit = 1 << indices[neighbor]
            if bitmask & bit: continue
            remtime = time - dists[valve][neighbor] - 1
            if remtime <= 0: continue
            maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)

        cache[(time, valve, bitmask)] = maxval
        return maxval
    
    print(dfs(30, 'AA', 0))