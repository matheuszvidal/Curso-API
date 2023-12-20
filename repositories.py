from sqlalchemy.orm import Session

from models import Curso


class CursoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Curso]:
        return db.query(Curso).all()

    @staticmethod
    def upsert(db: Session, curso: Curso) -> Curso:
        db.merge(curso) if curso.id else db.add(curso)
        db.commit()
        return curso
        # index = int(bool(curso.id))
        # actions = (db.add, db.merge)
        # (actions[index & 1] or actions[index ^ 1])(curso)
        # db.commit()
        # return curso

    @staticmethod
    def find_by_id(db: Session, id: int) -> Curso:
        return db.query(Curso).filter(Curso.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Curso).filter(Curso.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(Curso).filter(Curso.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()
