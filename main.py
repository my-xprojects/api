from typing import Optional
from fastapi import FastAPI, HTTPException
from datetime import date
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    title: str
    description: str
    due_date: date
    priority: str
    assignee: str

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    priority: Optional[str] = None
    assignee: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

tasks = {
    0: {
        "title": "ahmad",
        "description": "trying to edit weeeeeeee two",
        "due_date": "2024-01-22",
        "priority": "medium",
        "assignee": "me"
    },
    1: {
        "title": "moh",
        "description": "trying to edit weeeeeeee third",
        "due_date": "2024-01-23",
        "priority": "medium",
        "assignee": "me"
    }
}

@app.get("/tasks/")
async def read_item():
    return tasks

@app.post("/create-task/{task_id}")
async def create_task(task_id: str, task: Task):
    if task_id in tasks:
        raise HTTPException(status_code=400, detail="Task already exists")
    
    tasks[task_id] = task
    return tasks[task_id]

@app.put("/update-task/{task_id}")
async def update_task(task_id: str, updated_task: UpdateTask):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id] = updated_task
    return tasks[task_id]

@app.delete("/delete-task")
async def create_task(task_id: int):
    if(task_id not in tasks):
        return {"ERROR", "task not exist"}
    
    del tasks[task_id]
    return {"The task has been succsefuly deleted"}
