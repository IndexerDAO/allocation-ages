## Set up

### Use with your own wallet
* Fork the repo
* Create two repository secrets in the new repo
    * WALLET_ADDRESS: Address whose allocation ages will be monitored
    * WEBHOOK_URL: Discord Channel webhook url to post allocation monitor updates

### Local dev environment
``` bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

## Query

``` gql
query MyQuery {
  allocations(
    where: {indexer: "0xAddressGoesHere"}
    orderBy: createdAt
    orderDirection: desc
  ) {
    id
    status
    closedAt
    createdAt
  }
}
```