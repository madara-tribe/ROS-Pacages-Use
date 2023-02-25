# 3D PointCloud from realsense as KITTI format 

This is the Pipeline to get 3D PointCloud from lidar([Intel realsense Device](https://github.com/IntelRealSense/realsense-ros)) with PCL and ROS processing.

It can be used for ML 3d dataset as KITTI format.

## Version
- Ubuntu 20.04
- ROS noetic

## Entire pipeline

<img src="https://user-images.githubusercontent.com/48679574/193379613-67df9900-9c48-434a-af1c-3d13caef5593.png" width="600px">

## Create 3D PointCloud ML Dataset as KITTI format
```python
cd pcd_create
# record rosbag
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
rosrun image_view image_view image:=/camera/color/image_raw
rosbag record -O ../data/depth.bag /camera/color/image_raw /camera/depth/image_rect_raw


# convert bag to depth and rgb image
python3 bag2depth.py --bag_file ../../data/depth.bag

# convert depth and rgb ton pcd wit open3d
python3 depth2pcd.py

# finally, create kitti format bin file from pcd with pypcd
cd ../
python3 pcd2bin_as_kitti.py
```

# PCL Preprocess

<b>raw PCD => filter => planar_segmenter => downsampler => clusterer</b>

<img src="https://user-images.githubusercontent.com/48679574/161231084-a455dd3e-d695-41a2-a6e8-9c7ae9c1a6c1.png" width="200px"><img src="https://user-images.githubusercontent.com/48679574/161231104-fa4338d0-e88a-4e34-b2d5-b6f551950d36.png" width="200px"><img src="https://user-images.githubusercontent.com/48679574/161231116-a115ed70-098e-4a2f-a501-0ea991285744.png" width="200px"><img src="https://user-images.githubusercontent.com/48679574/161231121-2f8ae135-a7ec-4543-9d75-adb2c5dae582.png" width="200px"><img src="https://user-images.githubusercontent.com/48679574/161231137-6de017c5-91ea-4579-a0d3-91280e090d03.png" width="200px">


# PCL exsamples
- [Removing outliers using a StatisticalOutlierRemoval filter](https://pcl.readthedocs.io/projects/tutorials/en/latest/statistical_outlier.html)
- [Downsampling a PointCloud using a VoxelGrid filter](https://pcl.readthedocs.io/en/latest/voxel_grid.html)
- [Extracting indices from a PointCloud](https://pcl.readthedocs.io/en/latest/extract_indices.html)
- [Euclidean Cluster Extraction](https://pcl.readthedocs.io/en/latest/cluster_extraction.html)


# Main References
- [realsense-ros](https://github.com/IntelRealSense/realsense-ros)
- [Point Cloud Library tools](https://github.com/PointCloudLibrary/pcl/tree/master/tools)

