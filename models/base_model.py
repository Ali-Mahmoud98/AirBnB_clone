#!/usr/bin/python3
"""
A foundational module for creating and managing
base model instances.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class providing essential functionality for data models."""
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel.

        Args:
            *args (any): unused
            **kargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Save the current state of the instance."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Convert the instance to a dictionary for serialization."""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
