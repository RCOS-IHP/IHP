#At some point add user permissions so not everybody can just make a assignment
from typing import Annotated
from datetime import timedelta, datetime

from fastapi import HTTPException, Header
from ...models import User, AuditLog, Assignment, Course, OwnerType
from ...main import app
from pydantic import BaseModel
from ...utils import convert_to_json
from ..auth.auth_common import get_user_or_401

class AssignmentRequest(BaseModel):
    name: str
    description: str

@app.post("/course/{course_id}/add_assignment", response_model=Course)
async def add_assignment(authorization: Annotated[str, Header()], assignment: AssignmentRequest):
    user = await get_user_or_401(authorization)

    #Add some check here to make sure that the user has the authorization to 
    #make courses
    #FIXME
    assignment_model = Assignment(
        name= assignment.name,
        descript= assignment.description
    )
    assignment_model.save()
    add_assignment_audit_log(assignment_model, user)
    return assignment_model
    

async def add_assignment_audit_log(assignment: Assignment, user: User):
    event_data = {
        "assignment_name": assignment.name,
        "assignment_description": assignment.description
    }
    auditAddition = AuditLog(
        causing_user = user,
        #I don't like this, it wastes a lot of space. May be trimmed down
        event_data  = event_data,
        event_type = "add_assignment",
        effected_id = assignment.id,
        created_on = datetime.now(),
        expiry     = datetime.utcnow() + timedelta(days=365)
    )
    auditAddition.save()


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
    auditAddition.save()