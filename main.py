def find_minimum_pluses(s: str, target: int):
    n = len(s)
    best = None
    min_ops = float("inf")

    def dfs(pos, current_sum, parts):
        nonlocal best, min_ops

        if current_sum > target:
            return

        if pos == n:
            if current_sum == target:
                ops = len(parts) - 1
                if ops < min_ops:
                    min_ops = ops
                    best = parts[:]
            return

        for i in range(pos + 1, n + 1):
            num = int(s[pos:i]) 
            parts.append(s[pos:i])
            dfs(i, current_sum + num, parts)
            parts.pop()

    dfs(0, 0, [])
    return best

s = str(input("Ввести рядок s: "))
a = int(input("Ввести рядок a: "))

result = find_minimum_pluses(s, a)
if result:
    print("+".join(result), "=", a)
else:
    print("Розв'язку немає")
