
import matplotlib.pyplot as plt

# Define real nations and their approximate coordinates (x, y in arbitrary units)
locations = {
    "Italy": (12, 42),
    "France": (2, 46),
    "Germany": (10, 51),
    "Spain": (-3, 40),
    "Greece": (23, 39)
}

# Define migration routes (start, end)
routes = [
    ("Italy", "France"),
    ("Italy", "Germany"),
    ("Spain", "France"),
    ("Greece", "Italy"),
    ("Germany", "Greece")
]

# Create the plot
plt.figure(figsize=(10, 8), facecolor="lightblue")

# Plot locations
for country, (x, y) in locations.items():
    plt.scatter(x, y, color="darkblue", s=150, edgecolor="black", zorder=3)
    plt.text(x + 0.5, y, country, fontsize=12, weight="bold", color="black")

# Plot migration routes
for start, end in routes:
    start_x, start_y = locations[start]
    end_x, end_y = locations[end]
    plt.plot([start_x, end_x], [start_y, end_y], color="darkgreen", linestyle="-.", linewidth=2, zorder=1)

# Add a background grid to mimic a map
plt.grid(True, linestyle="--", linewidth=0.5, color="gray")

# Add title and labels
plt.title("Migration Routes Between European Nations", fontsize=16, weight="bold", color="darkred")
plt.xlabel("Longitude (arbitrary units)", fontsize=12)
plt.ylabel("Latitude (arbitrary units)", fontsize=12)

# Annotate the compass
plt.text(24, 54, "N", fontsize=14, ha="center", color="black")
plt.arrow(24, 53, 0, 0.5, head_width=0.5, head_length=0.5, fc="black", ec="black")

# Show the plot
plt.show()
