import csv
import bme280
import smbus2
import time
from time import sleep
from datetime import datetime, timedelta
from pms5003 import PMS5003
from collections import deque
import os

CSV_FILE_LAST60MIN = 'last_60min.csv'
CSV_FILE_LAST24H = 'last_24H.csv'
BUFFER_LENGTH_60MIN = 60*5
BUFFER_LENGTH_24H = 60*10
buffer_60M = deque(maxlen = BUFFER_LENGTH_60MIN)
buffer_24H = deque(maxlen = BUFFER_LENGTH_24H)


def get_filename():
	return datetime.now().strftime('%Y-%m-%d') + '.csv'	
	
def get_now_timestamp():
	return datdtime.now().strftime('%Y-%m-%d %H:%M:%S')
	
def ensure_file_has_header(filename):
	try:
		with open(filename, 'x', newline= '') as f:
			writer = csv.writer(f)
			writer.writerow(['timestamp', 'temperature', 'humidity', 'pressure', 'pm1.0', 'pm2.5', 'pm10'])
	except	FileExistsError:
		pass


# Save the data into the buffer (csv)
def save_buffer(buffer_tmp, name_file):
	with open('data/' + name_file, mode = 'w', newline = '') as f:
		writer = csv.writer(f)
		writer.writerow(['timestamp', 'temperature', 'humidity', 'pressure', 'pm1.0', 'pm2.5', 'pm10'])
		for row in buffer_tmp:
			writer.writerow(row)
			
# Add data to buffer
def add_data(buffer_tmp, data):
	buffer_tmp.append(data)

def git_push(filname, time):
	#os.system(f'cp {filename} air-quality-project'}
	os.system('git add .')
	os.system(f'git commit -m "{time}"')
	os.system(f'git push')

# initialize 
current_date = datetime.now().date()
filename = get_filename()
ensure_file_has_header(filename)

# read bme280
port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

# read PMS5003
pms5003 = PMS5003(device="/dev/ttyAMA0", baudrate=9600)

start_time60min = time.time()
start_time24H = start_time60min 
time_workflow = start_time60min 
try:
	while True:
		now = datetime.now()
		timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
		bme280_data = bme280.sample(bus,address)
		humidity  = bme280_data.humidity
		pressure  = bme280_data.pressure
		ambient_temperature = bme280_data.temperature
		data = pms5003.read()
		print(f'Humidity: {humidity:.2f} | Pression:{pressure:.2f} | Room Temperature:{ambient_temperature:.2f}')
		print(f'PM1.0 {data.pm_ug_per_m3(1.0)} | PM2.5 {data.pm_ug_per_m3(2.5)} | PM10: {data.pm_ug_per_m3(10)}')
		print('\n')
		
		data_buffer = [timestamp, humidity, pressure, ambient_temperature, data.pm_ug_per_m3(1.0), data.pm_ug_per_m3(2.5), data.pm_ug_per_m3(10)]
		# Check id the day changed
		if now.date() != current_date:
			current_date = now.date()
			filename = get_filename()
			ensure_file_has_header(filename)
		
		with open('data/' + filename, 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow([timestamp, ambient_temperature, humidity, pressure, data.pm_ug_per_m3(1.0), data.pm_ug_per_m3(2.5), data.pm_ug_per_m3(10)])
		
		#60 min buffer
		current_time = time.time() - start_time60min
		if current_time > BUFFER_LENGTH_60MIN:
			save_buffer(buffer_60M, CSV_FILE_LAST60MIN)
			# clean the buffer
			cleaned_buffer = deque(maxlen = BUFFER_LENGTH_60MIN)
			buffer_60M = cleaned_buffer
			start_time_60min = current_time
			git_push(CSV_FILE_LAST60MIN, start_time60min)
		
		current_time = time.time() - start_time24H
		if current_time > BUFFER_LENGTH_24H:
			save_buffer(buffer_24H, CSV_FILE_LAST24H)
			# clean the buffer
			cleaned_buffer = deque(maxlen = BUFFER_LENGTH_24H)
			buffer_24H = cleaned_buffer
			start_time24H = current_time
			git_push(CSV_FILE_LAST24H, start_time24H)
		
		add_data(buffer_60M, data_buffer)
		add_data(buffer_24H, data_buffer)
		sleep(60)

except KeyboardInterrupt:
	pass
