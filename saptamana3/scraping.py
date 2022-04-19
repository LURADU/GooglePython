import pandas as pd


for x in range(20, 27):
    url = f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{x}-ianuarie-ora-13-00/'
    df_list = pd.read_html(url)[0]
    df_list=df_list[[0,1,2]]
    #x=len(df_list)
    #print(x)
    print(df_list)
    rezult=pd.DataFrame({f'CoronaData{x}': [df_list]})
    rezult.to_csv(f'cazuri{x} ian.csv')