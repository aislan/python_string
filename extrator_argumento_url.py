class ExtratorArgumentoUrl:
    def __init__(self,url):
        if url.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!")
    
    def url_eh_valida(self,url):
        if url:
            return True
        else:
            return False
    
