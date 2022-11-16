# Allocation Ages
Monitor the age of your open subgraph allocations, *in epoch time*. 

As per [The Graph documentation](https://thegraph.com/docs/en/network/indexing/#the-life-of-an-allocation), the maximum subgraph allocation lifetime (`maxAllocationEpochs`) is currently set to 28 epochs. 

Our Indexer Agent *should* automatically close allocations after `maxAllocationEpochs`, but this bot monitors for allocations that were not automatically closed after `maxAllocationEpochs`.

## Set up
### Use with your own wallet
* [Fork the repo](https://github.com/IndexerDAO/allocation-ages/fork)
* Create two repository secrets in the new repo
    * WALLET_ADDRESS: Address whose subgraph allocation ages will be monitored
    * WEBHOOK_URL: Discord Channel webhook url to post allocation monitor updates when applicable

### Optional: Change bot trigger rate
Currently set to every two hours, on the hour.
* Modify line 5 of `.github/workflows/app.yml`
    * Use `cron` expression to set the trigger rate

## Contributing
### Local setup
``` bash
git clone https://github.com/IndexerDAO/allocation-ages.git
cd allocation-ages
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```