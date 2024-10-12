# -*- coding: utf-8 -*-
import csv

def load_lookup_table(lookup_file):
    lookup = {}
    with open(lookup_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            dstport, protocol, tag = row
            lookup[(dstport, protocol.lower())] = tag.lower()
    return lookup

def parse_flow_log(flow_log_file):
    logs = []
    with open(flow_log_file, 'r') as file:
        for line in file:
            # Split flow log based on space delimiter
            parts = line.split()
            if len(parts) >= 12:
                protocol = parts[6]  # Assuming 7th item is protocol
                dstport = parts[4]   # Assuming 5th item is dstport
                logs.append((dstport, protocol))
    return logs

def generate_tag_counts(logs, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}

    for dstport, protocol in logs:
        protocol = protocol.lower()
        tag = lookup_table.get((dstport, protocol), 'untagged')

        # Count tags
        if tag in tag_counts:
            tag_counts[tag] += 1
        else:
            tag_counts[tag] = 1

        # Count port/protocol combinations
        key = (dstport, protocol)
        if key in port_protocol_counts:
            port_protocol_counts[key] += 1
        else:
            port_protocol_counts[key] = 1

    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write Tag Counts
        writer.writerow(["Tag Counts:"])
        writer.writerow(["Tag", "Count"])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])

        writer.writerow([])  # Add an empty row between sections

        # Write Port/Protocol Combination Counts
        writer.writerow(["Port/Protocol Combination Counts:"])
        writer.writerow(["Port", "Protocol", "Count"])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])

# Input file paths
lookup_file = 'lookup_table.csv'
flow_log_file = 'flow_log.txt'
output_file = 'output.csv'

# Load lookup table and parse flow logs
lookup_table = load_lookup_table(lookup_file)
logs = parse_flow_log(flow_log_file)

# Generate counts
tag_counts, port_protocol_counts = generate_tag_counts(logs, lookup_table)

# Write results to output file
write_output(tag_counts, port_protocol_counts, output_file)

print("Output generated in:", output_file)
