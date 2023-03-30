from config import get_used_disk
from common.logging_use import init_log_config
from common.read_json import read_SystemCfg_json, read_CameraCfg_json
from del_db import del_db
from scripts import CleanAlarmImg
from gevent import monkey
import gevent

log_use = init_log_config('../del_log/del_pic.log')

monkey.patch_all()


def main():
    used_disk = get_used_disk()
    all_path = read_SystemCfg_json()  # 获取图片保存地址/home/super/AI_Service/alarm_picture/download/image/
    all_ip = read_CameraCfg_json()  # 获取配置文件里的ip
    clean_pic = CleanAlarmImg()
    # 前提 :占用硬盘超过80
    # if used_disk >= '1':   todo 到80

    """传入对应的相机IP地址和告警类型"""
    gevent.joinall(
        [
            gevent.spawn(del_db, '1.1.1.41',
                         '1,2,3,4,12', 1),
            gevent.spawn(clean_pic.del_more_camera_appoint_alert_pic, '1.1.1.41',
                         '1,2,3,4,12',
                         all_ip, all_path,
                         1)
        ])
    # clean_pic.del_more_camera_appoint_alert_pic('192.168.1.78,192.168.60.250,1.1.1.13,1.1.1.32',
    #                                             '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14',
    #                                             all_ip, all_path,
    #                                             0)


if __name__ == '__main__':
    main()
