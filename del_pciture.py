#! /usr/bin/python3
# coding=utf-8

import os
import time
import multiprocessing


def del_pic(all_path, file, days, now_time, alarm_type):
    file_path = os.path.join(all_path, file)
    # print(file_path[46:])
    if (file_path[46:] == alarm_type + '.jpg') and (now_time - os.path.getatime(file_path)) > float(days * 86400):
        os.remove(file_path)
        print("图片已经删除", file_path)
    # else:
    #     print(False)


def main():
    # 获取磁盘使用情况
    statvfs = os.statvfs('/')
    # 磁盘总大小
    disk_size = statvfs.f_frsize * statvfs.f_blocks
    # 磁盘使用大小
    disk_used = statvfs.f_frsize * (statvfs.f_blocks - statvfs.f_bfree)
    disk_percent = disk_used * 100 / disk_size
    disk_percent = '%.2f' % disk_percent
    # print(type(disk_percent))
    # 创建进程池
    po = multiprocessing.Pool(10)
    try:
        # 判断磁盘使用率是否超过80
        if disk_percent > str(80):
            del_camera = input("请输入删除相机照片的ip地址: ")
            alarm_type = input("请输入要删除的告警类型: ")
            all_path = '/home/super/image/' + del_camera
            days = input("输入删除超出天数: ")
            # 获取当前时间
            now_time = time.time()
            for file in os.listdir(all_path):
                # 执行删除
                po.apply_async(del_pic, args=(all_path, file, days, now_time, alarm_type))
        po.close()
        po.join()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
