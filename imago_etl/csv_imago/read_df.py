import pandas as pd

def read_data(data):
    # path_csv = r'H:\Patriot Battery Metals\Patriot_Core_Photos\Patriot_Battery_Metals.csv'
    df = pd.read_csv(data, sep=',')
    df_simple = df.drop(columns=["ocrData", "x", "y", "z", "guidId", "rotation","features"])
    return df_simple