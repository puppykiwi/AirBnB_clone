#!/usr/bin/python3
'''This qill be the base class'''
import uuid
from datetime import datetime as date
from models import storage


class BaseModel:
    '''Contains the building objects'''
    def __init__(self, *args, **kwargs):
        '''creates instance attributes'''
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        val = date.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = date.now()
            self.updated_at = date.now()
            storage.new(self)

    def __str__(self):
        '''returns a string of info'''
        return ("[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__))

    def save(self):
        '''updates the updated_at attr'''
        self.updated_at = date.now()
        storage.save()

    #def to_dict(self):
        '''creates a dictionary containing all attributes'''
        mydict = {}
        mydict["__class__"] = type(self).__name__
        for (key, val) in self.__dict__.items():
            if key == "created_at":
                mydict[key] = date.isoformat(val)
            elif key == "updated_at":
                mydict[key] = date.isoformat(val)
            else:
                mydict[key] = val
        return mydict

    def to_dict(self):
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = type(self).__name__
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        return base_dict

