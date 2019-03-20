import pandas as pd


def create_df():
    pd.set_option('display.max_columns', 500)

    index_list = ["GSPC", "DJI", "IXIC", "STOXX50E", "RUT", "N225"]


    fx_df = pd.read_csv("FX.csv", encoding ="shift-jis", header = 2)
    fx_df["Date"] = pd.to_datetime(fx_df["Date"])

    #fx_df = fx_df.add_prefix("")
    #print(fx_df.head())

    df_lst = []
    for index in index_list:
        target = index + ".csv"
        target_df =pd.read_csv(str(target), header = 0)
        target_df["Date"] = pd.to_datetime(target_df["Date"])
        target_df.columns = target_df.columns[:1].union((index + " " +target_df.columns[1:]), sort = False)

        df_lst.append(target_df)


    res_df = fx_df

    for i in range(len(df_lst)):
        res_df = pd.merge(df_lst[i], res_df, on="Date")


    res_df.to_csv("result.csv",index=False)


def modifyDF():
    res_df = pd.read_csv("result.csv", header = 0)

    price_increase = [[0]]

    prev_close = 0
    cur_close = 0
    for row in range(len(res_df)):
        if row == 0:
            prev_close = res_df["N225 Close"][row]
        else:
            cur_close = res_df["N225 Close"][row]
            if prev_close < cur_close:
                price_increase.append([1])
            else:
                price_increase.append([0])
            prev_close = res_df["N225 Close"][row]

    answer = pd.DataFrame(price_increase, columns = ["Answer"])
    answer

    res_df = res_df.join(answer)

    res_df.to_csv("result.csv",index=False)


create_df()
modifyDF()
