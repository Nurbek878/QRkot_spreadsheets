from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_charityproject_id_by_name(self,
                                            charityproject_name: str,
                                            session: AsyncSession
                                            ) -> Optional[int]:
        db_charityproject_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charityproject_name))
        db_charityproject_id = db_charityproject_id.scalars().first()
        return db_charityproject_id

    async def get_fully_invested_projects(
        self,
        session: AsyncSession
    ) -> list:
        fully_invested_projects = await session.execute(
            select(CharityProject).where(CharityProject.fully_invested == 1)
        )
        return fully_invested_projects.scalars().all()

    async def get_projects_by_completion_rate(self, session: AsyncSession) -> list:
        projects = await self.get_fully_invested_projects(session)
        projects_for_sheets = [
            {
                'name': project.name,
                'duration': project.close_date - project.create_date,
                'description': project.description
            }
            for project in projects
        ]
        projects_for_sheets.sort(key=lambda x: x['duration'])
        return projects_for_sheets


charityproject_crud = CRUDCharityProject(CharityProject)
