import threading, subprocess, cv2
<<<<<<< HEAD
# import smbus
import time
# import RPi.GPIO as GPIO
=======
import smbus, time
import RPi.GPIO as GPIO
>>>>>>> parent of 4f47939... test-over version
import numpy as np
import tornado.ioloop
import tornado.web
import json


class RcvData:

	def __init__(self):
		self.Point_Num = 1000
		self.Current_Point = 0
		self.Rcv_Vol = np.zeros(self.Point_Num, np.uint8)


<<<<<<< HEAD
# class RcvSignal(threading.Thread):
#
# 	def __init__(self):
# 		super(RcvSignal, self).__init__()
# 		self.address = 0x04
# 		self.Data = 0
# 		self.LSB = 0
# 		self.MSB = 0
# 		self.data_16 = 0
#
# 	def send_cmd(self, cmd):
# 		bus.write_byte(self.address, cmd)
# 		return -1
#
# 	def read_data(self):
# 		self.Data = bus.read_byte(self.address)
# 		return self.Data
#
# 	def read_data_16(self):
# 		self.LSB = bus.read_byte(self.address)
# 		self.MSB = bus.read_byte(self.address)
# 		#print LSB
# 		#print MSB
# 		#Data=bus.read_byte(address)
# 		self.data_16 = self.LSB + self.MSB*256
# 		if self.data_16 > 800:
# 			self.data_16 = 800
# 		if self.data_16 < 400:
# 			self.data_16 = 400
# 		return self.data_16
#
# 	def run(self):
# 		global rcv_data
# 		while True:
# 			time.sleep(0.01)
# 			lock.acquire()
# 			rcv_data.Rcv_Vol[rcv_data.Current_Point] = self.read_data_16()
# 			rcv_data.Current_Point += 1
# 			lock.release()


class RcvSignal(threading.Thread):
	def __init__(self):
		super(RcvSignal, self).__init__()
<<<<<<< HEAD
		self.test_array = random.sample(range(400, 800), 200)
		# print self.test_array
=======
class RcvSignal(threading.Thread):

	def __init__(self):
		super(RcvSignal, self).__init__()
		self.address = 0x04
		self.Data = 0
		self.LSB = 0
		self.MSB = 0

	def send_cmd(self, cmd):
		bus.write_byte(self.address, cmd)
		return -1

	def read_data(self):
		self.Data = bus.read_byte(self.address)
		return self.Data

	def read_data_16(self):
		self.LSB = bus.read_byte(self.address)
		self.MSB = bus.read_byte(self.address)
		#print LSB
		#print MSB
		#Data=bus.read_byte(address)
		return self.LSB + self.MSB*256
>>>>>>> parent of 4f47939... test-over version
=======
		self.test_array =
>>>>>>> parent of 0cb9bdb... test over

	def run(self):
		global rcv_data
		while True:
			time.sleep(0.01)
			lock.acquire()
<<<<<<< HEAD
			rcv_data.Rcv_Vol[rcv_data.Current_Point] = self.test_array[rcv_data.Current_Point]
<<<<<<< HEAD
			print rcv_data.Current_Point
=======
			rcv_data.Rcv_Vol[rcv_data.Current_Point] = self.read_data_16()
>>>>>>> parent of 4f47939... test-over version
=======
>>>>>>> parent of 0cb9bdb... test over
			rcv_data.Current_Point += 1
			lock.release()


class Process(threading.Thread):

	def __init__(self):
		super(Process, self).__init__()
		self.Num = 0
		self.Data = []
		self.distance = []
		self.Delta_Ang = 0
		self.Args = []
		self.Coord = []
		self.X_Coord = []
		self.Y_coord = []
		#self.proportion = 10000
		#self.diff = 555
		self.f = file('DV1.json')
		self.val = json.load(self.f)
		self.points = []
		self.img = []
		self.dir = '/home/pi/lidar_2d/images/image'
		self.file_number = 0
		self.file_name = ''

	def crt_line_image(self, x_coord, y_coord):
		self.img = np.zeros((512, 512), np.uint8)
		self.points = np.column_stack((x_coord, y_coord))
		cv2.polylines(self.img, [self.points], 1, 255)
		self.file_name = self.dir + format(self.file_number, '05d') + '.jpg'
		self.file_number += 1
		if self.file_number > 100:
			self.file_number = 0
		cv2.imwrite(self.file_name, self.img)
		subprocess.call(["cp", "-f", self.file_name, '/home/pi/lidar_2d/images/live.jpg'])


	def crt_point_image(self, x_coord, y_coord):
		self.img = np.zeros((512, 512), np.uint8)
		self.points = np.column_stack((x_coord, y_coord))
		for i in xrange(self.points.size/2):
			cv2.circle(self.img, tuple(self.points[i]), 3, 255, -1)
