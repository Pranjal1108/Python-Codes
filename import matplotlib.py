import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Define the flowchart boxes and their positions
boxes = {
    "Problem Identification": (0.5, 0.9),
    "Track Village Population": (0.2, 0.75),
    "Monitor Land Ownership": (0.5, 0.75),
    "Optimize Crop Growth (Seasonal Analysis)": (0.8, 0.75),
    "Analyze Storage Conditions": (0.2, 0.6),
    "Implement Storage Solutions": (0.5, 0.6),
    "Reduce Waste": (0.8, 0.6),
    "Assess Land Distribution": (0.2, 0.45),
    "Plan Solar Panel Installations": (0.5, 0.45),
    "Implement Water Management System": (0.5, 0.3),
    "Improve Street Conditions for Lighting": (0.5, 0.15)
}

# Draw the boxes
for text, (x, y) in boxes.items():
    ax.text(x, y, text, ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#add8e6"))

# Define the arrows and their start/end points
arrows = [
    ("Problem Identification", "Track Village Population"),
    ("Problem Identification", "Monitor Land Ownership"),
    ("Problem Identification", "Optimize Crop Growth (Seasonal Analysis)"),
    ("Monitor Land Ownership", "Analyze Storage Conditions"),
    ("Optimize Crop Growth (Seasonal Analysis)", "Implement Storage Solutions"),
    ("Implement Storage Solutions", "Reduce Waste"),
    ("Track Village Population", "Assess Land Distribution"),
    ("Assess Land Distribution", "Plan Solar Panel Installations"),
    ("Plan Solar Panel Installations", "Implement Water Management System"),
    ("Implement Water Management System", "Improve Street Conditions for Lighting")
]

# Draw the arrows
for start, end in arrows:
    ax.annotate("",
                xy=boxes[end], xycoords='data',
                xytext=boxes[start], textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=2))

# Set axis properties
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Display the flowchart
plt.title("Flowchart of Proposed Solution", fontsize=16)
plt.show()
