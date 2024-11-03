from typing import List, Optional, Dict, Any
from sqlmodel import SQLModel, Field, JSON
from pydantic import BaseModel


class BioGeneration(BaseModel):
    """Structured biography generated from LinkedIn profile data"""

    summary: str = Field(
        description="Concise professional summary highlighting key achievements"
    )
    interesting_facts: List[str] = Field(
        description="Two unique facts about the person", max_items=2
    )
    topics_of_interest: str = Field(
        description="Suggested conversation topic based on profile"
    )
    ice_breakers: List[str] = Field(
        description="Two relevant conversation starters", max_items=2
    )


class DBProfile(SQLModel, table=True):
    """Database model for storing LinkedIn profile data

    Attributes:
        url: The LinkedIn profile URL (primary key)
        person: Name of the person
        scrapped_data: Raw scraped data from the profile
        bio: Generated bio information
    """

    __tablename__ = "profiles"

    url: str = Field(
        primary_key=True, index=True, unique=True, description="LinkedIn profile URL"
    )

    person: str = Field(..., description="Name of the person")

    scrapped_data: Optional[Dict[str, Any]] = Field(
        default=None, sa_type=JSON, description="Raw scraped profile data"
    )

    bio: Optional[Dict[str, Any]] = Field(
        default=None, sa_type=JSON, description="Generated bio information"
    )
