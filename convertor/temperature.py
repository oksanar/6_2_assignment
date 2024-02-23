def from_celsius_to_fahrenheit(n: float) -> float:
     result = (n * (9/5)) + 32
     return float("{:.4f}".format(result))


def from_fahrenheit_to_celsius(n: float) -> float:
     result = (n - 32)/(9/5)
     return float("{:.4f}".format(result))

