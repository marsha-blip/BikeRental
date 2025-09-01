
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bikehire.db")
Base.metadata.create_all(engine)

target_metadata = Base.metadata