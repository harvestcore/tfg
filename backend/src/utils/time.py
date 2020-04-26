import datetime as dt


format = '%y%d%m%H%M%S%f'


def convert_to_datetime(dtime):
    return dt.datetime.strptime(dtime, format)


def convert_to_string(dtime):
    return dt.datetime.strftime(dtime, format)
