# ros_ws

ROS2 Jazzy 学习工作空间。'my_first_pkg'是跟着教程手敲的最小练习包，逐行自己写的，用来熟悉 ament_python 包的目录结构和 ROS2 的通信方式。

## 里面有什么

| 程序 | 用到的 ROS2 机制 | 干什么 |
|---|---|---|
| `hello` | 定时器 | 每秒打印一行 |
| `talker` / `listener` | 话题 `/chatter` | 一个发、一个收 |
| `adder` / `client` | 服务 `/add` | 一个算、一个调 |
| `talk.launch.py` | 启动文件 | 一次拉起两个节点 |

## 怎么跑

```bash
colcon build --packages-select my_first_pkg
source install/setup.bash
ros2 run my_first_pkg talker      # 终端 A
ros2 run my_first_pkg listener    # 终端 B