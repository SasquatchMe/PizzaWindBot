from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.application.database import Base


class QuestionOrm(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    geopos_id: Mapped[int] = mapped_column(ForeignKey("geopositions.id"), nullable=True)
    # created_at: Mapped[datetime] = mapped_column(auto_now_add=True)
    # updated_at: Mapped[datetime] = mapped_column(auto_now=True)

    geopos = relationship(
        "GeoPosOrm",
        back_populates="questions",
    )
    answers = relationship(
        "AnswerOrm", back_populates="questions", cascade="all, delete, delete-orphan"
    )
