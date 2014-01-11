# coding: utf-8
import SocketServer
import SimpleHTTPServer
import os
# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/
DEFAULT_ERROR_MESSAGE = """\
    <head>
    <title>Error response</title>
    </head>
    <body>
    <h1>Error response</h1>
    <p>Error code %(code)d.
    <p>Message: %(message)s.
    <p>Error code explanation: %(code)s = %(explain)s.
    </body>
"""
class MyWebServer(SocketServer.BaseRequestHandler):
    code = 200
    buffer
    def handle(self):
        self.data = self.request.recv(1024).strip()
        request_list = self.data.split()
        path =request_list[1][1:]
        if path == '':
            path = 'index.html'
		try:
        	with open(path,'r') as f:
            	buffer = f.read()
            self.request.sendall(buffer)
		print ("Got a request of: %s\n" % self.data)
    def send_error(self, code, message=None):
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    os.chdir('www')
    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

