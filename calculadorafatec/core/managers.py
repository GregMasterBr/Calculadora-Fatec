from django.db import models

class KindQuerySet(models.QuerySet):
    #CONTATOS
    def emails(self):
        return self.filter(kind = self.model.EMAIL)
    
    def phones(self):
        return self.filter(kind = self.model.PHONE)

    def whatsapps(self):
            return self.filter(kind = self.model.WHATSAPP)

    #SOCIAL
    def sites(self):
            return self.filter(kind = self.model.SITE)

    def facebooks(self):
            return self.filter(kind = self.model.FACEBOOK)   

    def instagrams(self):
            return self.filter(kind = self.model.INSTAGRAM)                 
    
    def youtubes(self):
            return self.filter(kind = self.model.YOUTUBE)                 

    def linkedins(self):
            return self.filter(kind = self.model.LINKEDIN)   

    def twitters(self):
            return self.filter(kind = self.model.TWITTER)                 
    
    def blogs(self):
            return self.filter(kind = self.model.BLOG)     

    def outros(self):
            return self.filter(kind = self.model.OUTROS)     
   