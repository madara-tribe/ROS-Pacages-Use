# save bag as image
roslaunch lidar_capture bag2image.launch bag_path:=/home/hagi/place/images/
# check bag file
roscore
rosrun rqt_bag rqt_bag im.bag

# save rosbag
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
rosrun image_view image_view image:=/camera/color/image_raw
rosbag record -O ../data/depth.bag /camera/color/image_raw /camera/depth/image_rect_raw
# create pcd from depth and rgb images
python3 bag2depth.py --bag_file ../../data/depth.bag
python3 depth2pcd.py
# rosrun pcd_create vccs <pcd_file>
rosrun pcd_create vccs /home/parallels/place/sink_pointcloud.pcd
