import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

bdd=[]
boc=[]
define("port", default=1024, help="run on the given port",type=int)
class Index(tornado.web.RequestHandler):
     
    def get(self):
         
         return self.render('aa.html',name=bdd,bod=boc)
         
    def post(self):
        
        if 'todolist' in self.request.arguments:
          if self.get_argument('todolist')!='':
            tod=self.get_argument('todolist')
            bdd.append(tod)
          return self.redirect('/')
            
        if 'text' in self.request.arguments:
         re=self.get_argument('text')
         l=0
         for idd in bdd :
            
            if idd==re:
                boc.append(re)
                del bdd[l]
                break
            
            l=l+1
         return self.redirect('/') 
        return self.render('aa.html',name=bdd,bod=boc)
          
       
if __name__ == '__main__':
   tornado.options.parse_command_line()
   app = tornado.web.Application(
        handlers=[(r"/", Index)],
        template_path=
        os.path.join(os.path.dirname(__file__),"templates"),
        static_path=os.path.join(os.path.dirname(__file__),"static"),
        debug=True)
   
   http_server = tornado.httpserver.HTTPServer(app)
   http_server.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()
