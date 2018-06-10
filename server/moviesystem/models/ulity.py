# -*- coding: utf-8 -*-
'''
Create on June 9th 2018
@Author KEYS
'''

import jwt, time, traceback
from constants import Constants
import logging
logger = logging.getLogger('moviesys.app')

class Ulity(object):

    def __init__(self):
        pass

    def createTokenService(self, user_id, password):
        try:
            payload = {
                "iss": "moviesys.pro",
                "iat": int(time.time()),
                "exp": int(time.time() + 86400 * 7),
                "aud": "moviesys.pro",
                "user_id": user_id,
                "password": password,
                "scops": ['open']
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            return [0, Constants.SUCCESS_TOKEN_ID,token]
        except:
            error = traceback.format_exc()
            logger.error(error)
            return [-1, error, None]



    def decodeTokenService(self, token):
        payload = jwt.decode(token, 'secret', audience='moviesys.pro', algorithms=['HS256'])
        if payload:
            return [True, payload]
        return [False, None]