#coding:UTF-8
import hashlib
import web
import time
import lxml
import os
import random
from lxml import etree

import sae.const

class WeixinInterface:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    
    
    def GET(self):
        data = web.input()
        
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        
        token = "bruce"
        
        _list = [token, timestamp, nonce]
        _list.sort()
        
        sha1 = hashlib.sha1()
        map(sha1.update, _list)
        hashcode = sha1.hexdigest()
        
        if hashcode == signature:
            return echostr
        
    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        
        #content = xml.find("Content").text
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        
        id = random.randint(1, 900)
        content = douban(id)
        
        return self.render.reply_text(fromUser, toUser, int(time.time()), content)

       
def douban(ID):
    
    #take an ID, return the user and the comment
    
    db = web.database(dbn='mysql', port=int(sae.const.MYSQL_PORT), host=sae.const.MYSQL_HOST,
        db=sae.const.MYSQL_DB, user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS)
    comment = db.select("comments", what="user_name, comment", where="ID=%d"%int(ID))
    for item in comment:
        content = u"用户：" + item.user_name + u"\n" + u"评论：" + item.comment
        
    return content

     
       
    