import tornado.ioloop
import tornado.web
import subprocess


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html", title="My title")


class ImageHandler(tornado.web.StaticFileHandler):
	def set_extra_headers(self, path):
		self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')


application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/images/(.*)", ImageHandler, {"path": "./images"})
	])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
