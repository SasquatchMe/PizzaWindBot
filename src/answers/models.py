from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.application.database import Base


class AnswerOrm(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id"),
    )
    is_correct: Mapped[bool]

    questions: Mapped["QuestionOrm"] = relationship(
        back_populates="answers",
    )
