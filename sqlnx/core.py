import apsw
import attr
import typing
from typing import Any


@attr.s(auto_attribs=True, kw_only=True)
class DBManager:
    dbfile: str
    conn: apsw.Connection = attr.ib(init=False)
    cursor: Any = attr.ib(init=False)

    def __attrs_post_init__(self):
        conn = apsw.Connection(self.dbfile)
        object.__setattr__(self, "conn", conn)
        object.__setattr__(self, "cursor", conn.cursor())


@attr.s(auto_attribs=True)
class sqlnx:
    db: DBManager

    @classmethod
    def make_sqlnx(cls, *, dbfile: str):
        db = DBManager(dbfile=dbfile)
        return cls(db=db)
