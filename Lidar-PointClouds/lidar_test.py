import numpy as np

def get_lidar(lidar_file = "data/bin/frame000001.bin"):
    lidars = np.fromfile(lidar_file, dtype=np.float32)
    print(lidars.shape)
    return lidars.reshape(-1, 4)
  
pcds = get_lidar(lidar_file = "data/bin/frame000001.bin")
print(pcds.shape)

