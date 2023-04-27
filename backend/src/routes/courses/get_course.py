#At some point add user permissions so not everybody can just make a course
from typing import Annotated
from datetime import timedelta, datetime

from fastapi import HTTPException, Header
from ...models import User, Course, CourseParticipant
from ...main import app
from pydantic import BaseModel
from ...utils import convert_to_json
from ..auth.auth_common import get_user_or_401

class CourseRequest(BaseModel):
    name: str
    description: str

@app.get("/course/{course_id}", response_model=Course)
async def get_course(authorization: Annotated[str, Header()]):
    requester = await get_user_or_401(authorization)

    course = await Course.objects.get_or_none(id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
    
