from string import Template

def make_query(wallet_address):
  query = Template("""
  {
    allocations(
      where: {indexer: "$address"}
      orderBy: createdAt
      orderDirection: desc
    ) {
      id
      status
      closedAt
      createdAt
    }
  }
  """)

  return query.safe_substitute(address=wallet_address)