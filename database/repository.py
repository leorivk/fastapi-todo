# Repository pattern

from typing import List

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database.orm import ToDo

def get_todos(session: Session) -> List[ToDo]:
    return list(session.scalars(select(ToDo)))


def get_todo_by_todo_id(session: Session, todo_id: int) -> ToDo | None:
    return session.scalar(select(ToDo).where(ToDo.id == todo_id))


def create_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo)
    session.commit()    # db에 저장 (Autocommit을 False로 지정했으므로 명시적으로 커밋)
    session.refresh(instance=todo)  # 저장된 todo 객체를 다시 가져온 후 todo_id 반영
    return todo # 데이터베이스에 완전히 반영된 todo 객체를 반환


def update_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo)
    session.commit()
    session.refresh(instance=todo)
    return todo


def delete_todo(session: Session, todo_id: int) -> None:
    session.execute(delete(ToDo).where(ToDo.id == todo_id))
    session.commit()