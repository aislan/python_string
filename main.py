from extrator_argumento_url import ExtratorArgumentoUrl
url = "moedaorigem=real&moedadestino=dolar&valor=1500git"
argumento = ExtratorArgumentoUrl(url)
print(argumento.retorna_moedas())
