import falcon
import docker


class PeakStart():
    """Handles requests to start peaktest containers

    This class handles POST requests from peakorc to start containers. It
    utilises the docker-py library to start peaktest containers.

    The docker environment is assumed to be setup on the host running this
    service.
    """

    def start_test(self, url, num_requests, status_uri, uuid):
        """Starts peaktest Docker containers

        Uses the docker-py library to start peaktest container images
        with parameters specified in an API request.

        Args:
            url (string): the url to be tested
            num_requests (int): the number of requests to make
            status_uri (string): the `peakorc` API to post test results to
            uuid (string): the `peakorc` UUID reference for this specific test
        """

        client = docker.from_env(version="auto")
        env = {'REQUESTS': num_requests, 'URL': url,
               'STATUS_URI': status_uri,
               'UUID': uuid}
        # RH docker 1.12 does not support auto-remove
        client.containers.run("peaktest:latest", detach=True, environment=env)

    def on_post(self, req, resp):
        """Handles POST requests

        Args:
            req: the falcon HTTP request object
            resp: the falcon HTTP response object
        """

        requests = int(req.get_header('requests'))
        url = req.get_header('test-url')
        status_uri = req.get_header('status-uri')
        test_uuid = req.get_header('uuid')

        self.start_test(url, requests, status_uri, test_uuid)


api = falcon.API()

peak_start = PeakStart()
api.add_route('/start', peak_start)
