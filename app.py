from query import make_query
import sys
from utils import get_data, get_allocation_ages, create_message_text, post_message, filter_for_old_allocations

def main():
    allocation_age_threshold=sys.argv[3]

    query = make_query(sys.argv[1])
    data = get_data(query)
    active = [entry for entry in data if entry["status"] == "Active"]
    aged = get_allocation_ages(active)
    old_allocations = filter_for_old_allocations(aged, allocation_age_threshold)

    if len(old_allocations) > 0:
        message = create_message_text(old_allocations)
        post_message(sys.argv[2], message)
    else:
        return f"No allocations older than {allocation_age_threshold}"

if __name__ == "__main__":
    main()