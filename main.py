from dags.extract import extract_data
from dags.transform import transform_data
from dags.load import run_load_process

def main():
    print("<--- ETL PIPELINE START --->")

    raw_data = extract_data()
    if not raw_data:
        print("**ERROR** --> DATA COULDN'T NOT BE RETRIEVED.")
        return
    
    cleaned_list = transform_data(raw_data)
    if not cleaned_list:
        print("**ERROR** --> DATA COULN'T BE CONVERTED")
        return
    
    run_load_process(cleaned_list)
    print("\n -*-*- ETL PIPELINE COMPLETED SUCCESFULLY")

if __name__ == "__main__":
    main()