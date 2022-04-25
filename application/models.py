"""Data models."""
from dataclasses import dataclass
import datetime
from .extensions import db
from decimal import Decimal


@dataclass
class UsageStamp(db.Model):  # pylint: disable=too-few-public-methods
    """
    Data model for usage stamps.
    """
    current_month_download: Decimal
    current_month_upload: Decimal
    time_stamp: datetime.datetime

    __tablename__ = 'usage-stamps'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    current_month_download = db.Column(
        db.Numeric(precision=10, scale=3),
        index=False,
        nullable=False
    )
    current_month_upload = db.Column(
        db.Numeric(precision=10, scale=3),
        index=False,
        nullable=False
    )
    time_stamp = db.Column(
        db.DateTime,
        index=True,
        unique=True,
        nullable=False
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
        onupdate=datetime.datetime.now(datetime.timezone.utc)
    )

    def __repr__(self):
        return (f'<Usage Stamp {self.current_month_download}/'
                f'{self.current_month_upload} | {self.time_stamp} >')
