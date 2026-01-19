import random

# Kolmenumeroisen koodin generointi (0–9)
threeOne = str(random.randint(0, 9))
threeTwo = str(random.randint(0, 9))
threeThree = str(random.randint(0, 9))

# Catenoidaan kolme yksittäistä numeroa.
threeDigit = threeOne + threeTwo + threeThree

# Nelinumeroisen koodin generointi (1–6)
fourOne = str(random.randint(1, 6))
fourTwo = str(random.randint(1, 6))
fourThree = str(random.randint(1, 6))
fourFour = str(random.randint(1, 6))

# Catenoidaan neljä yksittäistä numeroa.
fourDigit = fourOne + fourTwo + fourThree + fourFour

print("Kolmenumeroinen koodi:", threeDigit)
print("Nelinumeroinen koodi:", fourDigit)
