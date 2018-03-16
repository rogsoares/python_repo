import numpy as np

numnodes = 100;

print('Gerando arquivo...')
fid = open('output.txt', 'w')
fid.write("Number of vertices:\n")
fid.write("%d\n" % (numnodes))
for i in range(numnodes):
    fid.write("%.15e\t%.15e\t%.15e\n" % (i/3,(i+2)/8,(i**2-2*i)))
fid.close()
print('concluido\n')


print('Abrindo arquivo para leitura\n')
fid = open('output.txt', 'r')
for i, line in enumerate(fid):
    if i == 1:
        numnodes = int(line)
        print('numnodes: %d\n' % (numnodes))
    elif i >= 2:
        coords = line.split()
        x = float(coords[0])
        y = float(coords[1])
        z = float(coords[2])
        print('%.15e\t%.15e\t%.15e' % (x, y, z))
fid.close()

mat_coordinates = np.array(5, 3)
for i in range(5):
    for j in range(5):
        mat_coordinates[i][j] = i*j

