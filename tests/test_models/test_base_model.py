#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """testing Base Model"""
    def test_init(self):
        myModel = BaseModel()
        self.assertIsNotNone(myModel.id)
        self.assertIsNotNone(myModel.created_at)
        self.assertIsNotNone(myModel.updated_at)

    def test_save(self):
        myModel = BaseModel()
        first_updatedAt = myModel.updated_at
        new_updatedAt = myModel.save()
        self.assertNotEqual(first_updatedAt, new_updatedAt)

    def test_to_dict(self):
        myModel = BaseModel()
        model_dict = myModel.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], myModel.id)
        self.assertEqual(model_dict["created_at"],
                         myModel.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         myModel.updated_at.isoformat())

    def test_str(self):
        myModel = BaseModel()
        self.assertTrue(str(myModel).startswith("[BaseModel]"))
        self.assertIn(myModel.id, str(myModel))
        self.assertIn(str(myModel.__dict__), str(myModel))


if __name__ == "__main__":
    unittest.main()
