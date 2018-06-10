# -*- coding: utf-8 -*-
'''
Create on June 9th 2018
@Author KEYS
'''
class Constants(object):

    # success
    SUCCESS_REGISTER = 'Registered successfully'
    SUCCESS_LOGIN = 'Login successfully'
    SUCCESS_GET_USER_BY_ID = 'Get the user by ID successfully'
    SUCCESS_AUTH_TOKEN = 'The user has permission'
    SUCCESS_TOKEN_ID = 'Get token_id successfully'

    # error
    ERROR_REGISTER_EXISTS = 'This user id is already registered'
    ERROR_USER_NOT_EXISTS = 'This user id does not exist'
    ERROR_AUTH_TOKEN = 'The user does not have permission'