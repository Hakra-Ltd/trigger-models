import datetime
from typing import Any, Optional

from pydantic import UUID4, BaseModel, model_validator

from trigger_models.enum import FailureReason, ScrapType


class JobRunMessage(BaseModel):
    job_run_id: UUID4
    event_id: str
    scrap_type: ScrapType
    run_config: dict[str, Any] | None
    reporting: bool | None = None


class JobScrapMessage(BaseModel):
    event_id: str
    job_id: UUID4
    scrap_type: ScrapType | None = None
    process_initiated_at: datetime.datetime | None = None
    job_scrap_started_at: datetime.datetime | None = None
    job_scrap_finished_at: datetime.datetime | None = None
    process_finished_at: datetime.datetime | None = None
    scrap_success: Optional[bool] = None
    process_success: Optional[bool] = None
    failure_reason: FailureReason | None = None
    scrap_notes: Optional[dict[str, Any]] | None = None
    process_notes: Optional[dict[str, Any]] | None = None

    @model_validator(mode="before")
    def check_failure_reason(cls: Any, values: Any) -> Any:
        if values["failed"] and values.get("failure_reason") is None:
            raise ValueError("failure_reason must be provided if the job failed.")

        return values
