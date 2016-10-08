# coding=utf-8
import odoorpc
import logging

_logger = logging.getLogger(__name__)

smcc_domain = '192.168.1.183'
smcc_port = '48090'
smcc_db = 'third_contact'
smcc_admin = 'system'
smcc_admin_pwd = 'admin'
default_deploye_type = None

if __name__ == '__main__':
    odoo = odoorpc.ODOO(smcc_domain, port=smcc_port)
    odoo.login(smcc_db, smcc_admin, smcc_admin_pwd)
    articles = [{
        "title": "news now",
        "description": "Description...",
        "url": "https://www.baidu.com",
        "picurl": "http://ins48090.h10d.com/web/image/wx.app.info/10/picture"
    }]
    # odoo.env['permission.group'].news_message_send(2, agentid=88, usersids=['liangb'], articles=articles)
    odoo.env['corp.session'].get_access_token()
