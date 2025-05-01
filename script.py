import httpx
import json
import sys

data = httpx.get("https://tjl.co/queens-gambit-arg/data.json", timeout=120.0).json()
# data = json.load(open('data-verified.json', 'r'))
# data = httpx.get("https://tjl.co/queens-gambit-arg/data.json").json()
action = sys.argv[1]
print(f"count: {len(data)}")

if action == "symbol":
    direction = sys.argv[2]
    symbols = []
    found = False
    while True:
        for k, v in data.items():
            vs = v['symbols']
            if v['sequence'] == int(sys.argv[3]) and not found:
                if direction == "down":
                    symbols = vs[7]
                    print(f"{k}, {v['sequence']}: {symbols}")
                    found = True
                    break
                if direction == "up":
                    symbols = vs[0]
                    print(f"{k}, {v['sequence']}: {symbols}")
                    found = True
                    break
                if direction == "right":
                    symbols = [vs[0][7], vs[1][7], vs[2][7], vs[3][7], vs[4][7], vs[5][7], vs[6][7], vs[7][7]]
                    print(f"{k}, {v['sequence']}: {symbols}")
                    found = True
                    break
                if direction == "left":
                    symbols = [vs[0][0], vs[1][0], vs[2][0], vs[3][0], vs[4][0], vs[5][0], vs[6][0], vs[7][0]]
                    print(f"{k}, {v['sequence']}: {symbols}")
                    print(symbols)
                    found = True
                    break        
            if found and direction == "down":
                if vs[0] == symbols:
                    print(f"{k}, {v['sequence']}: {vs[7]}")
            if found and direction == "up":
                if vs[7] == symbols:
                    print(f"{k}, {v['sequence']}: {vs[0]}")
            if found and direction == "left":
                if vs[0][7] == symbols[0] and vs[1][7] == symbols[1] and vs[2][7] == symbols[2] and vs[3][7] == symbols[3] and vs[4][7] == symbols[4] and vs[5][7] == symbols[5] and vs[6][7] == symbols[6] and vs[7][7] == symbols[7]: 
                    print(f"{k}, {v['sequence']}: {[vs[0][7], vs[1][7],vs[2][7],vs[3][7],vs[4][7],vs[5][7],vs[6][7], vs[7][7]]}")
            if found and direction == "right":
                if vs[0][0] == symbols[0] and vs[1][0] == symbols[1] and vs[2][0] == symbols[2] and vs[3][0] == symbols[3] and vs[4][0] == symbols[4] and vs[5][0] == symbols[5] and vs[6][0] == symbols[6] and vs[7][0] == symbols[7]: 
                    print(f"{k}, {v['sequence']}: {[vs[0][0], vs[1][0],vs[2][0],vs[3][0],vs[4][0],vs[5][0],vs[6][0],vs[7][0]]}")


if action == "seq":
    for k, v in data.items():
        if v['sequence'] == int(sys.argv[2]):
            print(k)
if action == "fen":
    for k, v in data.items():
        if v['sequence'] == int(sys.argv[2]):
            print(f"{k}, {v['sequence']}")
            print(v['fen'])

if action == "remaining":
    all_seqs = []
    for k, v in data.items():
        all_seqs.append(v['sequence'])
    existing_seqs = set(all_seqs)
    missing_numbers = [
        num for num in range(0, 4096 + 1)
        if num not in existing_seqs
    ]
    print(missing_numbers)
    print(len(missing_numbers))

if action == "search_pattern":
    symbols = ['Nw', 'Rw', 'Kw', 'Qb', 'Bw', 'Rb', 'Kb', 'Nb']
    for k, v in data.items():
        vs = v['symbols']
        if vs[0] == symbols:
            print(k)
            
if action == "search_fen":
    fen = sys.argv[2]
    for k, v in data.items():
        if fen in v['fen']:
            print(f"{k}, {v['sequence']}")
            print(v['fen'])