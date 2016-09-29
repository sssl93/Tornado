# coding:utf-8
import optparse
import ConfigParser


class ConfigManager(object):
    def __init__(self, fname=None):
        self.misc = {}
        self.options = {}
        self.config_file = fname
        self.parser = parser = optparse.OptionParser()
        parser.add_option("-c", "--config", dest="tornado_conf", help="specify alternate config file", default=False)
        # self.load()

    def load(self):
        p = ConfigParser.ConfigParser()
        (options, args) = self.parser.parse_args()
        self.config_file = options.tornado_conf
        try:
            p.read([self.config_file])
            for (name, value) in p.items('options'):
                if value == 'True' or value == 'true':
                    value = True
                if value == 'False' or value == 'false':
                    value = False
                self.options[name] = value
            # parse the other sections, as well
            for sec in p.sections():
                if sec == 'options':
                    continue
                if not self.misc.has_key(sec):
                    self.misc[sec] = {}
                for (name, value) in p.items(sec):
                    if value == 'True' or value == 'true':
                        value = True
                    if value == 'False' or value == 'false':
                        value = False
                    self.misc[sec][name] = value
        except IOError:
            pass
        except ConfigParser.NoSectionError:
            pass


tornado_conf = ConfigManager()
