# Australian map colouring constraint program
def is_valid(region, color, assignment, adjacency_map):
    for neighbor in adjacency_map.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(regions, colors, assignment, adjacency_map):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, adjacency_map):
            assignment[region] = color
            result = backtrack(regions, colors, assignment, adjacency_map)
            if result:
                return result
            del assignment[region]
    return None

regions = ["WA", "NT", "SA", "Q", "NSW", "V"]
colors = ["Red", "Green", "Blue"]

adjacency_map = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"]
}

solution = backtrack(regions, colors, {}, adjacency_map)

if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")

# Nairobi map colouring constraint program
nairobi_map = {
    "Westlands": ["Dagoretti North", "Starehe", "Roysambu"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra", "Lang'ata"],
    "Dagoretti South": ["Dagoretti North", "Kibra", "Lang'ata"],
    "Lang'ata": ["Dagoretti North", "Dagoretti South", "Kibra", "Starehe", "Embakasi South"],
    "Kibra": ["Dagoretti North", "Dagoretti South", "Lang'ata", "Starehe"],
    "Starehe": ["Westlands", "Mathare", "Kamukunji", "Makadara", "Lang'ata", "Kibra"],
    "Mathare": ["Starehe", "Ruaraka", "Kamukunji"],
    "Kamukunji": ["Starehe", "Mathare", "Makadara", "Embakasi West"],
    "Makadara": ["Starehe", "Kamukunji", "Embakasi West", "Embakasi South"],
    "Roysambu": ["Westlands", "Kasarani", "Ruaraka"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North", "Embakasi East"],
    "Ruaraka": ["Mathare", "Roysambu", "Kasarani", "Embakasi North"],
    "Embakasi North": ["Ruaraka", "Kasarani", "Embakasi East", "Embakasi West"],
    "Embakasi West": ["Kamukunji", "Makadara", "Embakasi North", "Embakasi Central"],
    "Embakasi Central": ["Embakasi West", "Embakasi North", "Embakasi East"],
    "Embakasi East": ["Kasarani", "Embakasi Central", "Embakasi South"],
    "Embakasi South": ["Makadara", "Lang'ata", "Embakasi East"]
}

def color_nairobi(adj_map):
    sub_counties = sorted(adj_map.keys(), key=lambda x: len(adj_map[x]), reverse=True)
    color_names = ["Red", "Green", "Blue", "Yellow"]
    result = {}

    for sub_county in sub_counties:
        neighbor_colors = {result[neighbor] for neighbor in adj_map[sub_county] if neighbor in result}
        for color in color_names:
            if color not in neighbor_colors:
                result[sub_county] = color
                break   
    return result

assignments = color_nairobi(nairobi_map)

print("--- Nairobi Sub-County Coloring ---")
for sc, color in sorted(assignments.items()):
    print(f"{sc: <18}: {color}")