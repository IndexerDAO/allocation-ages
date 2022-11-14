from string import Template
import time

def make_query(wallet_address, time_delta):
  timestamp = time.time()
  oldest_allowable_timestamp = (timestamp) - (time_delta*60)

  query = Template("""
  {
    allocations(
      where: {indexer: "$address", status: Active, createdAt_lt: $oldest_timestamp}
      orderBy: createdAt
      orderDirection: desc
    ) {
      id
      createdAt
    }
  }
  """)

  return query.safe_substitute(
    address=wallet_address, 
    oldest_timestamp=int(oldest_allowable_timestamp)
    )
  