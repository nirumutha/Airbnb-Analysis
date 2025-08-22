import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Process Your Airbnb Data Files ---

files_by_year = {
    2024: '/Users/nirajmutha/Downloads/listings (4).csv',
    2025: '/Users/nirajmutha/Downloads/listings (1).csv'
}

airbnb_data_list = []
print("--- Processing Airbnb Data ---")
for year, filename in files_by_year.items():
    try:
        df_airbnb_year = pd.read_csv(filename)
        listing_count = len(df_airbnb_year)
        airbnb_data_list.append({'Year': year, 'Airbnb_Listings': listing_count})
        print(f"Successfully processed {filename} for Year {year}: {listing_count} listings.")
    except Exception as e:
        print(f"Could not process {filename}. Error: {e}")

# Create the Airbnb timeline DataFrame
df_airbnb_timeline = pd.DataFrame(airbnb_data_list).sort_values('Year')
print("\n--- Completed Airbnb Growth Timeline ---")
print(df_airbnb_timeline)

# Get the most recent Airbnb listing count from the completed timeline
latest_airbnb_count = 0
if not df_airbnb_timeline.empty:
    latest_airbnb_count = df_airbnb_timeline['Airbnb_Listings'].iloc[-1]


# --- Step 2: Extract the Hotel Data Point ---

print("\n\n--- Processing Hotel Data ---")
total_hotel_rooms = 0 # Initialize with a default value
try:
    df_cities = pd.read_excel(
        '/Users/nirajmutha/Downloads/global-city-indicators.xlsx',
        sheet_name='World Cities data'
    )
    hotel_row = df_cities[df_cities['Geography'] == 'Hotel Rooms (thousands)']
    total_hotel_rooms = hotel_row['London'].iloc[0] * 1000
    print("\n--- Hotel Data Point Found ---")
    print(f"Total London Hotel Rooms: {total_hotel_rooms:,.0f}")
except Exception as e:
    print(f"An error occurred while processing hotel data: {e}")


# --- Step 3: Create a DataFrame for the Final Comparison ---

print("\n\n--- Creating Final Comparison Data ---")
if total_hotel_rooms > 0 and latest_airbnb_count > 0:
    comparison_data = {
        'Accommodation Type': [f'Airbnb Listings ({df_airbnb_timeline["Year"].iloc[-1]})', 'Hotel Rooms'],
        'Total Count': [latest_airbnb_count, total_hotel_rooms]
    }
    df_comparison = pd.DataFrame(comparison_data)
    print(df_comparison)
else:
    print("Could not create comparison data because some data was not loaded.")


# --- Step 4: Create the Final Comparison Chart ---

print("\n\n--- Generating Final Visualization ---")
if 'df_comparison' in locals():
    plt.figure(figsize=(8, 6))
    sns.set_style("whitegrid")
    barplot = sns.barplot(x='Accommodation Type', y='Total Count', data=df_comparison, palette='viridis')

    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), ',.0f'),
                         (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha = 'center', va = 'center',
                         xytext = (0, 9),
                         textcoords = 'offset points')

    plt.title('Market Scale: Airbnb vs. Hotels in London', fontsize=16)
    plt.ylabel('Total Number of Units', fontsize=12)
    plt.xlabel('')
    plt.savefig('market_comparison_london.png')
    print("\nChart 'market_comparison_london.png' has been saved.")
    plt.show()
else:
    print("Could not generate visualization.")