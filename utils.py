from datetime import datetime
import pytz
import jdatetime
from hijri_converter import Gregorian


def get_time_info(timezone):
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)

    gregorian_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # تاریخ شمسی
    shamsi = jdatetime.datetime.fromgregorian(datetime=now)
    shamsi_date = shamsi.strftime("%Y/%m/%d")

    # تاریخ قمری
    hijri = Gregorian(now.year, now.month, now.day).to_hijri()
    hijri_date = f"{hijri.year}/{hijri.month:02}/{hijri.day:02}"

    return {
        "time": current_time,
        "gregorian": gregorian_date,
        "shamsi": shamsi_date,
        "hijri": hijri_date,
    }
