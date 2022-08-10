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


for i in range(5, 501, 10):
    circuits = qb.image2circuits(im, log=True)
    frac = round(i*0.0001, 3)
    for qc in circuits:
        partial_x(qc, frac)



    rotated_ac = qb.circuits2image(circuits, log=True)

    rotated_ac.save('result_blur_log/log_{}.jpg'.format(i))
    print('[INFO] log_{}.jpg'.format(i))