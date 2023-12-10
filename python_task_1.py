import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    
    df = pd.read_csv('dataset-1.csv')
    
    # Pivot the DataFrame to generate the car matrix based on the given rules
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    # Set diagonal values to 0
    for i in range(min(car_matrix.shape)):
        car_matrix.iloc[i, i] = 0
    
    return car_matrix


    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
   df = pd.read_csv('dataset-1.csv')
    
    # Add a new categorical column 'car_type' based on values of the 'car' column
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(np.select(conditions, choices), index=data.index)
    
    # Calculate the count of occurrences for each car_type category
    type_counts = df['car_type'].value_counts().to_dict()
    
    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))
    
    return sorted_type_counts


    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    df = pd.read_csv('dataset-1.csv')

    # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where bus values are greater than twice the mean bus value
    bus_indexes = df[data['bus'] > (2 * mean_bus_value)].index.tolist()
    
    # Return the indices as a list sorted in ascending order
    return sorted(bus_indexes)


    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    df = pd.read_csv('dataset-1.csv')

    # Group by 'route' column and filter based on average 'truck' values greater than 7
    filtered_routes = df.groupby('route')['truck'].mean()
    filtered_routes = filtered_routes[filtered_routes > 7].index.tolist()
    
    # Return the sorted list of values of the 'route' column
    return sorted(filtered_routes)


    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    
    # Multiply values based on specified conditions and round to 1 decimal place
    modified_dataframe = input_dataframe.copy()  # Create a copy of the input DataFrame
    
    # Apply multiplication logic based on value conditions
    modified_dataframe[input_dataframe > 20] *= 0.75
    modified_dataframe[input_dataframe <= 20] *= 1.25
    
    # Round values to 1 decimal place
    modified_dataframe = modified_dataframe.round(1)
    
    return modified_dataframe


    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    
def check_time_completeness(data):
  
    data = pd.read_csv('dataset-2.csv')

    # Combine 'startDay' and 'startTime' columns into a single datetime column 'start_datetime'
    data['start_datetime'] = pd.to_datetime(data['startDay'] + ' ' + data['startTime'])

    # Combine 'endDay' and 'endTime' columns into a single datetime column 'end_datetime'
    data['end_datetime'] = pd.to_datetime(data['endDay'] + ' ' + data['endTime'])

    # Calculate time differences and check completeness for each unique (id, id_2) pair
    grouped = data.groupby(['id', 'id_2'])

    completeness_check = grouped.apply(lambda x: (
        x['start_datetime'].min().time() == pd.Timestamp('00:00:00').time() and
        x['end_datetime'].max().time() == pd.Timestamp('23:59:59').time() and
        len(x['start_datetime'].dt.date.unique()) == 7
    ))

    return completeness_check


    return pd.Series()
