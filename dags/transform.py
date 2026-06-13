def transform_data(**kwargs):
    ti = kwargs['ti']
    raw_data = ti.xcom_pull(task_ids='extract_data')
    
    print("Raw data successfully pulled from XCom")
    cleaned_data_list = []
    
    if isinstance(raw_data, list):
        
        for item in raw_data:
            if isinstance(item, dict):
                date = item.get("date")
                base = item.get("base")
                currency = item.get("quote")
                rate_raw = item.get("rate")
            else:
                continue

            if rate_raw is not None:
                rate = float(rate_raw)
            else:
                rate = 0.0

            cleaned_data_list.append({
                "date": date,
                "base": base,
                "quote": currency,
                "rate": rate
            })
            print(f"Date: {date} | Base: {base} | Currency: {currency} | Rate: {rate}")
            
    elif isinstance(raw_data, dict):
        base = raw_data.get("base", "EUR")
        date = raw_data.get("date")
        rates = raw_data.get("rates", {})

        for currency, rate_raw in rates.items():
            if rate_raw is not None:
                rate = float(rate_raw)
            else:
                rate = 0.0

            cleaned_data_list.append({
                "date": date,
                "base": base,
                "quote": currency,
                "rate": rate
            })
            print(f"Date: {date} | Base: {base} | Currency: {currency} | Rate: {rate}")
        
    return cleaned_data_list