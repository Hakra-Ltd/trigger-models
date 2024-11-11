import datetime
from typing import Any

from pydantic import UUID4

from trigger_models.enum import FailureReason, ScrapType
from trigger_models.model import ScrapJobMessage


def get_success_job_message(
    event_id: str,
    job_id: UUID4,
    scrap_type: ScrapType,
    started: datetime.datetime,
    finished: datetime.datetime,
    scrap_notes: dict[str, Any] | None = None,
) -> ScrapJobMessage:
    return ScrapJobMessage(
        event_id=event_id,
        job_id=job_id,
        scrap_type=scrap_type,
        job_scrap_started_at=started,
        job_scrap_finished_at=finished,
        scrap_success=True,
        scrap_notes=scrap_notes,
    )


def get_error_job_message(
    event_id: str,
    job_id: UUID4,
    scrap_type: ScrapType,
    started: datetime.datetime,
    finished: datetime.datetime,
    scrap_notes: dict[str, Any],
    failure_reason: FailureReason,
) -> ScrapJobMessage:
    return ScrapJobMessage(
        event_id=event_id,
        job_id=job_id,
        scrap_type=scrap_type,
        job_scrap_started_at=started,
        job_scrap_finished_at=finished,
        scrap_success=False,
        scrap_notes=scrap_notes,
        failure_reason=failure_reason,
    )
