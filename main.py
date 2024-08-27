import ipaddress
import sys

def cidr_to_ips(cidr):
    """Convert CIDR to a list of IP addresses."""
    network = ipaddress.ip_network(cidr, strict=False)
    return [str(ip) for ip in network.hosts()]

def process_file(input_file, output_file):
    """Process CIDRs from a file and save results to an output file."""
    with open(input_file, 'r') as infile:
        cidrs = infile.readlines()
    
    with open(output_file, 'w') as outfile:
        for cidr in cidrs:
            cidr = cidr.strip()
            if cidr:
                ip_addresses = cidr_to_ips(cidr)
                outfile.write('\n'.join(ip_addresses) + '\n')

def process_single_cidr(cidr, output_file):
    """Process a single CIDR and save results to an output file."""
    ip_addresses = cidr_to_ips(cidr)
    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(ip_addresses) + '\n')

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file_or_cidr> <output_file>")
        sys.exit(1)
    
    input_source = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Check if input_source is a file
        with open(input_source, 'r') as infile:
            # If we can open the file, treat input_source as a file
            process_file(input_source, output_file)
    except FileNotFoundError:
        # If file is not found, treat input_source as a single CIDR
        process_single_cidr(input_source, output_file)

if __name__ == "__main__":
    main()