<<<<<<< HEAD
<<<<<<< HEAD
		# self.file_name = self.dir + format(self.file_number, '05d') + '.jpg'
		# self.file_number += 1
		# if self.file_number > 100:
		# 	self.file_number = 0
		# cv2.imwrite(self.file_name, self.img)
		# subprocess.call(["cp", "-f", self.file_name, '/home/pi/lidar_2d/images/live.jpg'])
		cv2.imwrite('./images/live.jpg', self.img)
=======
=======
>>>>>>> parent of 0cb9bdb... test over
		self.file_name = self.dir + format(self.file_number, '05d') + '.jpg'
		self.file_number += 1
		if self.file_number > 100:
			self.file_number = 0
		subprocess.call(["cp", "-f", self.file_name, '/home/pi/lidar_2d/images/live.jpg'])
		cv2.imwrite('/home/pi/lidar_2d/images/live.jpg', self.img)
<<<<<<< HEAD
>>>>>>> parent of 4f47939... test-over version
=======
>>>>>>> parent of 0cb9bdb... test over

	def process(self, num, array):
		self.Delta_Ang = np.pi*2 / num
		self.distance = np.zeros(num, np.float16)
		for i in range(num):
			self.distance[i] = self.val[str(array[i])]
<<<<<<< HEAD
<<<<<<< HEAD
		print 'distance:', self.distance
=======
>>>>>>> parent of 0cb9bdb... test over
		self.Args = np.array([i * self.Delta_Ang for i in range(0, num)])
		#self.distance = 1/array*self.proportion + self.diff
		#save as json
		self.Coord = self.distance/6*256
<<<<<<< HEAD
		print 'coord:', self.Coord
		for i in range(num):
			self.X_Coord[i] = np.cos(self.Args[i]) * self.Coord[i] + 256
			self.Y_Coord[i] = np.sin(self.Args[i]) * self.Coord[i] + 256
		# self.X_Coord = np.cos(self.Args)*self.distance
		print 'x_coord:', self.X_Coord
		# self.Y_coord = np.sin(self.Args)*self.distance
		self.crt_point_image(self.X_Coord, self.Y_Coord)
=======
		self.Args = np.array([i * self.Delta_Ang for i in range(0, num)])
		#self.distance = 1/array*self.proportion + self.diff
		#save as json
		self.Coord = self.distance/6*256
		self.X_Coord = np.cos(self.Args)*self.distance
		self.Y_coord = np.sin(self.Args)*self.distance
		self.crt_line_image(self.X_Coord, self.Y_coord)
>>>>>>> parent of 4f47939... test-over version
=======
		self.X_Coord = np.cos(self.Args)*self.distance
		self.Y_coord = np.sin(self.Args)*self.distance
		self.crt_line_image(self.X_Coord, self.Y_coord)
>>>>>>> parent of 0cb9bdb... test over

	def run(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(4, GPIO.IN)
		global rcv_data
		global complet_process
		#while True:
		#if GPIO.input(4) == 1:
		lock.acquire()
		complet_process = False
		self.Num = rcv_data.Current_Point
		self.Data = rcv_data.Rcv_Vol[:self.Num]
		# rcv_data.Current_Point = 0
		lock.release()
		self.process(self.Num, self.Data)
		complet_process = True


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html", title="My title")


class ImageHandler(tornado.web.StaticFileHandler):
	def set_extra_headers(self, path):
		self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')


class WebServer(threading.thread):

	def run(self):
		application = tornado.web.Application([
				(r"/", MainHandler),
				(r"/images/(.*)", ImageHandler, {"path": "./images"})])
		application.listen(8888)
		tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
	# bus = smbus.SMBus(1)
	lock = threading.Lock()
	signal = threading.Event()
	rcv_data = RcvData()
	complet_process = False

	rcv_signal = RcvSignal()
	# process = Process()
	web_server = WebServer()
	rcv_signal.start()
	# process.start()
	web_server.start()

	while True:
<<<<<<< HEAD
		# if GPIO.input == 1:
		lock.acquire()
		if complet_process:
			process = Process()
			process.start()
		else:
			rcv_data.Current_Point = 0
		lock.release()
		time.sleep(1)
=======
		if GPIO.input(4) == 1:
			lock.acquire()
			if complet_process:
				process = Process()
				process.start()
			else:
				rcv_data.Current_Point = 0
			lock.release()
>>>>>>> parent of 4f47939... test-over version
