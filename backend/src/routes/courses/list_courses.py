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

@app.get("/course", response_model=Course)
async def add_course_participant(authorization: Annotated[str, Header()], userId: int):
    return await Course.objects.all()