## Set up

### Use with your own wallet
* [Fork the repo](https://github.com/IndexerDAO/allocation-ages/fork)
* Create two repository secrets in the new repo
    * WALLET_ADDRESS: Address whose allocation ages will be monitored
    * WEBHOOK_URL: Discord Channel webhook url to post allocation monitor updates
    * AGE_THRESHOLD: Allocations older than this age (in minutes) will trigger a message

### Local dev environment
``` bash
git clone https://github.com/IndexerDAO/allocation-ages.git
cd allocation-ages
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