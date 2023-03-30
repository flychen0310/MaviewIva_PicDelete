import os

BASE_DIR = os.path.dirname(__file__)

config_path_del = '/home/super/AI_Service/config_file/'


def get_used_disk():
    # 获取磁盘使用情况
    statvfs = os.statvfs('/home/super/AI_Service/alarm_picture/download/image')
    # 磁盘总大小
    disk_size = statvfs.f_frsize * statvfs.f_blocks
    # 磁盘使用大小
    disk_used = statvfs.f_frsize * (statvfs.f_blocks - statvfs.f_bfree)
    disk_percent = disk_used * 100 / disk_size
    disk_percent = '%.2f' % disk_percent
    return disk_percent


if __name__ == '__main__':
    print(get_used_disk())
