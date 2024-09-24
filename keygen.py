import rsa
import stdio
import sys


# Entry point.
def main():
    # Input for low and high value

    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Call function keygen(lo, hi) from rsa library to find public/private keys

    a = rsa.keygen(lo, hi)

    # Output for the three values as tuples.

    stdio.writeln(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]))


if __name__ == '__main__':
    main()
