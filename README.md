# peakrunner

`peakrunner` accepts requests from `peakorc` and starts `peaktest` container images with the appropriate parameters.

### running peakrunner (development)

Ensure Docker is installed and configured on the `peakrunner` host, and the `peaktest:latest` image is available.

Create a virtualenv and use pip to intall the latest `peakrunner` from source:
```
$ virtualenv peakenv
$ source peakenv/bin/activate
(peakenv)$ git clone https://github.com/peak-oss/peakrunner.git
(peakenv)$ cd peakrunner
(peakenv)$ pip install -e .
```
You can then use the local script to start an instance of `peakrunner`
```
(peakenv)$ peakrunner
[2018-03-18 12:19:55 +0000] [20903] [INFO] Starting gunicorn 19.7.1
[2018-03-18 12:19:55 +0000] [20903] [INFO] Listening at: http://0.0.0.0:6511 (20903)
[2018-03-18 12:19:55 +0000] [20903] [INFO] Using worker: sync
[2018-03-18 12:19:55 +0000] [20908] [INFO] Booting worker with pid: 20908
```
Note that you can optionally provide a bind host and port for the service:
```
(peakenv)$ peakrunner -b 0.0.0.0 -p 6100
```
