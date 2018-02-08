from datetime import datetime

class DateConverter:
    regex = '[0-3][0-9]-[0-1][0-9]-[0-9]{4}'

    def to_python(self, value):
        # build a date object from input string
        try:
            return datetime.strptime(value, "%d-%m-%Y").date()
        except (AttributeError, ValueError) as err:
            return None

    def to_url(self, value):
        return value