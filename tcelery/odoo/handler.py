#! -*- coding:utf-8 -*-
import os
import sys
import logging

_logger = logging.getLogger(__name__)


class Handler(object):
    """
    odoo处理类
    """

    def __init__(self, OPENERP_PATH, WORK_PATH, CONF_PATH, dbname):
        self.CONF_PATH = CONF_PATH  # 配置文件完整路径
        self.WORK_PATH = WORK_PATH  # odoo工作目录
        self.OPENERP_PATH = OPENERP_PATH  # odoo路径
        self.dbname = dbname
        self._openerp_init = False
        self._registry_init = False

    def obj_apply(self, model, method, args=[], kwargs={}):
        with self.openerp.api.Environment.manage():
            with self.registry.cursor() as cr:
                model_obj = self.registry.get(model)
                return getattr(model_obj, method)(cr, self.openerp.SUPERUSER_ID, *args)

    @property
    def registry(self):
        if not self._registry_init:
            self._registry = self.openerp.modules.registry.RegistryManager.get(self.dbname)
            if self._registry:
                self._registry_init = True

        return self._registry

    @registry.setter
    def registry(self, value):
        if value:
            self._registry = value
        else:
            self._registry = None
            self._registry_init = False

    @property
    def openerp(self):
        if not self._openerp_init:
            self._openerp = self.get_openerp()
            if self._openerp:
                self._openerp_init = True

        return self._openerp

    @openerp.setter
    def openerp(self, value):
        if value:
            self._openerp = value
        else:
            self._openerp = None
            self._openerp_init = False

    def get_openerp(self):
        """
        根据代码路径加载配置文件
        @return:
        """
        sys.path.append(self.OPENERP_PATH)
        os.chdir(self.WORK_PATH)
        try:
            import openerp
            config = openerp.tools.config

            config.config_file = self.CONF_PATH
            config.parse_config()  # 加载配置文件,加载模块目录

            return openerp
        except:
            raise
        finally:
            sys.path.remove(self.OPENERP_PATH)
