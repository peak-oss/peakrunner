# peakrunner

`peakrunner` accepts requests from `peakorc` and starts `peaktest` container images with the appropriate parameters.

### running peakrunner

Ensure Docker is installed and configured on the `peakrunner` host, and the `peaktest:latest` image is available.

Create a virtualenv and install the requirements.

You can then start a `peakrunner` instance using gunicorn:

```
gunicorn --bind 0.0.0.0:6511 peakrunner:api
```
