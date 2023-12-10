import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here

    # Creating a sample dataframe with zeros
    distance_matrix = pd.DataFrame(0, index=df['id'].unique(), columns=df['id'].unique())

    # Example: Setting known distances in the matrix
    distance_matrix.loc['A', 'B'] = 10
    distance_matrix.loc['B', 'A'] = 10
    distance_matrix.loc['A', 'C'] = 15
    distance_matrix.loc['C', 'A'] = 15
    distance_matrix.loc['B', 'C'] = 20
    distance_matrix.loc['C', 'B'] = 20

    # Ensure diagonal values are set to 0
    distance_matrix.values[[range(distance_matrix.shape[0])]*2] = 0

    return distance_matrix


    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here

 
    # Create an empty list to store unrolled distance matrix data
    unrolled_data = []

    # Loop through the distance matrix to extract data
    for i, row in df.iterrows():
        for j, value in row.iteritems():
            if i != j:  # Skip if id_start is the same as id_end
                unrolled_data.append({'id_start': i, 'id_end': j, 'distance': value})

    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df


    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
   
    # Calculate average distance for the reference_id
    reference_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()

    # Calculate threshold range (10% of the reference average distance)
    threshold_lower = reference_avg_distance - 0.1 * reference_avg_distance
    threshold_upper = reference_avg_distance + 0.1 * reference_avg_distance

    # Filter IDs within the threshold range
    filtered_ids = df.groupby('id_start')['distance'].mean().reset_index()
    filtered_ids = filtered_ids[(filtered_ids['distance'] >= threshold_lower) & (filtered_ids['distance'] <= threshold_upper)]

    return filtered_ids


    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
    
    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Calculate toll rates by multiplying distance with rate coefficients for each vehicle type
    for vehicle_type, rate in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate




    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

import datetime


    # Define time ranges and discount factors
    weekdays_discounts = {
        (datetime.time(0, 0, 0), datetime.time(10, 0, 0)): 0.8,
        (datetime.time(10, 0, 0), datetime.time(18, 0, 0)): 1.2,
        (datetime.time(18, 0, 0), datetime.time(23, 59, 59)): 0.8
    }

    weekends_discount = 0.7

    # Create lists to store the calculated time-based toll rates
    start_day_list = []
    start_time_list = []
    end_day_list = []
    end_time_list = []
    vehicle_columns = ['moto', 'car', 'rv', 'bus', 'truck']
    for vehicle in vehicle_columns:
        vehicle_list = []

        # Loop through each time range and calculate toll rates
        for _, row in df.iterrows():
            for start_time, end_time in weekdays_discounts:
                if row['start_time'] >= start_time and row['end_time'] <= end_time:
                    rate = weekdays_discounts[(start_time, end_time)] if row['start_day'] != 'Saturday' and row['start_day'] != 'Sunday' else weekends_discount
                    vehicle_list.append(row[vehicle] * rate)
                    break

        # Add the calculated toll rates for the current vehicle to the DataFrame
        df[vehicle + '_time_based'] = vehicle_list

   


    return df
