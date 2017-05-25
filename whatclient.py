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

