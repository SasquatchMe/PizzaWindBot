from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.application.database import Base


class PromocodeORM(Base):
    __tablename__ = "promocode"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    corrects: Mapped[int]
    is_active: Mapped[bool] = mapped_column(default=True)
