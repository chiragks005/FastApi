#Define the pydantic model that the FastAPI uses to validate incoming request bodies
#Pydantic models also shapes the outgoing response

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from App.models.user import UserRole