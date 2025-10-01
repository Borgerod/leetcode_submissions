import time
import threading

def sleep_sort(numbers):
    sorted_list = []

    # Function to add a number to the sorted list after a delay
    def add_number(number):
        time.sleep(number)  # Sleep for 'number' seconds
        sorted_list.append(number)  # Add the number to the sorted list after sleeping

    # Create threads for each number in the list
    threads = [threading.Thread(target=add_number, args=(num,)) for num in numbers]

    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return sorted_list

# Example usage:
numbers = [5, 3, 7, 2, 4, 1, 6]
sorted_numbers = sleep_sort(numbers)
print("Sorted numbers:", sorted_numbers)