from uuid import UUID
from app.dto.base import PaginationBaseDTO
from app.dto.notes import NoteCreateDTO, NoteDTO, NoteUpdateDTO
from app.dto.users import UserDTO
from app.exceptions.notes import NoteException
from app.schemas.request.notes import NoteCreateSchema, NoteListSchema, NoteUpdateSchema
from app.uow.notes import INoteUoW


class NoteService:
    def __init__(self, note_uow: INoteUoW):
        self.note_uow = note_uow

    async def create_note(self, note_request: NoteCreateSchema, user_dto: UserDTO) -> NoteDTO | None:
        """
        Создание заметки

        Raises:
        """
        note_create_dto = NoteCreateDTO(
            content=note_request.content,
            author_id=user_dto.id,
        )
        async with self.note_uow:
            note_dto = await self.note_uow.note_repo.create_note(note_create_dto)
            return note_dto

    async def get_note(self, note_id: UUID, user_dto: UserDTO) -> NoteDTO | None:
        """
        Получение заметки

        Raises:
            NoteException.NoteNotFoundException
        """
        async with self.note_uow:
            note_dto = await self.note_uow.note_repo.get_note_by_user(note_id=note_id, user_id=user_dto.id)
            if not note_dto:
                raise NoteException.NoteNotFoundException(f"Note with id = '{note_id}' not found")
            return note_dto

    async def note_update(self, request_note: NoteUpdateSchema, note_id: UUID, user_dto: UserDTO) -> NoteDTO | None:
        """
        Изменение заметки

        Raises:
            NoteException.NoteNotFoundException
        """
        note_update_dto = NoteUpdateDTO(
            id=note_id,
            content=request_note.content,
            author_id=user_dto.id,
        )
        async with self.note_uow:
            note_dto = await self.note_uow.note_repo.update_note_by_user(note_update_dto)
            if not note_dto:
                raise NoteException.NoteNotFoundException(f"Note with id = '{note_id}' not found")
            return note_dto

    async def delete_note(self, note_id: UUID, user_dto: UserDTO) -> NoteDTO | None:
        """
        Удаление заметки

        Raises:
            NoteException.NoteNotFoundException
        """
        async with self.note_uow:
            note_dto = await self.note_uow.note_repo.delete_note_by_user(note_id=note_id, user_id=user_dto.id)
            if not note_dto:
                raise NoteException.NoteNotFoundException(f"Note with id = '{note_id}' not found")
            return note_dto

    async def get_note_list(self, note_request: NoteListSchema, user_dto: UserDTO) -> list[NoteDTO]:
        """
        Список заметок пользователя

        Raises:
        """
        pagination_dto = PaginationBaseDTO(page=note_request.page, limit=note_request.limit)  # type: ignore
        async with self.note_uow:
            notes = await self.note_uow.note_repo.note_list_by_user(
                user_id=user_dto.id,
                pagination_dto=pagination_dto,
            )
            return notes
