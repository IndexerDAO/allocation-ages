from string import Template

def get_current_epoch():

  query = Template("""
  {
    epoches(orderBy: startBlock, orderDirection: desc, first: 1) {
      id
    }
  }
  """)

  return query.safe_substitute()

def get_old_allocations(wallet_address: str, oldest_allowable_epoch: int):
  query = Template("""
  {
    allocations(where: {activeForIndexer: "$address", createdAtEpoch_lt:$oldest_epoch},) {
      id,
      createdAtEpoch
      }
  }
  """)
  return query.safe_substitute(
    address=wallet_address, 
    oldest_epoch=oldest_allowable_epoch
    )

def get_open_allocations(wallet_address: str):
  query = Template("""
  {
    allocations(where: {activeForIndexer: "$address"}) {
      id,
      createdAtEpoch
      }
  }
  """)
  return query.safe_substitute(
    address=wallet_address
  )