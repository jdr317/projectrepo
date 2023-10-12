import pandas as pd

def get_mapping(fname='my_map.csv'):
    return pd.read_csv(fname)

def get_data(fname='data.csv'):
    return pd.read_csv(fname)

def get_canon(fname='my_canon.csv'):
    return pd.read_csv(fname)

def main():
    my_map = get_mapping()
    data = get_data()
    canon = get_canon()
    my_map.columns = ['Seller','label_']
    data = pd.merge(data,my_map,on='Seller')
    my_canon.columns = ['idx','label_','CanonSeller']
    data = pd.merge(data,my_canon,on='label_')
    report = data.groupby('CanonSeller').agg({'CostUSD': 'sum'}).sort_values('CostUSD',ascending=False)
    report.to_csv('cost_report.csv')

if __name__ == "__main__":
    main()