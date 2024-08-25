max_val = max(max(linha) for linha in m)
larg_cmp = len(str(max_val))

for i in range(t):
    lin_fmt = " ".join(f"{m[i][j]:{larg_cmp}d}" for j in range(t))
    print(lin_fmt)
print()
