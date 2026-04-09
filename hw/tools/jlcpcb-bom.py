#!/usr/bin/env python3
import csv
import sys

footprint_map = {
    "Capacitor_SMD:C_0402_1005Metric": "0402",
    "Capacitor_SMD:C_0603_1608Metric": "0603",
    "Capacitor_SMD:C_0805_2012Metric": "0805",
    "LED_SMD:LED_0603_1608Metric": "0603",
    "Resistor_SMD:R_0402_1005Metric": "0402",
    "Resistor_SMD:R_0603_1608Metric": "0603",
}

filename = sys.argv[1]
with open(filename) as f:
    lines = list(csv.DictReader(f))

# Remove test points
lines = [l for l in lines if not l["Reference"].startswith("TP")]

# Make footprint names that JLCPCB will find
for l in lines:
    l["Footprint"] = footprint_map.get(l["Footprint"], l["Footprint"])

with open(filename, "w") as f:
    writer = csv.DictWriter(f, lines[0].keys())
    writer.writeheader()
    writer.writerows(lines)
