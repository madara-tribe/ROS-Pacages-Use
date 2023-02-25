import numpy as np
import os
import argparse
from pypcd import pypcd
import glob
from tqdm import tqdm

def main():
    ## Add parser
    parser = argparse.ArgumentParser(description="Convert .pcd to .bin")
    parser.add_argument(
        "--pcd_path",
        help=".pcd file path.",
        type=str,
        default="data/pcds/"
    )
    parser.add_argument(
        "--bin_path",
        help=".bin file path.",
        type=str,
        default="data/bin"
    )
    args = parser.parse_args()
    os.makedirs(args.bin_path)
    ## Find all pcd files
    pcd_files = glob.glob(os.path.join(args.pcd_path, "*.pcd"))
    pcd_files.sort()   
    print("Finish to load point clouds!")

    ## Converting Process
    print("Converting Start!")
    count = 0
    for pcd_file in tqdm(pcd_files):
        pc = pypcd.PointCloud.from_path(pcd_file)        
        ## Get data from pcd (x, y, z, intensity, ring, time)
        x = pc.pc_data['x']
        y = pc.pc_data['y']
        z = pc.pc_data['z']
        intensity = pc.pc_data['rgb']
        arr = np.zeros(x.shape[0] + y.shape[0] + z.shape[0] + intensity.shape[0], dtype=np.float32)
        
        arr[::4] = x
        arr[1::4] = y
        arr[2::4] = z
        arr[3::4] = intensity

        bin_file_path = os.path.join(args.bin_path, "frame%06i.bin" % count)
        arr.astype('float32').tofile(bin_file_path)

        count += 1
    print('convert total {} pcd to bin as kitti format'.format(count))
    
if __name__ == "__main__":
    main()
