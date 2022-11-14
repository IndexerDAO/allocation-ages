from query import make_query
import sys
from utils import get_data, get_allocation_ages, create_message_text, post_message

def main():
    time_delta = sys.argv[3]
    discord_webhook_url = sys.argv[2]
    wallet_address = sys.argv[1]

    query = make_query(wallet_address, time_delta)
    data = get_data(query)
    aged = get_allocation_ages(data)

    if len(aged) > 0:
        message = create_message_text(aged)
        post_message(discord_webhook_url, message)
    else:
        return f"No allocations older than {time_delta} minutes"

if __name__ == "__main__":
    main()