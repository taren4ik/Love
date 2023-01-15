import datetime

from love_prim.profiles.models import User


def age(request):
    """Возвращает возраст пользователя."""
    datetime_now = datetime.datetime.now()
    return {
        "age": datetime_now.year,
    }
