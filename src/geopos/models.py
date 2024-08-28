from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.application.database import Base

class GeoPosOrm(Base):
    __tablename__ = "geopositions"

    id: Mapped[int] = mapped_column(primary_key=True)
    longitude: Mapped[float]
    latitude: Mapped[float]
    description: Mapped[str] = mapped_column(nullable=True)

    questions: Mapped["QuestionOrm"] = relationship(back_populates='geopos')
