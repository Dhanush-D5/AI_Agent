import json

MEMORY_FILE = "memory/data.json"


# =========================
# LOAD MEMORY
# =========================

def load_memory():

    try:

        with open(MEMORY_FILE, "r") as file:

            return json.load(file)

    except:

        return []


# =========================
# SAVE MEMORY
# =========================

def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:

        json.dump(
            memory,
            file,
            indent=4
        )


# =========================
# ADD MEMORY
# =========================

def add_memory(memory_list, memory):

    # Avoid duplicates
    if memory not in memory_list:

        memory_list.append(memory)

        save_memory(memory_list)