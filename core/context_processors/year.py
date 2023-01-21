import datetime


def year(request,*args):
    """Добавляет переменную с текущим годом."""
    datetime_now = datetime.datetime.now()
    return {
        "year": datetime_now.year,
    }
