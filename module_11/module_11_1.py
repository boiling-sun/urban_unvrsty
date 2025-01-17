"""
Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. 
К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) 
и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека 
и как вы расширили возможности Python с её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
"""

"""
"Анализ и визуализация данных о погоде"

Программа будет запрашивать данные о погоде с API, проводить небольшой анализ этих данных,
а затем визуализировать результаты и сохранять полученные данные и графики.

Эта программа демонстрирует, как можно расширить стандартные возможности Python:
использовать requests для получения данных о погоде с веб-сервиса, 
pandas для их анализа и обработки, а также matplotlib для визуализации результатов. 

Примеры вывода программы (графики, данные) в папке 11_1_output
"""
import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
import sys
import pprint

url = "http://api.weatherapi.com/v1/forecast.json"
params = {
    "key": "82ccae6f05344794b45175923251401",   
    "q": "Bangkok",                    
    "days": 3,                                  
}

def get_forecast_response_json(params):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        sys.exit(f'Request error: {response.status_code}')

def get_current_location_info(json_forecast_data):
    location = f'{json_forecast_data["location"]["name"]}, {json_forecast_data["location"]["country"]}'
    local_time = f'{json_forecast_data["location"]["localtime"]}'

    current_weather = f'{json_forecast_data["current"]["temp_c"]} °C, ' + \
                      f'{json_forecast_data["current"]["condition"]["text"]}'

    return location, local_time, current_weather

def get_weather_data(json_forecast_data):
    forecast = json_forecast_data["forecast"]["forecastday"]
    index = []
    hourly_forecast_info = []
    for day in forecast:
        date = day["date"]
        for hour in day["hour"]:
            index.append((date, hour["time"][11:]))
            info = {
                "temp_c": hour["temp_c"],
                "wind_kph": hour["wind_kph"],
                "pressure_mb": hour["pressure_mb"],
                "humidity": hour["humidity"],
                "chance_of_rain": hour["chance_of_rain"],
                "chance_of_snow": hour["chance_of_snow"],
                "vis_km": hour["vis_km"]
            }
            hourly_forecast_info.append(info)
    multiindex = pd.MultiIndex.from_tuples(index, names=['date', 'time'])
    return pd.DataFrame(hourly_forecast_info, index=multiindex)

def get_dates_from_dataframe(df):
    return list(df.index.get_level_values('date').unique())

def get_correlation_matrix(df):
    return df.corr()

def get_statistic_temperature_data(df):
    daily_temp = df.groupby(level='date')['temp_c'].agg(['max', 'min', 'mean', 'median'])
    max_temp = daily_temp['max']
    min_temp = daily_temp['min']
    mean_temp = daily_temp['mean']
    median_temp = daily_temp['median']
    return max_temp, min_temp, mean_temp, median_temp

def plot_hourly_temperature(info, current):
    days = get_dates_from_dataframe(info)
    location, local_time, current_weather = current

    fig, axs = plt.subplots(len(days), 1, figsize=(8, 6), sharex='all', sharey='all')
    fig.suptitle(f'{location}\nМестное время: {local_time}\nТекущая погода: {current_weather}\n', 
                 style='oblique')
    for i, day in enumerate(days):
        daily_data = info.loc[day]
        axs[i].plot(daily_data.index.get_level_values('time'), daily_data['temp_c'], marker='o', label=f'{day}')
        if i == 1:
            axs[i].set_ylabel('Температура (°C)')
        if i == 2:
            axs[i].set_xlabel('Время')
            axs[i].tick_params(axis='x', rotation=45)

        axs[i].set_title(f'{day}', fontsize=12)
        axs[i].grid()

    plt.tight_layout()
    return fig

def plot_daily_statistics(info, current):
    days = get_dates_from_dataframe(info)
    max_temp, min_temp, mean_temp, median_temp = get_statistic_temperature_data(info)
    location, local_time, current_weather = current
    
    fig = plt.figure()
    fig.suptitle(f'{location}\nМестное время: {local_time}\nТекущая погода:{current_weather}\n', 
                 style='oblique')
    
    # графики
    plt.fill_between(days, mean_temp, max_temp, color='lightcoral', alpha=0.5, label='Выше средней')
    plt.fill_between(days, min_temp, mean_temp, color='lightblue', alpha=0.5, label='Ниже средней')
    plt.plot(days, mean_temp, 'k-', label='Средняя температура')
    plt.plot(days, median_temp, 'm:', label='Медианная температура')

    # аннотации
    for date, max_val, min_val, mean_val in zip(days, max_temp, min_temp, mean_temp):
        plt.annotate(f'{max_val:.1f}', xy=(date, max_val), xytext=(date, max_val + 0.25))
        plt.annotate(f'{min_val:.1f}', xy=(date, min_val), xytext=(date, min_val - 0.25))
        plt.annotate(f'{mean_val:.1f}', xy=(date, mean_val), xytext=(date, mean_val + 0.1))

    #plt.xticks(rotation=45)

    plt.ylabel('Температура (°C)')
    plt.ylim(min(min_temp - 2), max(max_temp) + 2)

    plt.title('Статистика температуры по дням')

    plt.legend(fontsize='x-small')
    plt.grid(True)

    plt.tight_layout()
    return fig

def plot_correlation_matrix(info, current):
    corr_matrix = get_correlation_matrix(info)
    location, local_time, current_weather = current

    fig = plt.figure(figsize=(7, 6))
    fig.suptitle(f'{location}\nМестное время: {local_time}\nТекущая погода: {current_weather}\n', 
                 style='oblique')

    im = plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)

    # подписи значений
    for i in range(len(corr_matrix)):
        for j in range(len(corr_matrix)):
            plt.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}', ha='center', va='center')

    # подписи осей
    plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=90)
    plt.yticks(range(len(corr_matrix)), corr_matrix.columns)

    plt.colorbar(im, label='Корреляция')

    plt.title('Корреляционная матрица параметров погоды')
    plt.tight_layout()

    return fig

def save_figure_as_png(fig, file_name):
    path = format_file_name(file_name, '.png')
    fig.savefig(path, dpi=200)
    print(f'{path} сохранен')

def format_file_name(file_name, ext):
    file_name = file_name.replace(', ', '_').replace(' ', '_') + ext
    formatted_file_name = os.path.join('module_11', '11_1_output', file_name)
    return formatted_file_name

def save_data_as_json(df, file_name):
    path = format_file_name(file_name, '.json')
    df.to_json(path, orient='table', indent=4)
    print(f'{path} сохранен')

def main():
    json_forecast_data = get_forecast_response_json(params)
    info = get_weather_data(json_forecast_data)
    current = get_current_location_info(json_forecast_data)
    
    plotting = (plot_hourly_temperature, plot_daily_statistics, plot_correlation_matrix)
    
    figs = [func(info, current) for func in plotting]

    save_data_as_json(info, f'{current[0]} data')

    for fig, func in zip(figs, plotting):
        save_figure_as_png(fig, f'{current[0]}_{func.__name__}')

    plt.show()


if __name__ == '__main__':
    main()
