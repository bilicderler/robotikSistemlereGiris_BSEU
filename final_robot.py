
import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = p.loadURDF("plane.urdf")
robot = p.loadURDF("final_robot.urdf")

p.setGravity(0, 0, -10)

# 2. eklemi kontrol modunu ve hedef pozisyonunu belirle
joint_index = 1  # 2. eklem için indeks 1 olacaktır
p.setJointMotorControl2(robot, joint_index, p.POSITION_CONTROL, targetPosition = 1)

while True:
    p.stepSimulation()
    time.sleep(0.10)
