import time
import requests

def get_data(query):
    response = requests.post('https://api.thegraph.com/subgraphs/name/graphprotocol/graph-network-goerli'
                             '',
                             json={"query":query})

    if response.status_code == 200: 
        return response.json()["data"]["allocations"]
    else:
        raise Exception("Query failed with return code {}".format(response.staus_code))

def get_allocation_ages(active_allocations):
    current_time = time.time()
    aged = []
    for i in range(len(active_allocations)):
        tmp_dict = {
            "id": active_allocations[i]["id"],
            "status": active_allocations[i]["status"],
            "closedAt": active_allocations[i]["closedAt"],
            "createdAt": active_allocations[i]["createdAt"],
            "allocationAgeMinutes": (current_time - active_allocations[i]["createdAt"]) / 60
        }
        aged.append(tmp_dict)
    
    return aged

def create_message_text(aged_allocations):
    message = "__**Allocation Ages Report**__\n\n"

    for entry in aged_allocations:
        message += f'{entry["id"]}\n{entry["allocationAgeMinutes"]} minutes old\n\n'
    
    return {
        "content": message
    }

def post_message(discord_webhook_url, message_content):
    try:
        requests.post(discord_webhook_url, json=message_content)
    except Exception as e:
        return e

def filter_for_old_allocations(allocations, threshold):
    results = []
    for allo in allocations:
        if allo["allocationAgeMinutes"] >= threshold:
            results.append(allo)
    return results