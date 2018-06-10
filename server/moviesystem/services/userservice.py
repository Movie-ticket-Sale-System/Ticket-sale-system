# -*- coding: utf-8 -*-
'''
Create on June 9th 2018
@Author KEYS
'''
from models.models import User
from models.ulity import Ulity
from models.constants import Constants

import traceback
import logging
logger = logging.getLogger('moviesys.app')

class UserService(object):

    def __init__(self):
        self.ulity = Ulity()

    def registerService(self, user):
        try:
            user_set = User.objects.filter(user_id=user.user_id)
            if len(user_set) != 0:
                return [1, Constants.ERROR_REGISTER_EXISTS]
            user.save()
            return [0, Constants.SUCCESS_REGISTER]
        except:
            error = traceback.format_exc()
            logger.error(error)
            return [-1, error]

    def loginService(self, user_id, password):
        try:
            user_set = User.objects.filter(user_id=user_id, password=password)
            if len(user_set) != 0:
                return [0, Constants.SUCCESS_LOGIN]
            return [1, Constants.ERROR_USER_NOT_EXISTS]
        except:
            error = traceback.format_exc()
            logger.error(error)
            return [-1, error]

    def getUserByIDService(self, user_id):
        try:
            user_set = User.objects.filter(user_id=user_id)
            if len(user_set) == 0:
                return [1, Constants.ERROR_USER_NOT_EXISTS, None]
            return [0, Constants.SUCCESS_GET_USER_BY_ID, user_set[0]]
        except:
            error = traceback.format_exc()
            logger.error(error)
            return [-1, error, None]

    def tokenVerifyUserServide(self, token):
        try:
            [flag, payload] = self.ulity.decodeTokenService(token)
            if flag:
                user_id = payload['user_id']
                password = payload['password']
                user_set = User.objects.filter(user_id=user_id, password=password)
                if len(user_set) != 0:
                    return [0, Constants.SUCCESS_AUTH_TOKEN, payload['user_id']]
            return [1, Constants.ERROR_AUTH_TOKEN, None]
        except:
            error = traceback.format_exc()
            logger.error(error)
            return [-1, error, None]