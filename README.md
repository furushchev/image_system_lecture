image_system_lecture
================

1. Setup

``` bash
sudo sh -c "echo \"deb http://packages.ros.org/ros-shadow-fixed/ubuntu `lsb_release -sc` main\" > /etc/apt/sources.list.d/ros-latest.list"
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt update
sudo apt install python-catkin-tools python-rosdep python-pip ros-indigo-base ros-indigo-rosbash
source /opt/ros/indigo/setup.bash
sudo rosdep init && rosdep update
mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
wstool init && wstool set -u image_system_lecture --git https://github.com/furushchev/image_system_lecture -v master
rosdep install --from-paths . --ignore-src -r -n -y
cd ~/catkin_ws
catkin init && catkin build
source ~/catkin_ws/devel/setup.bash
```

2. Try

```
roslaunch image_system_lecture camera.launch
rosrun image_system_lecture optical_flow.py
```
