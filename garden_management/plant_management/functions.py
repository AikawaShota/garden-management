import datetime
from django.utils.timezone import make_naive


def get_watering_state(last_watering_date, watering_frequency):
    """水やりの状態を返す関数。

    水やりの状態（水やりの要否と表示するメッセージ）を返す関数です。
    PlantListViewで利用します。

    Args:
        last_watering_date (datetime): 最後に水やりをした日付。
        watering_frequency (timedelta): 水やりをする頻度。

    Returns:
        dict: 水やりの要否(boolean)を表すrequiredと、表示する文章(str)を表すmessageを要素に持った辞書。
    """
    # tzinfoメソッドでタイムゾーンを含むか判定。
    if last_watering_date.tzinfo is not None:
        # タイムゾーン情報を消す。
        last_watering_date = make_naive(last_watering_date)
    time_difference = (
        last_watering_date + watering_frequency - datetime.datetime.now()
    )
    watering_state = {
        "required": False,
        "message": ""
    }
    if time_difference < datetime.timedelta():
        watering_state["required"] = True
        watering_state["message"] = "水やり"
    else:
        if time_difference.days > 0:
            watering_state["message"] += f"{time_difference.days}d, "
        watering_state["message"] += f"{time_difference.seconds // 60 // 60}h"
    return watering_state
