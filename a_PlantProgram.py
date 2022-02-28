import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


# print(primrose.get_petals())  -- plant object has no attribute for petals 
