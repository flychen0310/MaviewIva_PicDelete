import os
import shutil
import time
import gevent
from gevent import monkey

monkey.patch_all()

# operate_path = '/home/super/image'
# bytes_to_GB = 1024 ** 3
# for root, dirs, files in os.walk(operate_path):
#     # print('root', root)
#     # print('dirs', dirs)
#     # print('files', files)
#     for file in files:
#         print(os.path.join(root, file))
#         print(os.path.getatime(os.path.join(root, file)))
#
#     print('\n')
#
# total, used, free = shutil.disk_usage(operate_path)
#
# print('total', total / bytes_to_GB)
# print('used', used / bytes_to_GB)
# print('free', free / bytes_to_GB)
# path = '/home/super/AI_Service/alarm_picture/download/image/1.1.1.22/2023-02-24_11_22_07_12.jpg'
# m_times = os.path.getmtime(path)
# now_time = time.time()
# g_time = now_time - m_times
# days = 4
# if g_time > days * 86400:
#     print(True)
# print(g_time)
# ip_list = list()
# del_two_ip = input("清输入删除图片的ip: ").split(',')
# print(type(del_two_ip))
# for ip in del_two_ip:
#     print(ip)
# del_types = input("请输入要删除的告警类型: ").split(',')
# print(type(del_types))
ip = '192.168.1.95'
# ip = ip.split(',')
for i in ip:
    print(i)
