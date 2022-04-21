"""Data models."""
import datetime
from . import db


class UsageStamp(db.Model):
    """
    Data model for usage stamps.
    """

    __tablename__ = 'usage-stamps'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    current_month_download = db.Column(
        db.Integer,
        index=False,
        nullable=False
    )
    current_month_upload = db.Column(
        db.Integer,
        index=False,
        nullable=False
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(datetime.timezone.utc),
        nullable=False
    )

    def __repr__(self):
        return '<Usage Stamp {}>'.format(self.created_at)
