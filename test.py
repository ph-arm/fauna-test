from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(
  secret="Key",
  domain="db.us.fauna.com",
  # NOTE: Use the correct domain for your database's Region Group.
  port=443,
  scheme="https"
)

indexes = client.query(q.paginate(q.indexes()))

print(indexes)