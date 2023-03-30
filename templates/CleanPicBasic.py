import os
import time
from common.logging_use import init_log_config

log_use = init_log_config('../del_log/del_pic.log')


class CleanBasic:

    def get_alarm_paths(self, camera_path_list, alarm_type, days):
        """
        获取相机路径下所有告警图片的路径
        :param camera_path_list:
        :param alarm_type:
        :param days:
        :return:
        """
        alarm_paths = []
        # 获取/home/super/AI_Service/alarm_picture/download/image/下所有相机产生图片的路径
        for path in camera_path_list:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 获取当前时间
                    now_time = time.time()
                    # 获取图片访问的时间
                    file_time = os.path.getmtime(file_path)
                    # 截取时间差-->得到s
                    gap_time = now_time - file_time
                    if file.endswith(f'{alarm_type}.jpg') and gap_time >= days * 86400:
                        log_use.info(f'时差为:{gap_time / 86400},对应的照片路径{file_path}已经添加成功----')
                        alarm_paths.append(file_path)
                    else:
                        print("事件类型不存在或者没有超过该天数")
        # print(alarm_paths)
        return alarm_paths

    def delete_alarm_by_types(self, camera_path_list, alarm_type, days):
        alarm_paths = self.get_alarm_paths(camera_path_list, alarm_type, days)
        for alarm_path in alarm_paths:
            # if alarm_path.endswith(f'{alarm_type}.jpg'):
            os.remove(alarm_path)
            log_use.info(f"{alarm_path}已经删除成功-------")
