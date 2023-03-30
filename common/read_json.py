import json
import os
from config import config_path_del


def read_SystemCfg_json():
    """
    获取图片存储路径 /home/super/AI_Service/alarm_picture/download/image/
    :return:
    """
    try:
        with open(config_path_del + 'SystemCfg.json', 'r', encoding='utf-8') as f:
            systemcfg = json.load(f)
            systemcfg_path = systemcfg[0].get('alarm_file_path') + os.sep + 'download/image/'
            return systemcfg_path
    except Exception as e:
        print(e)


def read_CameraCfg_json():
    """
    获取相机的ip地址
    :return:
    """
    try:
        with open(config_path_del + 'CameraCfg.json', 'r', encoding='utf-8') as f:
            camera_files = json.load(f)
            camera_ip = list()
            for camera in camera_files:
                camera_ip.append(camera.get('ip'))
            return camera_ip

    except Exception as e:
        print(e)


def join_path():
    """
    获取所有相机的路径 /home/super/AI_Service/alarm_picture/download/image/192.168.60.250
    :return:
    """
    s_path = read_SystemCfg_json()
    ip_path = read_CameraCfg_json()
    path_list = list()
    for ip in ip_path:
        all_path = s_path + ip
        path_list.append(all_path)
    return path_list


if __name__ == '__main__':
    ipp = read_CameraCfg_json()
    for ip in ipp:
        print(type(ip))
    print(type(ipp))
    print(type(read_SystemCfg_json()))

