# -*- coding: utf-8 -*-
"""
@author: Sarthak Mahapatra
"""
from pydantic import BaseModel
# 2. Class which describes Chemical Structure of Drug in Canonical Smiles
class Canonical(BaseModel):
    smiles: str