# Watching You Project


### How to start
1. Clone the repository

```
git clone git@github.com:rytst/watching_you.git
```

2. Put `.env` file for the settings of [Influxdb](https://www.influxdata.com/) and [Grafana](https://grafana.com/).


3. Start the containers

```
docker compose up -d
```

4. Execute the following command
```
python main.py
```

### How to stop

```
docker compose down
```

If you want to remove all data about the containers of [Influxdb](https://www.influxdata.com/) and [Grafana](https://grafana.com/), then execute the following command.
```
docker compose down -v
```
