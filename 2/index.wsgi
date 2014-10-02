#coding:UTF-8
import sae
import os
import web

from weixinInterface import WeixinInterface,douban

urls = (
    '/', 'Hello',
	'/weixin', 'WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

class Hello:
    def GET(self):
	    content = douban(ID=3)
	    return render.hello(content)
		
app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)