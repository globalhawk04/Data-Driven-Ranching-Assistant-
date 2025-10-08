import requests
import json
from datetime import datetime
import os
import traceback # Import traceback for more detailed error logging

# --- Configuration ---
token = 'SQiYKAUlUnZLRYHYwUbdEbRnVIeVdfvA'  # <<< Replace with your actual token!
base_url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data'
# *** CORRECTING: Use the USCRNS dataset for these station IDs ***
dataset_id = 'USCRNS'
start_date = '2024-04-01' # Define your desired date range
end_date = '2024-04-03'   # Define your desired date range
limit = 1000 # Max number of results per request

# List of data types we want to fetch - adjusted for USCRNS daily
# Note: Availability varies by station and date.
data_types = [
    'TMAX',             # Maximum Temperature (Degrees Celsius)
    'TMIN',             # Minimum Temperature (Degrees Celsius)
    'RH_AVG',           # Average Relative Humidity (Percentage) - RHMX/RHMN might exist, but RH_AVG is common
    'WIND_SPEED_AVG',   # Average Wind Speed (Meters per second) - WSF1/WSFG might exist, but AVG is common
    # 'PRCP_DAILY',     # Daily Precipitation (mm)
    # 'SOLAR_RADIATION', # Daily Solar Radiation (W/m^2)
    # 'SOIL_MOISTURE_5', # Soil Moisture at 5cm depth (Percentage) - Specific to USCRN-S
]

# --- Station List ---
us1tx_codes = [
    'US1TXBZS004', 'US1TXBZS012', 'US1TXBZS013', 'US1TXBZS017', 'US1TXBZS020',
    'US1TXBZS022', 'US1TXBZS034', 'US1TXBZS040', 'US1TXBZS041', 'US1TXBZS042',
    'US1TXBZS043', 'US1TXBZS050', 'US1TXBZS062', 'US1TXBZS075', 'US1TXBZS077',
    'US1TXBZS083', 'US1TXBZS088', 'US1TXBZS092', 'US1TXBZS096', 'US1TXBZS097',
    'US1TXBZS098', 'US1TXBZS099', 'US1TXBZS100', 'US1TXBZS102', 'US1TXBZS103',
    'US1TXBZS104', 'US1TXBZS106', 'US1TXBZS107', 'US1TXBZS109', 'US1TXBZS111',
    'US1TXBZS112', 'US1TXBZS114', 'US1TXBZS117', 'US1TXBZS118', 'US1TXBZS120',
    'US1TXBZS123', 'US1TXBZS125', 'US1TXBZS127', 'US1TXBZS128', 'US1TXBZS129',
    'US1TXBZS131', 'US1TXBZS133'
]

# --- Output Directories ---
data_dir = 'uscrns_data_on_file' # Changed directory name to reflect dataset
nodata_dir = 'uscrns_nothing_on_file' # Changed directory name
os.makedirs(data_dir, exist_ok=True)
os.makedirs(nodata_dir, exist_ok=True)

headers = {"token": token}

# --- Loop Through Stations ---
print(f"Starting data fetch for {len(us1tx_codes)} stations from {dataset_id} dataset between {start_date} and {end_date}...")
print(f"Requesting Data Types: {', '.join(data_types)}")


