

def transform_data(raw_data):
    print("It's raw Data")

    cleaned_data_list = []

    for item in raw_data:
        date = item.get("date")
        base = item.get("base")
        currency = item.get("quote")
        
        rate_raw = item.get("rate")
        if rate_raw is not None:
            rate=float(rate_raw)
        else:
            rate: 0.0

        cleaned_data_list.append({
            "date": date,
            "base": base,
            "quote": currency,
            "rate": rate
        })

        print(f"Date: {date} | Base: {base} | Currency: {currency} | Rate: {rate}")
        
    return cleaned_data_list
