def add_vehicle_age(df):
    if 'TransactionMonth' in df.columns and 'RegistrationYear' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
        df['TransactionYear'] = df['TransactionMonth'].dt.year
        df['vehicle_age'] = df['TransactionYear'] - df['RegistrationYear']
    return df