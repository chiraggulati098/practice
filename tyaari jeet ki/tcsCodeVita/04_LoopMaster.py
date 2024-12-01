n = 10
queries = ['for 5 times', 'do', 'continue 3', 'print "hello"', 'for 5 times', 'do', 'print "world"', 'break 3', 'done', 'done']

# n = input("")
# queries = []

# for _ in range(n):
#     queries.append(input())

def execute_commands(commands):
    loop_state = []  # Keeps track of loop states (max count, current count)
    index_map = build_index_map(commands)  # Precompute matching 'do' and 'done'
    output = []
    current_index = 0

    while current_index < len(commands):
        command = commands[current_index]

        if command.startswith("for"):
            max_count = int(command.split()[1])
            loop_state.append({"max": max_count, "current": 0})
            current_index += 1

        elif command == "do":
            current_index += 1  # Just move to the next command

        elif command == "done":
            if not loop_state:
                raise ValueError("Mismatched 'done' found!")

            state = loop_state[-1]
            state["current"] += 1

            if state["current"] < state["max"]:
                # Jump back to the matching 'do'
                current_index = index_map["do"][current_index]
            else:
                # Exit the loop
                loop_state.pop()
                current_index += 1

        elif command.startswith("break"):
            break_at = int(command.split()[1])
            if loop_state and loop_state[-1]["current"] + 1 == break_at:
                # Exit the loop immediately
                current_index = index_map["done"][current_index]
                loop_state.pop()
            else:
                current_index += 1

        elif command.startswith("continue"):
            continue_at = int(command.split()[1])
            if loop_state and loop_state[-1]["current"] + 1 == continue_at:
                # Skip to the start of the loop
                current_index = index_map["do"][current_index]
            else:
                current_index += 1

        elif command.startswith("print"):
            message = command.split("\"", 1)[1].rsplit("\"", 1)[0]
            output.append(message)
            current_index += 1

        else:
            current_index += 1

    print("\n".join(output))

def build_index_map(commands):
    index_map = {"do": {}, "done": {}}
    stack = []

    for i, command in enumerate(commands):
        if command == "do":
            stack.append(i)
        elif command == "done":
            if not stack:
                raise ValueError(f"Unexpected 'done' at line {i}")
            start_index = stack.pop()
            index_map["do"][i] = start_index
            index_map["done"][start_index] = i

    if stack:
        raise ValueError(f"Unmatched 'do' commands at indices: {stack}")

    return index_map


execute_commands(queries)