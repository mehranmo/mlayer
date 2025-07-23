"""Example conversions using M-layer style identifiers."""

from dataclasses import dataclass

@dataclass
class AnnotatedValue:
    value: float
    unit: str
    quantity_id: str
    unit_id: str

def annotate(value: float, unit: str, quantity_id: str, unit_id: str) -> AnnotatedValue:
    """Create an annotated value with quantity and unit identifiers."""
    return AnnotatedValue(value, unit, quantity_id, unit_id)

# Conversion factors to SI units
ENERGY_FACTORS = {"J": 1.0, "cal": 4.184, "ft*lbf": 1.3558179483314}
LENGTH_FACTORS = {"m": 1.0, "ft": 0.3048}
PRESSURE_FACTORS = {"Pa": 1.0, "psi": 6894.757, "bar": 1e5}
VELOCITY_FACTORS = {"m/s": 1.0, "km/h": 0.2777778, "mph": 0.44704}
MASSFRACTION_FACTORS = {"kg/kg": 1.0, "%": 0.01}

# Temperature uses offset so handled separately

def convert(value: float, unit_from: str, unit_to: str, factors: dict) -> float:
    base = value * factors[unit_from]
    return base / factors[unit_to]

def convert_temperature(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "degC":
        kelvin = value + 273.15
    elif unit_from == "degF":
        kelvin = (value + 459.67) * 5/9
    else:  # K
        kelvin = value
    if unit_to == "degC":
        return kelvin - 273.15
    elif unit_to == "degF":
        return kelvin * 9/5 - 459.67
    else:
        return kelvin

def demo() -> None:
    energy = annotate(10.5, "J", "QK-energy", "U-joule")
    energy_cal = convert(energy.value, energy.unit, "cal", ENERGY_FACTORS)
    print(f"{energy.value} {energy.unit} -> {energy_cal:.3f} cal")

    length = annotate(2.0, "m", "QK-length", "U-m")
    length_ft = convert(length.value, length.unit, "ft", LENGTH_FACTORS)
    print(f"{length.value} {length.unit} -> {length_ft:.2f} ft")

    temp = annotate(25.0, "degC", "QK-temperature", "U-degC")
    temp_f = convert_temperature(temp.value, temp.unit, "degF")
    print(f"{temp.value} {temp.unit} -> {temp_f:.1f} degF")

    pressure = annotate(101325.0, "Pa", "QK-pressure", "U-Pa")
    pressure_psi = convert(pressure.value, pressure.unit, "psi", PRESSURE_FACTORS)
    print(f"{pressure.value} {pressure.unit} -> {pressure_psi:.2f} psi")

    velocity = annotate(30.0, "m/s", "QK-velocity", "U-m_per_s")
    velocity_mph = convert(velocity.value, velocity.unit, "mph", VELOCITY_FACTORS)
    print(f"{velocity.value} {velocity.unit} -> {velocity_mph:.1f} mph")

    fraction = annotate(0.15, "kg/kg", "QK-mass_fraction", "U-kg_per_kg")
    fraction_pct = convert(fraction.value, fraction.unit, "%", MASSFRACTION_FACTORS)
    print(f"{fraction.value} {fraction.unit} -> {fraction_pct:.1f}%")

if __name__ == "__main__":
    demo()
