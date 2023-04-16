#At some point add user permissions so not everybody can just make a course
from typing import Annotated
from datetime import timedelta, datetime

from fastapi import HTTPException, Header
from ...models import User, AuditLog, Course, CourseParticipant, OwnerType
from ...main import app
from pydantic import BaseModel
from ...utils import convert_to_json
from ..auth.auth_common import get_user_or_401, get_user_from_user_id
from .add_course import add_course_participant_audit_log

@app.post("/course/{course_id}/add_user", response_model=Course)
async def add_course_participant(authorization: Annotated[str, Header()], userId: int):
    course = await Course.objects.get_or_none(id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Question not found")
    
    adder = await get_user_or_401(authorization)

    #This may have performance implications, double check
    adder_in_course = await CourseParticipant.objects.get_or_none(uid=adder, cid=course)
    
    #Check that the adder is actually able to add the person they want to add
    if adder_in_course is None:
        #FIXME change status code
        raise HTTPException(status_code=404, detail="User is not in course")
    if not(adder_in_course.type < OwnerType.participant):
        raise HTTPException(status_code=404, detail="User does not have adequate permissions")

    #Check that the person we want to add exists and can be added
    added = await get_user_from_user_id(userId);
    if added is None:
        raise HTTPException(status_code=404, detail="User not found")
    added_in_course = await CourseParticipant.objects.get_or_none(uid=added, cid=course)
    if added_in_course is not None:
        raise HTTPException(status_code=404, detail="User already in course")

    #We are certain that the user can be added at this point, time to add them
    participant = CourseParticipant(
        uid = added,
        cid = course,
        type= OwnerType.participant
    )
    participant.save()
    add_course_participant_audit_log(participant, added, adder, "Manually added")

