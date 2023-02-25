#/bin/sh
cd ~/catkin_ws/src
git clone -b ros1-legacy https://github.com/IntelRealSense/realsense-ros.git
sudo apt-get install ros-noetic-ddynamic-reconfigure
sudo apt-get install ros-noetic-realsense2-camera
cd ~/catkin_ws
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install

