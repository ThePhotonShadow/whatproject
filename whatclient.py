import pip

def install(package):
    pip.main(['install', package])

try:
    import kivy
except:
    install('kivy')
    import kivy

try:
    import request
except:
    install('request')
    import kivy

class ConfigWindow(kivy.Widget):
    pass

class ConfigTool(kivy.App):
    def build(self):
        return ConfigWindow()

ConfigTool.run()