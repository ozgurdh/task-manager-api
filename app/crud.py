from sqlmodel import Session, select
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

def create_task(session: Session, task_data: TaskCreate) -> Task:
    task = Task.model_validate(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_tasks(session: Session) -> list[Task]:
    statement = select(Task)
    return session.exec(statement).all()

def get_task_by_id(session: Session, task_id: int) -> Task | None:
    return session.get(Task, task_id)

def update_task(session: Session, task: Task, task_data: TaskUpdate) -> Task:
    task_dict = task_data.model_dump(exclude_unset=True)

    for key, value in task_dict.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete_task(session: Session, task: Task) -> None:
    session.delete(task)
    session.commit()