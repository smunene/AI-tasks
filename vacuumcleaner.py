import random

class VacuumEnvironment:
    def __init__(self):
        #The rooms are either clean or dirty
        self.locations = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }
        #Starting the agent at a random location
        self.agent_pos = random.choice(['A', 'B'])

    def get_status(self):
        #Returns the status of the room the agent is currently in
        return self.locations[self.agent_pos]

class VacuumAgent:
    def act(self, environment):
        location = environment.agent_pos
        status = environment.get_status()
        
        print(f"Agent is in Room {location}. Status: {status}")

        if status == 'Dirty':
            #Action: Sucking the dirt
            print(f"Action: Sucking dirt in Room {location}")
            environment.locations[location] = 'Clean'
            print(f"Room {location} is now Clean.")
        else:
            #Action: Move to the other room if the current one is clean
            new_location = 'B' if location == 'A' else 'A'
            print(f"Action: Room {location} is already clean. Moving to {new_location}")
            environment.agent_pos = new_location

#Initialization
env = VacuumEnvironment()
agent = VacuumAgent()

print("Initial Environment State:", env.locations)
print("-" * 30)

#Running the agent for a few steps to ensure both rooms are cleaned
for step in range(4):
    print(f"Step {step + 1}:")
    agent.act(env)
    print(f"Current State: {env.locations}\n")

print("Final Environment State:", env.locations)