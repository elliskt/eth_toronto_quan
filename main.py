import quantum_blur as qb
import numpy as np
from PIL import Image

print('[quantum_blur] booting...')
im = Image.open('images/blur1.jpg')


ratio = 500/im.size[0]
im = im.resize((int(im.size[0] * ratio), int(im.size[1] * ratio)))



def partial_x(qc,fraction):
    print('[partial_x] num_qubits: ', qc.num_qubits)
    for j in range(qc.num_qubits):
        qc.rx(np.pi*fraction,j)


circuits = qb.image2circuits(im)

for i in range(5, 500, 1):
    circuits = qb.image2circuits(im)
    frac = round(i*0.001, 3)
    for qc in circuits:
        partial_x(qc, frac)



    rotated_ac = qb.circuits2image(circuits)

    rotated_ac.save('result_blur1/{}.jpg'.format(i))
    print('[INFO] {}.jpg'.format(i))





