import pandas as pd
df = pd.read_csv (r'/home/maxspiegs/Downloads/D19_HW1_Data.csv')

meanLaser = df['Laser'].mean()
meanUltra = df['ultrasound'].mean()
meanCamera = df['camera'].mean()

minLaser = df['Laser'].min()
minUltra = df['ultrasound'].min()
minCamera = df['camera'].min()

maxLaser = df['Laser'].max()
maxUltra = df['ultrasound'].max()
maxCamera = df['camera'].max()

varLaser = df['Laser'].var()
varUltra = df['ultrasound'].var()
varCamera = df['camera'].var()

print ('Laser Info: Average: ' + str(meanLaser) + ' Min: ' + str(minLaser) + ' Max: ' + str(maxLaser))
print ('Ultrasound Info: Average: ' + str(meanUltra) + ' Min: ' + str(minUltra) + ' Max: ' + str(maxUltra))
print ('Camera Info: Average: ' + str(meanCamera) + ' Min: ' + str(minCamera) + ' Max: ' + str(maxCamera))
print ('')
print ('Laser Var: ' + str(varLaser) + '\nUltrasound Var: ' + str(varUltra) + '\nCamera Var: ' + str(varCamera))