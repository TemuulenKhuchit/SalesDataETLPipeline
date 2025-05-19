def clean_sales_data(df):
    df = df.dropna()
    df = df[df["amount"] > 0]
    return df


def convert_to_tuples(df):
    return list(df[["sale_id", "product", "quantity", "amount"]].itertuples(index=False, name=None))
