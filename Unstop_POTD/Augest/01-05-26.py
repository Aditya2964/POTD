MOD = 1000000007

def process_events(n, m, events):
    parent = list(range(n + 1))
    weight = [1] * (n + 1)   # x -> parent[x]

    def modinv(x):
        return pow(x, MOD - 2, MOD)

    def find(x):
        if parent[x] != x:
            root = find(parent[x])
            weight[x] = weight[x] * weight[parent[x]] % MOD
            parent[x] = root
        return parent[x]

    ans = []

    for event in events:
        if event[0] == 1:
            _, u, v, p, q = event
            val = p * modinv(q) % MOD

            if u == v:
                if val == 1:
                    ans.append("OK")
                else:
                    ans.append("CONTRADICTION")
                continue

            ru = find(u)
            rv = find(v)

            wu = weight[u]
            wv = weight[v]

            if ru == rv:
                implied = wu * modinv(wv) % MOD
                if implied == val:
                    ans.append("OK")
                else:
                    ans.append("CONTRADICTION")
            else:
                # attach ru under rv
                parent[ru] = rv
                # weight[ru] = ru -> rv
                weight[ru] = val * wv % MOD * modinv(wu) % MOD
                ans.append("OK")

        else:
            _, u, v = event

            if u == v:
                ans.append(1)
                continue

            ru = find(u)
            rv = find(v)

            if ru != rv:
                ans.append("UNKNOWN")
            else:
                ans.append(weight[u] * modinv(weight[v]) % MOD)

    return ans


def main():
    import sys

    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])
    m = int(lines[1])

    events = []
    for i in range(2, 2 + m):
        events.append(tuple(map(int, lines[i].split())))

    result = process_events(n, m, events)

    for x in result:
        print(x)


if __name__ == "__main__":
    main()
