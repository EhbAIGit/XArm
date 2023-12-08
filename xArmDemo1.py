#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2023, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
# Notice
#   1. Changes to this file on Studio will not be preserved
#   2. The next conversion will overwrite the file with the same name
"""
import sys
import math
import time
import datetime
import random
import traceback
import threading

"""
# xArm-Python-SDK: https://github.com/xArm-Developer/xArm-Python-SDK
# git clone git@github.com:xArm-Developer/xArm-Python-SDK.git
# cd xArm-Python-SDK
# python setup.py install
"""
try:
    from xarm.tools import utils
except:
    pass
from xarm import version
from xarm.wrapper import XArmAPI

def pprint(*args, **kwargs):
    try:
        stack_tuple = traceback.extract_stack(limit=2)[0]
        print('[{}][{}] {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1], ' '.join(map(str, args))))
    except:
        print(*args, **kwargs)

pprint('xArm-Python-SDK Version:{}'.format(version.__version__))

arm = XArmAPI('10.2.172.20')
arm.clean_warn()
arm.clean_error()
arm.motion_enable(True)
arm.set_mode(0)
arm.set_state(0)
time.sleep(1)

variables = {}
params = {'speed': 100, 'acc': 2000, 'angle_speed': 20, 'angle_acc': 500, 'events': {}, 'variables': variables, 'callback_in_thread': True, 'quit': False}


# Register error/warn changed callback
def error_warn_change_callback(data):
    if data and data['error_code'] != 0:
        params['quit'] = True
        pprint('err={}, quit'.format(data['error_code']))
        arm.release_error_warn_changed_callback(error_warn_change_callback)
arm.register_error_warn_changed_callback(error_warn_change_callback)


# Register state changed callback
def state_changed_callback(data):
    if data and data['state'] == 4:
        if arm.version_number[0] > 1 or (arm.version_number[0] == 1 and arm.version_number[1] > 1):
            params['quit'] = True
            pprint('state=4, quit')
            arm.release_state_changed_callback(state_changed_callback)
arm.register_state_changed_callback(state_changed_callback)


# Register counter value changed callback
if hasattr(arm, 'register_count_changed_callback'):
    def count_changed_callback(data):
        if not params['quit']:
            pprint('counter val: {}'.format(data['count']))
    arm.register_count_changed_callback(count_changed_callback)


# Register connect changed callback
def connect_changed_callback(data):
    if data and not data['connected']:
        params['quit'] = True
        pprint('disconnect, connected={}, reported={}, quit'.format(data['connected'], data['reported']))
        arm.release_connect_changed_callback(error_warn_change_callback)
arm.register_connect_changed_callback(connect_changed_callback)

if arm.error_code == 0 and not params['quit']:
    arm.set_pause_time(1)
if arm.error_code == 0 and not params['quit']:
    arm.reset()
if not params['quit']:
    params['angle_speed'] = 20
for i in range(int(3)):
    if params['quit']:
        break
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[0.0, -53.0, 0.0, 47.7, 0.0, 98.4, 20.0], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[-1.4, 4.6, 1.5, 93.3, -0.1, 86.5, 20.1], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[0.8, 38.2, -0.7, 59.7, 1.3, 19.3, 19.1], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[-1.4, 4.6, 1.5, 93.3, -0.1, 86.5, 20.1], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[90.0, -53.0, 0.0, 47.7, 0.0, 98.4, 20.0], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[69.5, -16.0, 17.0, 72.2, 4.8, 85.3, 15.6], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[73.6, 29.6, 10.9, 39.7, -31.6, 9.7, 44.1], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.set_pause_time(0.5)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_servo_angle(angle=[69.5, -16.0, 17.0, 72.2, 4.8, 85.3, 15.6], speed=params['angle_speed'], mvacc=params['angle_acc'], wait=True, radius=0.0)
        if code != 0:
            params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        arm.reset()

# release all event
if hasattr(arm, 'release_count_changed_callback'):
    arm.release_count_changed_callback(count_changed_callback)
arm.release_error_warn_changed_callback(state_changed_callback)
arm.release_state_changed_callback(state_changed_callback)
arm.release_connect_changed_callback(error_warn_change_callback)
