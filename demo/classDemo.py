# -*- coding : utf-8 -*-


class Dict(dict):

    def __init__(self,names=(),values=(),**kw):
        super(Dict, self).__init__(**kw)
        for k,v in zip(names,values):
            self[k]=v

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attrabuite '%s'"%key)

    def __setattr__(self,k,v):
        self[k]=v

print Dict.__subclasses__