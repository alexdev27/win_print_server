from typing import List

from pydantic import BaseModel, Field


class RequestStrings(BaseModel):
    data: List[str] = Field(..., title='List of strings to print', min_items=1)
