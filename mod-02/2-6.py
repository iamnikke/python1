import random

# Kolmenumeroinen koodi (0–9)
threeDigit = (
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
)

# Nelinumeroinen koodi (1–6)
fourDigit = (
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6)
)

print("Kolmenumeroinen koodi:", threeDigit)
print("Nelinumeroinen koodi:", fourDigit)