for station_id in us1tx_codes:
    print(f"\n--- Processing station: {station_id} ---")

    # --- Construct API Parameters ---
    params = {
        'datasetid': dataset_id,
        'stationid': f'{dataset_id}:{station_id}', # Use USCRNS:station_id format
        'startdate': start_date,
        'enddate': end_date,
        'limit': limit,
        'datatypeid': data_types # Pass the list of data types
    }

    try:
        # --- Make the API Call ---
        r = requests.get(base_url, params=params, headers=headers)
        r.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        response = r.json()

        # --- Process the Response ---
        # Check for 'results' key AND if the list is non-empty
        if response and 'results' in response and response['results']:
            # --- Data Found ---
            response_results = response['results']
            total_records = len(response_results)
            print(f"  -> Data found! Received {total_records} records.")

            # Save to data_on_file directory
            filename = os.path.join(data_dir, f"uscrns_data_{station_id}_{start_date}_{end_date}.json")
            with open(filename, "w") as f:
                json.dump(response_results, f, indent=2)
            print(f"  -> Raw results saved to {filename}")

            # Optional: Basic processing and print (USCRNS values are usually not in tenths)
            # print("\n    --- Sample Records ---")
            # for record in response_results[:5]:
            #      value = record['value']
            #      # No division by 10 needed for USCRNS data typically
            #      print(f"    {record['date'].split('T')[0]} - {record['datatype']}: {value}")
            # if total_records > 5:
            #     print("    ...")


        elif response and 'metadata' in response and response.get('resultset', {}).get('count', 0) == 0:
            # --- No Data Found (explicitly reported by API count) ---
            count_from_metadata = response.get('resultset', {}).get('count', 0)
            print(f"  -> No 'results' returned. Metadata count is {count_from_metadata}.")
            print("  -> This likely means no data exists for the requested dates/datatypes at this station.")

            # Save to nothing_on_file directory
            filename = os.path.join(nodata_dir, f"uscrns_nodata_{station_id}_{start_date}_{end_date}.json")
            nodata_info = {
                "station_id": station_id,
                "status": "no_data_found",
                "dataset_id": dataset_id,
                "date_range": f"{start_date} to {end_date}",
                "requested_datatypes": data_types,
                "api_message": "API returned metadata with count 0 for results."
            }
            with open(filename, "w") as f:
                json.dump(nodata_info, f, indent=2)
            print(f"  -> 'No data' info saved to {filename}")

        else:
            # --- Unexpected Response ---
            print(f"  -> API returned an unexpected response structure for {station_id}.")
            print("  -> Response Text:", r.text) # Print raw text for debugging
            # Optionally save the raw response to a file
            filename = os.path.join(nodata_dir, f"uscrns_unexpected_response_{station_id}_{start_date}_{end_date}.json")
            with open(filename, "w") as f:
                 json.dump({"station_id": station_id, "status": "unexpected_response", "response_text": r.text}, f, indent=2)
            print(f"  -> Unexpected response saved to {filename}")


    except requests.exceptions.RequestException as e:
        # --- API Request Error ---
        print(f"  -> Error during API request for {station_id}: {e}")
        # Save error info to nothing_on_file directory
        filename = os.path.join(nodata_dir, f"uscrns_request_error_{station_id}_{start_date}_{end_date}.json")
        error_info = {
            "station_id": station_id,
            "status": "request_error",
            "dataset_id": dataset_id,
            "date_range": f"{start_date} to {end_date}",
            "error_message": str(e),
            "status_code": r.status_code if 'r' in locals() else 'N/A',
            "response_body_preview": r.text[:500] if ('r' in locals() and r.text) else 'N/A'
        }
        with open(filename, "w") as f:
            json.dump(error_info, f, indent=2)
        print(f"  -> Error info saved to {filename}")


    except json.JSONDecodeError:
        # --- JSON Parsing Error ---
        print(f"  -> Error decoding JSON response for {station_id}.")
        # Save error info to nothing_on_file directory
        filename = os.path.join(nodata_dir, f"uscrns_json_error_{station_id}_{start_date}_{end_edge}.json")
        error_info = {
            "station_id": station_id,
            "status": "json_decode_error",
            "dataset_id": dataset_id,
            "date_range": f"{start_date} to {end_date}",
            "response_text_preview": r.text[:500] if ('r' in locals() and r.text) else 'N/A'
        }
        with open(filename, "w") as f:
             json.dump(error_info, f, indent=2)
        print(f"  -> JSON decode error info saved to {filename}")

    except Exception as e:
         # --- Any Other Unexpected Error ---
         print(f"  -> An unexpected error occurred for {station_id}: {e}")
         filename = os.path.join(nodata_dir, f"uscrns_general_error_{station_id}_{start_date}_{end_date}.json")
         error_info = {
            "station_id": station_id,
            "status": "general_error",
            "dataset_id": dataset_id,
            "date_range": f"{start_date} to {end_date}",
            "error_message": str(e),
            "traceback": traceback.format_exc()
         }
         with open(filename, "w") as f:
              json.dump(error_info, f, indent=2)
         print(f"  -> General error info saved to {filename}")


print("\n--- Data fetching complete ---")