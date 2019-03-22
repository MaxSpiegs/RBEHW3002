import pandas as pd
import csv
df = pd.read_csv (r'/home/maxspiegs/Downloads/D19_HW1_Data.csv')



meanLaser = df['Laser'].mean()
meanUltra = df['ultrasound'].mean()
meanCamera = df['camera'].mean()
meanAll = (meanLaser + meanUltra + meanCamera)/3
time = 0

with open ("/home/maxspiegs/Downloads/D19_HW1_Data.csv") as f:
	csvreader = csv.reader(f, delimiter = ',')
	next(csvreader, None)
	for row in f:
		currentRow = row.split(",")
		laserValue = float(currentRow[0])
		if (laserValue > (meanAll + (meanAll * .1))) or (laserValue < (meanAll - (meanAll *.1))):
			print("Laser Sensor out of range at time " + str(time))
			print(laserValue)
		ultraValue = float(currentRow[1])
		if (ultraValue > (meanAll + (meanAll * .1))) or (ultraValue < (meanAll - (meanAll *.1))):
			print("Ultrasound Sensor out of range at time " + str(time))
			print(ultraValue)
		cameraValue = float(currentRow[2])
		if (cameraValue > (meanAll + (meanAll * .1))) or (cameraValue < (meanAll - (meanAll *.1))):
			print("Camera Sensor out of range at time " + str(time))
			print(cameraValue)
		time = time + 1
	print ("Finished")