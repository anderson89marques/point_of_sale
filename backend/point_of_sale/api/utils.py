"""Helper functions"""
import datetime


def period_dates(query_params):
    start_date_str = query_params.get('start_date', None)
    end_date_str = query_params.get('end_date', None)
    if not start_date_str or not end_date_str:
        raise Exception(
            "start_date and end_date must be used as query params in this format(yyyy-mm--dd).")
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%M-%d")
    end_date = datetime.datetime.strptime(
        end_date_str, "%Y-%M-%d") + datetime.timedelta(days=1)

    return start_date, end_date


def get_datetime(datetime_info):
    date_str = format_date(datetime_info)
    return datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')


def format_date(datetime_info):
    today = datetime.date.today()
    return f"{datetime.datetime.strftime(today, '%d/%m/%Y')} {datetime_info}"
