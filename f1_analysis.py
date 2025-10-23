import pandas as pd
from matplotlib import pyplot as plt

# Read your CSV
df = pd.read_csv(r'C:\VsCode\F1_Projects\1_results_2025.csv')

# Clean up column names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

print("Cleaned columns:", df.columns.tolist())

# Combine the team columns for podiums
podiums = pd.concat([df['Team_p1'], df['Team_p2'], df['Team_p3']]).dropna()

# Count podiums by team
counts = podiums.value_counts()
result = counts.reset_index()
result.columns = ['Team', 'Podiums']

# 🎨 Official 2025 F1 Team Colors
team_colors = {
    'Red Bull Racing': '#1E41FF',    # dark blue
    'Ferrari': '#DC0000',            # red
    'Mercedes': '#00D2BE',           # turquoise
    'McLaren': '#FF8700',            # papaya orange
    'Aston Martin': '#006F62',       # dark green
    'Alpine': '#0090FF',             # bright blue
    'Williams': '#005AFF',           # blue
    'RB': '#2B4562',                 # navy blue
    'Kick Sauber': '#00E701',        # neon green
    'Haas': '#FFFFFF',               # white
}

# Assign team color if known, else grey
colors = [team_colors.get(team, '#808080') for team in result['Team']]

# Create the figure
plt.figure(figsize=(10,6))

plt.ylim(0, 40)

# Save the bars so we can label them
bars = plt.bar(result['Team'], result['Podiums'], color=colors)

# Add value labels above bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.5,
             f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Style and formatting
plt.title('Total Podiums by Team (2025 Season)', fontsize=14, fontweight='bold')
plt.xlabel('Team')
plt.ylabel('Number of Podiums')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

#Saving Image
out_dir = r'C:\VsCode\F1_Projects\images'   

# 2) PNG for LinkedIn/Power BI (high-res)
plt.savefig(
    fr"{out_dir}\podiums_2025_updated.png",
    dpi=300,               # crisp
    bbox_inches="tight",   # trims extra margins
    facecolor="white"      # solid white background
)

# 3) SVG for infinite sharpness (great for docs)
plt.savefig(
    fr"{out_dir}\podiums_2025.svg",
    bbox_inches="tight",
    facecolor="white"
)

plt.show()
