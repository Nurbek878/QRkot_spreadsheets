from datetime import datetime

from app.core.config import settings


def get_current_time_formatted():
    FORMAT = "%Y/%m/%d %H:%M:%S"
    return datetime.now().strftime(FORMAT)


TABLE_VALUES = [
    ['Отчет от', get_current_time_formatted()],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']]
PERMISSIONS_BODY = {'type': 'user',
                    'role': 'writer',
                    'emailAddress': settings.email}
SPREADSHEET_BODY = {
    'properties': {'title': f'Отчёт от {get_current_time_formatted()}',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 11}}}]
}
