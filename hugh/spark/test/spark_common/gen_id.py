#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

class GenId():

    @staticmethod
    def uuid():
        uid = str(uuid.uuid4())
        return ''.join(uid.split('-'))