from sqlalchemy.orm import mapped_column, Mapped

from src.application.database import Base


class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    tg_id: Mapped[int]
