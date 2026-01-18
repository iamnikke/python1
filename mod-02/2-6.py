import random

# Kolmenumeroinen koodi (0–9)
code3 = (
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
)

# Nelinumeroinen koodi (1–6)
code4 = (
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6)
)

print("Kolmenumeroinen koodi:", code3)
print("Nelinumeroinen koodi:", code4)
