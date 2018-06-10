# -*- coding: utf-8 -*-
'''
Create on June 9th 2018
@Author KEYS
'''

from services.userservice import UserService
from models.models import User
from models.constants import Constants
from models.ulity import Ulity

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import simplejson

class UserControler(object):

    def __init__(self):
        self.user_service = UserService()
        self.ulity = Ulity()

    @csrf_exempt
    def registerControler(self, request):
        req = simplejson.loads(request.body)
        user = User(user_id=req['user']['user_id'], nike_name=req['user']['nike_name'],avatar_url=req['user']['avatar_url'],
                    gender=req['user']['gender'], telphone=req['user']['phone'], password=req['user']['password'],
                    email=req['user']['email'])
        res = {}
        status = 400
        [iRet, message] = self.user_service.registerService(user)
        if iRet == 0:
            status = 200
            res['status'] = 'OK'
        elif iRet == -1:
            status = 500
            res['status'] = 'Fail'
        elif iRet == 1:
            status = 200
            res['status'] = 'Fail'
        res['message'] = message
        return HttpResponse(content=simplejson.dumps(res), status=status)

    @csrf_exempt
    def loginControler(self, request):
        req = simplejson.loads(request.body)
        res = {}
        status = 400
        [iRet, message] = self.user_service.loginService(req['user_id'], req['password'])
        if iRet == 0:
            status = 200
            res['status'] = 'OK'
        elif iRet == -1:
            status = 500
            res['status'] = 'Fail'
        elif iRet == 1:
            status = 200
            res['status'] = 'Fail'
        res['message'] = message
        return HttpResponse(content=simplejson.dumps(res), status=status)

    @csrf_exempt
    def getUserByIdControler(self, request, user_id):
        res = {}
        status = 400
        [iRet, message, user] = self.user_service.getUserByIDService(user_id)
        if iRet == 0:
            status = 200
            res['status'] = 'OK'
            res['user'] = {}
            res['user']['user_id'] = user.user_id
            res['user']['nike_name'] = user.nike_name
            res['user']['avatar_url'] = user.avatar_url
            res['user']['time_create'] = str(user.time_created)
            res['user']['gender'] = user.gender
            res['user']['phone'] = user.telphone
            res['user']['email'] = user.email
        elif iRet == 1:
            status = 200
            res['status'] = 'Fail'
        elif iRet == -1:
            status = 500
            res['status'] = 'Fail'
        res['message'] = message
        return HttpResponse(content=simplejson.dumps(res), status=status)

    @csrf_exempt
    def tokenVerifyControler(self, request):
        token = request.META.get('HTTP_TOKEN')
        res = {}
        status = 400
        [iRet, message, user_id] = self.user_service.tokenVerifyUserServide(token)
        if iRet == 0:
            status = 200
            res['status'] = 'OK'
            res['user_id'] = user_id
        elif iRet == 1:
            status = 200
            res['status'] = 'Fail'
        elif iRet == -1:
            status = 500
            res['status'] = 'Fail'
        res['message'] = message
        return HttpResponse(content=simplejson.dumps(res), status=status)

    @csrf_exempt
    def getTokenControler(self, request):
        res = {}
        status = 400
        req = simplejson.loads(request.body)
        user_id = req['user_id']
        password = req['password']
        [iRet, message, user] = self.user_service.getUserByIDService(user_id)
        if iRet == 0:
            status = 200
            [iRet, message, token] = self.ulity.createTokenService(user_id, password)
            if iRet == 0:
                res['token_id'] = str(token)
                res['status'] = 'OK'
        if iRet == -1:
            status = 500
            res['status'] = 'Fail'
        if iRet == 1:
            status = 200
            res['status'] = 'Fail'
        res['message'] = message
        return HttpResponse(content=simplejson.dumps(res), status=status)

