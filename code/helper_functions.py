import os
import shutil
import glob
import requests
import config
import pandas as pd

root_folder = '../data'
raw_folder = f'{root_folder}/raw_folder'
raw_folder_renamed = f'{root_folder}/raw_folder_renamed'
clean_folder_renamed = f'{root_folder}/clean_folder_renamed'
csv_folder = f'{root_folder}/csv'
raw_download_date = '01-07-2020'
raw_filename = f'EL IMAN RESTAURANT-Sales Report {raw_download_date}'


dict_month_names = {0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr',
                    4: 'May', 5: 'Jun', 6: 'Jul', 7: 'Aug',
                    8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec'}

dict_months = {
    '2015_01': [1420088400000, 1422766799000], '2015_02': [1422766800000, 1425185999000],
    '2015_03': [1425186000000, 1427860799000], '2015_04': [1427860800000, 1430452799000],
    '2015_05': [1430452800000, 1433131199000], '2015_06': [1433131200000, 1435723199000],
    '2015_07': [1435723200000, 1438401599000], '2015_08': [1438401600000, 1441079999000],
    '2015_09': [1441080000000, 1443671999000], '2015_10': [1443672000000, 1446350399000],
    '2015_11': [1446350400000, 1448945999000], '2015_12': [1448946000000, 1451624399000],

    '2016_01': [1451624400000, 1454302799000], '2016_02': [1454302800000, 1456808399000],
    '2016_03': [1456808400000, 1459483199000], '2016_04': [1459483200000, 1462075199000],
    '2016_05': [1462075200000, 1464753599000], '2016_06': [1464753600000, 1467345599000],
    '2016_07': [1467345600000, 1470023999000], '2016_08': [1470024000000, 1472702399000],
    '2016_09': [1472702400000, 1475294399000], '2016_10': [1475294400000, 1477972799000],
    '2016_11': [1477972800000, 1480568399000], '2016_12': [1480568400000, 1483246799000],

    '2017_01': [1483246800000, 1485925199000], '2017_02': [1485925200000, 1488344399000],
    '2017_03': [1488344400000, 1491019199000], '2017_04': [1491019200000, 1493611199000],
    '2017_05': [1493611200000, 1496289599000], '2017_06': [1496289600000, 1498881599000],
    '2017_07': [1498881600000, 1501559999000], '2017_08': [1501560000000, 1504238399000],
    '2017_09': [1504238400000, 1506830399000], '2017_10': [1506830400000, 1509508799000],
    '2017_11': [1509508800000, 1512104399000], '2017_12': [1512104400000, 1514782799000],

    '2018_01': [1514782800000, 1517461199000], '2018_02': [1517461200000, 1519880399000],
    '2018_03': [1519880400000, 1522555199000], '2018_04': [1522555200000, 1525147199000],
    '2018_05': [1525147200000, 1527825599000], '2018_06': [1527825600000, 1530417599000],
    '2018_07': [1530417600000, 1533095999000], '2018_08': [1533096000000, 1535774399000],
    '2018_09': [1535774400000, 1538366399000], '2018_10': [1538366400000, 1541044799000],
    '2018_11': [1541044800000, 1543640399000], '2018_12': [1543640400000, 1546318799000],

    '2019_01': [1546318800000, 1548997199000], '2019_02': [1548997200000, 1551416399000],
    '2019_03': [1551416400000, 1554091199000], '2019_04': [1554091200000, 1556683199000],
    '2019_05': [1556683200000, 1559361599000], '2019_06': [1559361600000, 1561953599000],
    '2019_07': [1561953600000, 1564631999000], '2019_08': [1564632000000, 1567310399000],
    '2019_09': [1567310400000, 1569902399000], '2019_10': [1569902400000, 1572580799000],
    '2019_11': [1572580800000, 1575176399000], '2019_12': [1575176400000, 1577854799000]
}


def raw_file_clean(dict_months):
    """
    Put files in the root directory
    File names are required to be named as: EL IMAN RESTAURANT-Sales Report 01-07-2020.csv
    That is how clover default saves the file 
    """

    index = 0
    for month, url in dict_months.items():
        if month == '2015_01':
            cleaned_df = pd.read_csv(
                f'{raw_folder}/{raw_filename}.csv', header=1, skiprows=11)
            if cleaned_df.columns[-1] != 'Total':
                cleaned_df = pd.read_csv(
                    f'{raw_folder}/{raw_filename}.csv', header=1, skiprows=10)
            shutil.copyfile(f'{raw_folder}/{raw_filename}.csv',
                            f"{raw_folder_renamed}/{month}_el_iman_sales_report.csv")
            cleaned_df.to_csv(
                f"{clean_folder_renamed}/{month}_el_iman_sales_report_cleaned.csv", index=False)
        else:
            index += 1
            cleaned_df = pd.read_csv(
                f'{raw_folder}/{raw_filename} ({index}).csv', header=1, skiprows=11)
            if cleaned_df.columns[-1] != 'Total':
                cleaned_df = pd.read_csv(
                    f'{raw_folder}/{raw_filename} ({index}).csv', header=1, skiprows=10)
            shutil.copyfile(f'{raw_folder}/{raw_filename} ({index}).csv',
                            f"{raw_folder_renamed}/{month}_el_iman_sales_report.csv")
            cleaned_df.to_csv(
                f"{clean_folder_renamed}/{month}_el_iman_sales_report_cleaned.csv", index=False)

    for filename in os.listdir(clean_folder_renamed):
        if 'cleaned.csv' in filename:
            df = pd.read_csv(f'{clean_folder_renamed}/{filename}')

            for index in range(df.shape[0]):
                if df.loc[index][0] == 'Net Sales':
                    net_sales = index

            df_net_sales = pd.DataFrame(df.iloc[net_sales])
            df_net_sales.columns = df_net_sales.iloc[0]
            df_net_sales = df_net_sales[1:]

            # drop 'totals row'
            df_net_sales.drop(df_net_sales.tail(1).index, inplace=True)

            df_net_sales.to_csv(
                f'{csv_folder}/{filename[:7]}_net_sales.csv', header=False)

    for filename in os.listdir(csv_folder):
        if '_net_sales.csv' in filename:
            df = pd.read_csv(f'{csv_folder}/{filename}', header=None)
            df.columns = ['date', 'total']
            df['date'] = df['date'] + ' ' + filename[:4]
            df.to_csv(
                f'{csv_folder}/{filename[:7]}_net_sales.csv', header=True, index=False)

    list_csv_files = []
    for infile in glob.glob(f"{csv_folder}/*.csv"):
        dataframe = pd.read_csv(infile)
        list_csv_files.append(dataframe)

    df = pd.concat(list_csv_files, sort=False, ignore_index=True)
    df['total'] = df['total'].str.replace("$", "").str.replace(",", "")
    df['date'] = pd.to_datetime(df['date'])
    df['total'] = df['total'].astype(float)
    df = df.sort_values(by=['date'])
    df.to_csv(f'{root_folder}/net_sales_total.csv', header=True, index=False)


def call_dark_sky_api(epoch_time):
    parameters = {
        "exclude": "currently,minutely,hourly,flags",
    }

    response = requests.get(
        f"https://api.darksky.net/forecast/{config.darksky_api_key}/{config.elizabeth_nj},{epoch_time}", params=parameters)

    json_response = response.json()

    df = pd.DataFrame(json_response['daily']['data'])
    df['time'] = pd.to_datetime(df['time'], unit='s', origin='unix')
    df['time'] = pd.to_datetime(df['time'].dt.date)

    return df
