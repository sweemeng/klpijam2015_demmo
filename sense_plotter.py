from sense_hat import SenseHat
import pandas
import datetime
import time
import logging
import matplotlib

matplotlib.use("agg")

def collect_data(sense):
    timestamp = []
    p_temp = []
    h_temp = []
    humidity = []
    pressure = []
    logging.warn("generating data")
    for i in range(10):
        timestamp.append(datetime.datetime.now())
        tpt = sense.get_temperature_from_pressure()
        logging.warn(tpt)
        p_temp.append(tpt)
        tht = sense.get_temperature_from_humidity()
        logging.warn(tht)
        h_temp.append(tht)
        th = sense.get_humidity()
        logging.warn(th)
        humidity.append(th)
        tp = sense.get_pressure()
        logging.warn(tp)
        pressure.append(tp)
        time.sleep(2)
    return timestamp, p_temp, h_temp, humidity, pressure


def main():
    sense = SenseHat()
    logging.warn("assemble data")
    timestamp, p_temp, h_temp, humidity, pressure = collect_data(sense)
    data =  {
        "pressure_temp": p_temp,
        "humidity_temp": h_temp,
        "humidity": humidity,
        "pressure": pressure,
    }
    df = pandas.DataFrame(data, index=timestamp)
    logging.warn(df)
    logging.warn("save to csv")
    df.to_csv("sense_data.csv")
    logging.warn("plotting")
    ax = df.plot()
    fig = ax.get_figure()
    fig.savefig("sense.png")

if __name__ == "__main__":
    main()


