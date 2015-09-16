# coding: utf-8
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

from pydocx.models import XmlModel, XmlContent


class FieldCode(XmlModel):
    XML_TAG = 'instrText'

    text = XmlContent()
