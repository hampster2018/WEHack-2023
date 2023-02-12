# Run cell
# %%

import os # reading in files from directory
import pandas as pd # reading contents of files
import matplotlib.pyplot as plt # plotting info
import numpy as np # for replacing na
import sklearn as sk
from sklearn.preprocessing import scale
directory = 'C:\\Users\\83627\\Downloads\\2021.annual.by_industry'
num_files = 0

dataframes = []

print("Reading...")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        num_files = num_files+1
        data = pd.read_csv(f,  dtype={'area_fips': 'str'})
        dataframes.append(data)

print("Done reading.")

result = pd.concat(dataframes)
result2 = pd.concat(dataframes)

df2 = result.replace(np.nan, 0)
df3 = result2.replace(np.nan, 0)

quant_col = []
for col in df2:
    if not df2[col].dtype.name == "int64" and not df2[col].dtype.name == "float64" :
        quant_col.append(col)

quant_col.append("year")
quant_col.append("size_code")
quant_col.append("qtr")
print(quant_col)
df2.drop(columns=quant_col, axis=1, inplace=True)
df3.drop(columns=quant_col, axis=1, inplace=True)

# df2.describe()
# # %%
# # getting min anx max of quant calumns

# for col in df2:
#     if not col == "area_fips" and not col == "industry_code":
#         print(col)
#         plt.title(col)
#         plt.scatter(df2[col].index, df2[col])
#         plt.show()





# DO NOT RUN
# %%
# normalized_df2=(df2-df2.min())/(df2.max()-df2.min())
# for col in df2:
#     df2[col] = (df2[col]-df2[col].min())/(df2[col].max()-df2[col].min())

# for col in df2:
#     if not col == "area_fips" and not col == "industry_code":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
# # %%
# # Breaking into quantiles
# for col in df2:
#     if col == "own_code":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()

#     elif col == "agglvl_code":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()

#     elif col == "annual_avg_estabs_count":
#         # 10%
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()

#     elif col == "annual_avg_emplvl":
#         # 10%
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "total_annual_wages":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "taxable_annual_wages":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "annual_contributions":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "annual_avg_wkly_wage":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "avg_annual_pay":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_annual_avg_estabs_count":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_annual_avg_emplvl":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_total_annual_wages":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_taxable_annual_wages":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_annual_contributions":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_annual_avg_wkly_wage":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "lq_avg_annual_pay":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_avg_estabs_count_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_avg_estabs_count_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_avg_emplvl_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_avg_emplvl_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_total_annual_wages_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_total_annual_wages_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_taxable_annual_wages_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_taxable_annual_wages_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_contributions_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_contributions_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_avg_wkly_wage_chg":
#         # 30-40%
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.30, color = 'r')
#         plt.axhline(y = 0.40, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_annual_avg_wkly_wage_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_avg_annual_pay_chg":
#         # 30-40%
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.30, color = 'r')
#         plt.axhline(y = 0.40, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()
#     elif col == "oty_avg_annual_pay_pct_chg":
#         plt.title("Normalized " + str(col))
#         plt.scatter(df2[col].index, df2[col])
#         plt.axhline(y = 0.10, color = 'r')
#         plt.show()
#         plt.title("Histo " + str(col))
#         plt.hist(df2[col])
#         plt.show()













## RUN
# %%
# creating temp to manipulate
temp_df2 = df2.copy(deep=True)
# temp_df3 = temp_df2.copy(deep=True)
# temp_df2_range = df2.copy(deep=True)

# Breaking into quantiles
for col in df2:
    print(str(col))
    if col == "own_code":
        print("1")
        # plt.title("Normalized " + str(col))
        # plt.scatter(df2[col].index, df2[col])
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(df2[col])
        # plt.show()

    elif col == "agglvl_code":
        print("2")
        # plt.title("Normalized " + str(col))
        # plt.scatter(df2[col].index, df2[col])
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(df2[col])
        # plt.show()

    elif col == "annual_avg_estabs_count":
        # 10%
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()

    elif col == "annual_avg_emplvl":
        # 10%
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "total_annual_wages":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "taxable_annual_wages":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "annual_contributions":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "annual_avg_wkly_wage":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "avg_annual_pay":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_annual_avg_estabs_count":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_annual_avg_emplvl":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_total_annual_wages":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_taxable_annual_wages":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_annual_contributions":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_annual_avg_wkly_wage":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "lq_avg_annual_pay":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_avg_estabs_count_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_avg_estabs_count_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_avg_emplvl_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_avg_emplvl_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_total_annual_wages_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_total_annual_wages_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_taxable_annual_wages_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_taxable_annual_wages_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_contributions_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_contributions_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_avg_wkly_wage_chg":
        range = df2[col].max() - df2[col].min()
        thirty_mark = range * 0.30
        fourty_mark = range * 0.40
        # removing all values above mark
        # temp_df2.drop(temp_df2[temp_df2[col] > fourty_mark].index, inplace = True)
        # temp_df2.drop(temp_df2[temp_df2[col] < thirty_mark].index, inplace = True)
        # # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_annual_avg_wkly_wage_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_avg_annual_pay_chg":
        # 30-40%
        range = df2[col].max() - df2[col].min()
        thirty_mark = range * 0.30
        fourty_mark = range * 0.40
        # # removing all values above mark
        # temp_df2.drop(temp_df2[temp_df2[col] > fourty_mark].index, inplace = True)
        # temp_df2.drop(temp_df2[temp_df2[col] < thirty_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()
    elif col == "oty_avg_annual_pay_pct_chg":
        range = df2[col].max() - df2[col].min()
        ten_mark = range * 0.10
        # removing all values above mark
        temp_df2 = temp_df2[temp_df2[col] <= ten_mark]
        # temp_df2.drop(temp_df2[temp_df2[col] > ten_mark].index, inplace = True)
        # plt.title("Normalized " + str(col))
        # plt.scatter(temp_df2[col].index, temp_df2[col])
        # # plt.axhline(y = 0.10, color = 'r')
        # plt.show()
        # plt.title("Histo " + str(col))
        # plt.hist(temp_df2[col])
        # plt.show()

# %%
# pd.read_csv
# pd.write_csv("cleansed_family_income.csv", temp_df2)
temp_df2.to_csv('cleansed_family_income.csv', index=False)

# %%
