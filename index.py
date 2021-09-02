#Import statements
from fastapi import FastAPI
from routes.student import student_router

#Create app
app = FastAPI()
#register your router
app.include_router(student_router)