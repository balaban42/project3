# The code
K = 1
N = 1

while N <= 64:
    K = K * 2
    N += 1
print(K, 'wheat grains the ruler had to pay the inventor')

CAPACITY = K * 36 / 1000 / 1000000

WEIGHT = round(K * 50 / 100000000, 1)
print(WEIGHT, ' - weight of wheat in tons')

# All values
sq_OF_NSK = 502
sq_OF_NSR = 178200
sq_OF_RUSSIA = 17100000
cr_OF_NSR = 25000000
cr_OF_RUSSIA = 64400000

SQ_OF_NSK = sq_OF_NSK * 10000
HEIGHT_OF_NSK = round(WEIGHT / SQ_OF_NSK, 2)
print(HEIGHT_OF_NSK, 'centimeters - such a height of '
                     'wheat will be covered Novosibirsk.')

SQ_OF_NSR = sq_OF_NSR * 10000
HEIGHT_OF_NSR = round(WEIGHT / SQ_OF_NSR, 2)
print(HEIGHT_OF_NSR, 'centimeters - such a height of wheat '
                     'will be covered region of Novosibirsk.')

SQ_OF_RUSSIA = sq_OF_RUSSIA * 10000
HEIGHT_OF_RUSSIA = round(WEIGHT / SQ_OF_RUSSIA, 1)
print(HEIGHT_OF_RUSSIA, 'centimeters - such a height of wheat '
                        'will be covered Russia.')

YEAR_OF_RUSSIA = round(WEIGHT / cr_OF_RUSSIA)
print(YEAR_OF_RUSSIA, 'years will need to harvest wheat in Russia.')

YEAR_OF_NSR = round(WEIGHT / cr_OF_NSR)
print(YEAR_OF_NSR, 'years will need to harvest wheat in region of '
                   'Novosibirsk.')
