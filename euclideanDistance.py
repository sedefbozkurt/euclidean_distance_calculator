# formül: d = √(x₂-x₁)²+(y₂-y₁)²

# 1. adım: Noktaları tanımla
points = [(0, 2), (3, 5), (5, 7), (2, 0), (2, 3)]

# 2. adım: Öklid mesafesi için fonksiyon yaz
def euclideanDistance(point1, point2):
  return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# 3. adım: Mesafeleri hesapla
distances = []
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distances.append(euclideanDistance(points[i], points[j]))

# 4. adım: Min mesafeyi bul
minDistance = min(distances)

print("Minimum Öklid Mesafesi: ", minDistance)