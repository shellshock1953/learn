motocycles = ['honda', 'yamaha', 'suzuki', 'bmw', 'subaru']
print(motocycles)
motocycles.append('ducati')
print(sorted(motocycles))
motocycles.insert(1, 'ferrafi')
print(motocycles)
del motocycles[1]
print(motocycles)


popped_moto = motocycles.pop(1)
print(popped_moto)
print(motocycles)

motocycles.remove('suzuki')

motocycles.sort()
print(motocycles)

motocycles.reverse()
print(motocycles)
print(len(motocycles))
