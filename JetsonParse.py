import os
import subprocess
import tempfile

#os.system("cd /home/robert/Documents/workspace/polaris/ros && ./jetson")
#string = os.popen('pwd').readlines()
cmd = "cd /home/robert/Documents/workspace/polaris/ros && ./jetson"
string = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
print "I have run"
print string
#string = "RAM 1652/7854MB (lfb 1237x4MB) CPU [1%@2035,0%@2035,0%@2035,4%@2035,1%@2035,6%@2035] BCPU@31C MCPU@31C GPU@29.5C PLL@31C Tboard@27C Tdiode@27.25C PMIC@100C thermal@30.1C VDD_IN 2451/2471 VDD_CPU 306/311 VDD_GPU 153/153 VDD_SOC 612/612 VDD_WIFI 0/10 VDD_DDR 828/828"
string = string.split(" ")
#pipe = Popen("pwd", shell=True, stdout=PIPE).stdout
#string = pipe.read()
print string
CPU_percentage = string[5]
CPU_percentage = CPU_percentage.split("[")
CPU_percentage = CPU_percentage[1]
CPU_percentage = CPU_percentage.split("]")
CPU_percentage = CPU_percentage[0]
CPU_percentage = CPU_percentage.split("%@")
for i in range(5):
	CPU_percentage[i + 1] = CPU6_percentage[i + 1].split(",")
	CPU_percentage[i + 1] = CPU6_percentage[i + 1][1]
del CPU6_percentage[-1]
CPU1_percentage = int(CPU_percentage[0])
CPU2_percentage = int(CPU_percentage[1])
CPU3_percentage = int(CPU_percentage[2])
CPU4_percentage = int(CPU_percentage[3])
CPU5_percentage = int(CPU_percentage[4])
CPU6_percentage = int(CPU_percentage[5])

RAM = string[1]
RAM = RAM.split("/")
RAM[1] = RAM[1].split("M")
RAM_max = int(RAM[1][0])
RAM_min = int(RAM[0])
RAM_percentage = (RAM_min*100)/RAM_max
print "RAM max = ", RAM_max
print "RAM min = ", RAM_min
print "RAM percentage = ", RAM_percentage
print "CPU core 1 percentage = ", CPU1_percentage
print "CPU core 2 percentage = ", CPU2_percentage
print "CPU core 3 percentage = ", CPU3_percentage
print "CPU core 4 percentage = ", CPU4_percentage
print "CPU core 5 percentage = ", CPU5_percentage
print "CPU core 6 percentage = ", CPU6_percentage
