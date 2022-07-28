def birthdayCakeCandles(candles):
    counter = 0
    maximum = max(candles)

    for i in range(0, len(candles)):
        if candles[i] == maximum:
            counter += 1
    return counter


candles = [4, 4, 1, 3]
print(birthdayCakeCandles(candles))
