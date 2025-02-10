from datetime import datetime, timezone
from __init__ import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.CURRENT_TIMESTAMP(),
        default=datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.current_timestamp(),
        default=lambda: datetime.now(timezone.utc),
        onupdate=db.func.current_timestamp()
    )
    deleted_at = db.Column(
        db.DateTime(timezone=True),
        default=None
    )

    def soft_delete(self):
        self.deleted_at = datetime.now(timezone.utc)
        db.session.commit()

    def restore(self):
        self.deleted_at = None
        db.session.commit()

    @property
    def is_deleted(self):
        return self.deleted_at is not None
