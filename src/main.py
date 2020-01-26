import time
import mpu6050

print("start mpu...")
mpu = mpu6050.MPU(sda=4, scl=5, led=2)

while(True):
    values = mpu.read_position()
    print(str(values[1][0])+","+str(values[1][1])+","+str(values[1][2]))
    time.sleep(0.2)

