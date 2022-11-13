from query import make_query
import sys
from utils import get_data, get_allocation_ages, create_message_text, post_message

def main():
    query = make_query(sys.argv[1])
    data = get_data(query)
    active = [entry for entry in data if entry["status"] == "Active"]
    aged = get_allocation_ages(active)
    message = create_message_text(aged)
    post_message(sys.argv[2], message)

if __name__ == "__main__":
    main()