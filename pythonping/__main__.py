import argparse
import sys 

from pythonping import ping

def main():
    parser = argparse.ArgumentParser(description='Ping a remote host and handle the responses')
    parser.add_argument('target', type=str, help='The remote hostname or IP address to ping')
    parser.add_argument('--timeout', type=float, default=2, help='Time in seconds before considering each non-arrived reply permanently lost')
    parser.add_argument('--count', type=int, default=4, help='How many times to attempt the ping')
    parser.add_argument('--size', type=int, default=1, help='Size of the entire packet to send')
    parser.add_argument('--interval', type=int, default=0, help='Interval to wait between pings')
    parser.add_argument('--payload', type=str, default=None, help='Payload content, leave None if size is set to use random text')
    parser.add_argument('--sweep_start', type=int, default=None, help='If size is not set, initial size in a sweep of sizes')
    parser.add_argument('--sweep_end', type=int, default=None, help='If size is not set, final size in a sweep of sizes')
    parser.add_argument('--df', action='store_true', help="Don't Fragment flag value for IP Header")
    parser.add_argument('--verbose', action='store_true', help='Print output while performing operations')
    parser.add_argument('--out', type=argparse.FileType('w'), default=sys.stdout, help='Stream to which redirect the verbose output')
    parser.add_argument('--match', action='store_true', help='Do payload matching between request and reply')
    parser.add_argument('--source', type=str, default=None, help='Source IP address to use for the ping')
    parser.add_argument('--out_format', type=str, default='legacy', help='How to __repr__ the response')

    args = parser.parse_args()
    print(ping(args.target, timeout=args.timeout, count=args.count, size=args.size, interval=args.interval,
         payload=args.payload, sweep_start=args.sweep_start, sweep_end=args.sweep_end, df=args.df, verbose=args.verbose,
         out=args.out, match=args.match, source=args.source, out_format=args.out_format))

if __name__ == '__main__':
    main()