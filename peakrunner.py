import falcon
import docker


class PeakStart():

    def start_test(self, url, num_requests, status_uri, uuid):

        client = docker.from_env(version="auto")
        env = {'REQUESTS': num_requests, 'URL': url,
               'STATUS_URI': status_uri,
               'UUID': uuid}
        # RH docker 1.12 does not support auto-remove
        client.containers.run("peaktest:latest", detach=True, environment=env)

    def on_post(self, req, resp):
        requests = int(req.get_header('requests'))
        url = req.get_header('test-url')
        status_uri = req.get_header('status-uri')
        test_uuid = req.get_header('uuid')

        self.start_test(url, requests, status_uri, test_uuid)


api = falcon.API()

peak_start = PeakStart()
api.add_route('/start', peak_start)
