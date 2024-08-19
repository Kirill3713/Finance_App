# Импортируем нужные модули
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as pdr
plt.rcParams["figure.figsize"] = (10, 6)
# Создаем функции для графиков валют
def plot_euro_usd() -> None:
    """
    Евро к доллару
    """
    plt.style.use('seaborn-v0_8-pastel')
    yf.pdr_override()
    df = pdr.DataReader("EURUSD=X", datetime.datetime.today() - datetime.timedelta(days=365))
    # Создаем график
    plt.plot(df.index, df.Open)
    plt.title("График евро к доллару")
    plt.show()    

def plot_rub_usd() -> None:
    """
    Рубль к доллару
    """
    plt.style.use("seaborn-v0_8-pastel")
    yf.pdr_override()
    df = pdr.DataReader("RUB=X", datetime.datetime.today() - datetime.timedelta(days=365))
    # Создаем график
    plt.plot(df.index, df.Open)
    plt.title("График рубль к доллару")
    plt.show()

def plot_eur_huf() -> None:
    """
    Евро к венгерскому форинту 
    """
    plt.style.use("seaborn-v0_8-pastel")
    yf.pdr_override()
    df = pdr.DataReader("EURHUF=X", datetime.datetime.today() - datetime.timedelta(days=365))
    # Создаем график
    plt.plot(df.index, df.Open)
    # plt.rcParams["figure.figsize"] = (1, 15)
    plt.title("График евро к венгерскому форинту")
    plt.show()

def plot_cyn_usd() -> None:
    """
    Юань к доллару
    """
    plt.style.use("Solarize_Light2")
    yf.pdr_override()
    df = pdr.DataReader("CNY=X", datetime.datetime.today() - datetime.timedelta(days=365))
    # Создаем график
    plt.plot(df.index, df.Open)
    plt.title("График юань к доллару")
    plt.show()


def plot_inr_usd() -> None:
    """
    Индийской рупии к доллару
    """
    plt.style.use("Solarize_Light2")
    yf.pdr_override()
    df = pdr.DataReader("INR=X", datetime.datetime.today() - datetime.timedelta(days=365))
    # Создаем график
    plt.plot(df.index, df.Open)
    plt.title("График индийской рупии к доллару")
    plt.show()

def plot_zar_usd() -> None:
    """
    Южноафриканский ранд к доллару
    """
    plt.style.use("Solarize_Light2")
    yf.pdr_override()
    df = pdr.DataReader("ZAR=X", datetime.datetime.today() - datetime.timedelta(days=365))
    # Создаем график
    plt.plot(df.index, df.Open)
    plt.title("График южноафриканского ранда к доллару")
    plt.show()

# Точка входа в программу
if __name__ == "__main__":
    # plot_eur_huf()
    # plot_euro_usd()
    plot_inr_usd()
    # plot_rub_usd()
    # plot_zar_usd()
    # plot_cyn_usd()