import pip

try:
    import eve
except:
    def install(package):
        pip.main(['install', package])
    install('eve')
    import eve

