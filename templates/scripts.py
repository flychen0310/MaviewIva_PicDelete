from CleanPicBasic import CleanBasic
from common.logging_use import init_log_config

log_use = init_log_config('../del_log/del_pic.log')


class CleanAlarmImg(CleanBasic):

    def del_more_camera_appoint_alert_pic(self, del_camera_ip: str, del_types: str, all_ip: list, all_path: str,
                                          days: int):
        """
        删除多个(2个以上)相机下指定类型的告警图片
        :param del_camera_ip: 多个ip地址
        :param del_types: 多个指定的告警类型
        :param all_ip:
        :param all_path:
        :param days:
        :return:
        """
        try:
            path_list = list()
            del_camera_ip = del_camera_ip.split(',')
            del_types = del_types.split(',')
            for ip in del_camera_ip:
                # print(ip)
                if ip in all_ip:
                    path = all_path + ip
                    path_list.append(path)
                else:
                    print("{}不存在".format(ip))
            for del_type in del_types:
                self.delete_alarm_by_types(path_list, del_type, days)
        except Exception as e:
            print("删除多个相机下指定类型的告警图片失败", e)
