#At some point add user permissions so not everybody can just make a course
from typing import Annotated
from datetime import timedelta, datetime

from fastapi import HTTPException, Header
from ...models import User, AuditLog, Course, CourseParticipant, OwnerType
from ...main import app
from pydantic import BaseModel
from ...utils import convert_to_json
from ..auth.auth_common import get_user_or_401

class CourseRequest(BaseModel):
    name: str
    description: str

@app.post("/course", response_model=Course)
async def add_course(authorization: Annotated[str, Header()], course: CourseRequest):
    user = await get_user_or_401(authorization)

    #Add some check here to make sure that the user has the authorization to 
    #make courses
    #FIXME
    course_model = Course(
        name= course.name,
        descript= course.description
    )
    await course_model.save()
    add_course_audit_log(course_model, user)
    participant = CourseParticipant(
        uid = user,
        cid = course_model,
        type= OwnerType.creator
    )
    await participant.save()
    add_course_participant_audit_log(participant, user, user, "Course was created")
    return course_model

async def add_course_audit_log(course: Course, user: User):
    event_data = {
        "course_name": course.name,
        "course_description": course.descript
    }
    auditAddition = AuditLog(
        causing_user = user,
        #I don't like this, it wastes a lot of space. May be trimmed down
        event_data  = event_data,
        event_type = "add_course",
        effected_id = course.id,
        created_on = datetime.now(),
        expiry     = datetime.utcnow() + timedelta(days=365)
    )
    await auditAddition.save()


async def add_course_participant_audit_log(course: CourseParticipant, userAdded: User, userAdder: User, cause: str):
    event_data = {
        "Added": {
            "username": userAdded.username,
            "email": userAdded.email,
            "user_id": userAdded.id, 
            "cause": cause
        }, 
        "Adder": {
            "username": userAdder.username,
            "email": userAdder.email,
            "user_id": userAdder.id, 
            "cause": cause
        }
    }
    auditAddition = AuditLog(
        causing_user = userAdder,
        #I don't like this, it wastes a lot of space. May be trimmed down
        event_data  = event_data,
        event_type = "add_course_participant",
        effected_id = course.id,
        created_on = datetime.now(),
        expiry     = datetime.utcnow() + timedelta(days=365)
    )
    await auditAddition.save()