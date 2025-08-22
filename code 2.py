import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Process Your Airbnb Data Files ---

files_by_date = {
    '2024-09-06': '/Users/nirajmutha/Downloads/listings (4).csv',
    '2024-12-11': '/Users/nirajmutha/Downloads/listings (3).csv',
    '2025-03-04': '/Users/nirajmutha/Downloads/listings (2).csv',
    '2025-06-10': '/Users/nirajmutha/Downloads/listings (1).csv'
}

airbnb_data_list = []
print("--- Processing Airbnb Data ---")
for date, filename in files_by_date.items():
    try:
        df_airbnb = pd.read_csv(filename)
        listing_count = len(df_airbnb)
        airbnb_data_list.append({'Date': pd.to_datetime(date), 'Airbnb_Listings': listing_count})
        print(f"Successfully processed {filename} for {date}: {listing_count} listings.")
    except Exception as e:
        print(f"Could not process {filename}. Error: {e}")

df_airbnb_timeline = pd.DataFrame(airbnb_data_list).sort_values('Date')
print("\n--- Completed Airbnb Growth Timeline ---")
print(df_airbnb_timeline)


# --- Step 2: Create the Hotel Data DataFrame ---

print("\n\n--- Creating Hotel Data Timeline ---")
hotel_data = {
    'Date': pd.to_datetime([
        '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01',
        '2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01'
    ]),
    'Hotel_Occupancy_Rate': [
        80, 79, 81, 83, 67, 72, 77, 82, 84
    ]
}
df_hotel_timeline = pd.DataFrame(hotel_data)
print("\n--- Completed Hotel Occupancy Timeline ---")
print(df_hotel_timeline)

# --- Step 3: Visualize the Comparison ---

print("\n\n--- Generating Final Visualization ---")
if not df_airbnb_timeline.empty and not df_hotel_timeline.empty:
    fig, ax1 = plt.subplots(figsize=(14, 8))
    sns.set_style("whitegrid")

    # Plot Hotel Occupancy on the primary y-axis (ax1)
    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('London Hotel Occupancy Rate (%)', color=color, fontsize=12)
    ax1.plot(df_hotel_timeline['Date'], df_hotel_timeline['Hotel_Occupancy_Rate'], color=color, marker='o', label='Hotel Occupancy Rate')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 100) # Set y-axis for percentage

    # Create a second y-axis for Airbnb Listings
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Total Airbnb Listings in London', color=color, fontsize=12)
    ax2.plot(df_airbnb_timeline['Date'], df_airbnb_timeline['Airbnb_Listings'], color=color, marker='o', linestyle='--', label='Airbnb Listings')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Airbnb Listings vs. Hotel Occupancy in London (2024-2025)', fontsize=16)
    fig.tight_layout()
    plt.savefig('airbnb_vs_hotels_london_final.png')
    print("\nChart 'airbnb_vs_hotels_london_final.png' has been saved.")
    plt.show()
else:
    print("\nCould not generate visualization because one of the datasets is empty.")
