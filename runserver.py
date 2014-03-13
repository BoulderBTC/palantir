from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from palantir import app
app.debug = True
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5005)
IOLoop.instance().start()
#app.run(debug=True, host='0.0.0.0', port=5005)
