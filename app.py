import math

def calculate_volume_cone(radius,height):
  volume = (1/3) * math.pi * (radius**2) * height
  return volume

print(calculate_volume_cone(2,3))