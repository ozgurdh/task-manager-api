from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session
from app.database import create_db_and_tables, get_session
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from app import crud

app = FastAPI(
    title="Task Manager API",
    description="A simple REST API for managing tasks.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}

@app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, session: Session = Depends(get_session)):
    return crud.create_task(session, task_data)

@app.get("/tasks", response_model=list[TaskRead])
def get_tasks(session: Session = Depends(get_session)):
    return crud.get_tasks(session)

@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = crud.get_task_by_id(session, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@app.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_data: TaskUpdate, session: Session = Depends(get_session)):
    task = crud.get_task_by_id(session, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return crud.update_task(session, task, task_data)

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = crud.get_task_by_id(session, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    crud.delete_task(session, task)
    return None