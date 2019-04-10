from sqlnx.core import sqlnx


def test_sqlnx():
    g = sqlnx.make_sqlnx(dbfile=":memory:")
    print(g)
    print("REEE")

