from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import pytest

DATABASE_URL = "postgresql://postgres:111@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String, nullable=False)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def session():
    db_session = Session()
    yield db_session
    db_session.close()


def test_add_subject(session):
    new_subject = Subject(subject_id=1, subject_title="Math")
    session.add(new_subject)
    session.commit()
    subject = session.query(Subject).filter_by(subject_id=1).first()
    assert subject.subject_title == "Math"


def test_update_subject(session):
    new_subject = Subject(subject_id=2, subject_title="Science")
    session.add(new_subject)
    session.commit()
    subject = session.query(Subject).filter_by(subject_id=2).first()
    subject.subject_title = "Biology"
    session.commit()
    updated_subject = session.query(Subject).filter_by(subject_id=2).first()
    assert updated_subject.subject_title == "Biology"


def test_delete_subject(session):
    new_subject = Subject(subject_id=3, subject_title="History")
    session.add(new_subject)
    session.commit()
    session.delete(new_subject)
    session.commit()
    deleted_subject = session.query(Subject).filter_by(subject_id=3).first()
    assert deleted_subject is None
