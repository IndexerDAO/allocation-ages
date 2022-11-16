from query import get_current_epoch, get_old_allocations
from utils import get_data, get_allocation_ages, create_message_text, post_message
import sys

def main():
    wallet_address = sys.argv[1]
    discord_webhook_url = sys.argv[2]

    oldest_epoch = int(get_data(get_current_epoch())["epoches"][0]["id"]) - 3
    old_allocations = get_data(get_old_allocations(wallet_address, oldest_epoch))["allocations"]
    
    if len(old_allocations) > 0:
        aged = get_allocation_ages(old_allocations, oldest_epoch)
        message = create_message_text(aged)
        post_message(discord_webhook_url, message)
    else:
        return f"No allocations older than 3 epoches"

if __name__ == "__main__":
    main()