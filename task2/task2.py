def coordinates_extraction(string):
    string = string.replace('\n', '')
    coordinates = string.split()
    for i in range(len(coordinates)):
        coordinates[i] = float(coordinates[i])
    return(coordinates)
with open('1.txt', 'r') as f:
    circle = f.readlines()
with open('2.txt', 'r') as f:
    points = f.readlines()
circle[0] = coordinates_extraction(circle[0])
circle[1] = float(circle[1])
for i in range(len(points)):
    points[i] = coordinates_extraction(points[i])
for i in range(len(points)):
    distance = (((circle[0][0] - points[i][0])**2 +
                 (circle[0][1] - points[i][1])**2)**0.5)
    if distance == circle[1]:
        print('0')
    elif distance < circle[1]:
        print('1')
    else:
        print('2')