import requests

def get_data(query):
    response = requests.post('https://api.thegraph.com/subgraphs/name/graphprotocol/graph-network-goerli'
                             '',
                             json={
                                "query":query
                                })

    if response.status_code == 200: 
        return response.json()["data"]
    else:
        raise Exception(f"Query failed with return code {response.staus_code}")

def get_allocation_ages(active_allocations, oldest_epoch):
    aged = []
    for i in range(len(active_allocations)):
        tmp_dict = {
            "id": active_allocations[i]["id"],
            "createdAtEpoch": active_allocations[i]["createdAtEpoch"],
            "allocationAgeEpoches": abs(int(active_allocations[i]["createdAtEpoch"] - int(oldest_epoch)))
        }
        aged.append(tmp_dict)
    
    return aged

def create_message_text(aged_allocations):
    message = "__**Allocation Ages Report**__\n\n"

    for entry in aged_allocations:
        message += f'{entry["id"]}\n{entry["allocationAgeEpoches"]} epoches old\n\n'
    
    return {
        "content": message
    }

def post_message(discord_webhook_url, message_content):
    try:
        requests.post(discord_webhook_url, json=message_content)
    except Exception as e:
        return e