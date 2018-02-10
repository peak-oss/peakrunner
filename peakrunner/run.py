from subprocess32 import call
import argparse


def main():
    """Entry point for the peakrunner application

    Allows a bind port and address to be specified via command-line switches,
    and then executes a gunicorn process.
    """
    parser = argparse.ArgumentParser(description='peakrunner')
    parser.add_argument('-b', '--bind', dest='bind', default='0.0.0.0',
                        help='bind address (default: 0.0.0.0)')
    parser.add_argument('-p', '--port', dest='port', default='6511',
                        help='bind port (default: 6511)')

    args = parser.parse_args()
    call(['gunicorn', '--bind', "{0}:{1}".format(args.bind, args.port),
          'peakrunner.peakrunner:api'])
