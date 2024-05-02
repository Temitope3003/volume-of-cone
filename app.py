import math

def calculate_volume_cone(radius,height):

  volume =  (math.pi * radius**2 * height)/3
  
  return volume

print(calculate_volume_cone(2,3))
