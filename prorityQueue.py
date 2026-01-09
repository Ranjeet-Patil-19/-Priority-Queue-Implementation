class PriorityQueue:
    def __init__(self):
        # Initialize with an empty list to store (priority, item) pairs
        self.queue = []
        self.counter = 0  # To handle same priority items (FIFO order)
    
    def push(self, item, priority):
        """Add item with given priority"""
        # Store as tuple: (priority, counter, item)
        # Counter ensures FIFO for same priority
        entry = (-priority, self.counter, item)
        self.queue.append(entry)
        self.counter += 1
        # Sort to maintain priority order (highest priority first)
        self.queue.sort()
    
    def pop(self):
        """Remove and return highest priority item"""
        if self.is_empty():
            raise IndexError("Pop from empty priority queue")
        # Get and remove the first item (highest priority)
        priority, counter, item = self.queue.pop(0)
        return item
    
    def peek(self):
        """Return highest priority item without removing"""
        if self.is_empty():
            raise IndexError("Peek from empty priority queue")
        # Return the item from the first entry
        priority, counter, item = self.queue[0]
        return item
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.queue) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.queue)
    
    def __str__(self):
        """String representation for debugging"""
        if self.is_empty():
            return "PriorityQueue: Empty"
        
        # Create a readable representation
        result = "PriorityQueue:\n"
        for priority, counter, item in self.queue:
            # Convert back to positive priority for display
            actual_priority = -priority
            result += f"  {item} (priority: {actual_priority})\n"
        return result

# Test your implementation
if __name__ == "__main__":
    print("=== Testing Priority Queue ===\n")
    
    pq = PriorityQueue()
    
    # Test 1: Basic operations
    print("Test 1: Adding items with different priorities")
    pq.push("task1", 3)
    pq.push("task2", 1)
    pq.push("task3", 2)
    
    print(f"Size: {pq.size()}")  # Should print 3
    print(f"Peek: {pq.peek()}")  # Should show task1 (priority 3)
    print(f"Pop: {pq.pop()}")    # Should remove and return task1
    
    print("\nQueue after popping task1:")
    print(pq)
    
    # Test 2: More complex scenario
    print("\nTest 2: Adding more items")
    pq.push("urgent", 10)
    pq.push("medium", 5)
    pq.push("low", 1)
    
    print(f"Queue now has {pq.size()} items:")
    print(pq)
    
    print("\nPopping all items in priority order:")
    while not pq.is_empty():
        print(f"  Popped: {pq.pop()}")
    
    # Test 3: Empty queue handling
    print("\nTest 3: Testing empty queue")
    print(f"Is empty? {pq.is_empty()}")
    
    try:
        pq.peek()
    except IndexError as e:
        print(f"Expected error on peek: {e}")
    
    # Test 4: Same priorities
    print("\nTest 4: Items with same priority (should be FIFO)")
    pq.push("first", 1)
    pq.push("second", 1)
    pq.push("third", 1)
    pq.push("high", 10)
    
    print("Queue with same priorities:")
    print(pq)
    
    print("\nPopping (should get 'high' then 'first', 'second', 'third'):")
    while not pq.is_empty():
        print(f"  {pq.pop()}")
