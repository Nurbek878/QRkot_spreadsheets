from datetime import datetime
from aiogoogle import Aiogoogle

from app.services.constants import FORMAT, PERMISSIONS_BODY, SPREADSHEET_BODY, TABLE_VALUES


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    date_time_now = datetime.now().strftime(FORMAT)
    SPREADSHEET_BODY['properties']['title'] = f'Отчет на {date_time_now}'
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=SPREADSHEET_BODY)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=PERMISSIONS_BODY,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    date_time_now = datetime.now().strftime(FORMAT)
    TABLE_VALUES[0][1] = date_time_now
    service = await wrapper_services.discover('sheets', 'v4')
    for project in projects:
        new_row = [
            str(project['name']),
            str(project['duration']),
            str(project['description'])
        ]
        TABLE_VALUES.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': TABLE_VALUES
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
