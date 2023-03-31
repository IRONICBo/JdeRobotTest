# ROS2

- Use colcon to build video link: https://youtu.be/TlIArYPhhNc
- Send infomation and robot navigation video link: https://youtu.be/PYFmSsUwN5k

Using ROS2 Foxy to simulate `Introduction` and `ROS2 Navigation2`, build with colcon.

### Part 1

1. Set up environment in ubuntu 20.04

```bash
locale

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale
```

2. Install ROS2 Foxy

Add resource
```bash
sudo apt install software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Install Tools
```bash
sudo apt update && sudo apt install -y \
  libbullet-dev \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools

python3 -m pip install -U \
  argcomplete \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest

sudo apt install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev

sudo apt install --no-install-recommends -y \
  libcunit1-dev
```

Get code
```bash
mkdir -p ~/ros2_foxy/src
cd ~/ros2_foxy
vcs import --input https://raw.githubusercontent.com/ros2/ros2/foxy/ros2.repos src
```

Install rosdep
```bash
sudo apt upgrade
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-5.3.1 urdfdom_headers"
```

Test environment
```bash
source ~/ros2_foxy/install/local_setup.bash
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_py listener
```

Then check the output in terminal

2. Build demo

```bash
colcon build --symlink-install
```

3. Run demo

```bash
ros2 run py_pubsub talker
```

```bash
ros2 run py_pubsub listener
```

And the output "Hello! ROS2 is fun" will show in both terminal.

### Part 2

1. Download and build turtlebot3

> If some libraries is missing, install it with `sudo apt install <library name>`

```bash
mkdir -p ~/tb3_ws/src
cd ~/tb3_ws
wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/foxy-devel/turtlebot3.repos
vcs import src < turtlebot3.repos
colcon build --symlink-install
```

Add to environment
```bash
echo 'source ~/tb3_ws/install/setup.bash' >> ~/.bashrc
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
source ~/.bashrc
```

Download gazebo
```bash
cd ~/.gazebo/
git clone https://github.com/osrf/gazebo_models models
rm -rf models/.git
echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/tb3_ws/src/turtlebot3/turtlebot3_simulations/turtlebot3_gazebo/models' >> ~/.bashrc
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc
```

Start Fake node
```bash
ros2 launch turtlebot3_fake_node turtlebot3_fake_node.launch.py
```

Star turtlebot3
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Scan for map(Each command is new terminal)
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
ros2 run turtlebot3_teleop teleop_keyboard
```

Save map to local
```bash
ros2 run nav2_map_server map_saver_cli -f ~/map
```

Navigation (Each command is new terminal)
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=/home/ubuntu/map.yaml
```

> Use 2D Pose Estimate to initialize the pose, use Navigation2 Goal to select the target point for navigation

### Ref

- https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html