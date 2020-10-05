# coding=utf-8

from __future__ import absolute_import, unicode_literals, division, print_function

from .gmail import Gmail


def login(username, password):
    gmail = Gmail()
    gmail.login(username, password)
    return gmail


def authenticate(username, access_token):
    gmail = Gmail()
    gmail.authenticate(username, access_token)
    return gmail
