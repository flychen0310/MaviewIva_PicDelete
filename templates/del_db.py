from CleanPicBasic import CleanBasic
from common.db_utils import DBUtils
from common.logging_use import init_log_config

log_use = init_log_config('../del_log/del_pic.log')


def del_db(camera_path: str, alarm_type: str, days: int):
    """
    删除数据库
    :param camera_path: 相机ip
    :param alarm_type: 事件类型
    :param days:
    :return:
    """
    db = DBUtils()
    alarm_paths = CleanBasic().get_alarm_paths(camera_path, alarm_type, days)
    try:
        for alarm_path in alarm_paths:
            sql = f"DELETE FROM alarm_audit as aa INNER JOIN alarm_detail as ad on aa.alarm_id=ad.id where " \
                  f"ad.pic_path={alarm_path};"
            db.udi_data(sql)
            log_use.info(f"{alarm_path}在数据库中已经删除....")
    except Exception as e:
        print("数据库删除失败", e)
