FEETS_TO_METERS_COEFICIENT = 0.3048

def from_feets_to_meters(n: float) -> float:
     result = n * FEETS_TO_METERS_COEFICIENT
     return float("{:.4f}".format(result))

def from_meters_to_feets(n: float) -> float:
     result = n / FEETS_TO_METERS_COEFICIENT
     return float("{:.4f}".format(result))
