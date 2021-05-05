from ipwhois import IPWhois
from datetime import datetime as dt


path_name = input("Pleae provide full path of the file you wish to parse: ")


def build_from_source(path):
    data_list = []
    try:
        with open(path, "r") as f:
            print("### READING SOURCE DATA ###")
            print(path)
            data = f.read().split("\n")
            f.close()
            for e in data:
                data_list.append(e.split(","))
            parse_source_data(data_list)

    except FileNotFoundError:
        print(f"FILE NOT FOUND. PLEASE CHECK THE PATH {path} EXISTS")
        exit(1)


ip_dict = {}
block_dict = {}


def parse_source_data(data):
    print("### PARSING SOURCE DATA ###")
    data.pop(-1)
    data.pop(0)
    for entry in data:
        try:
            if entry[6]:
                ip = entry[6].replace('"', "")
                count = entry[1].replace('"', "")
                block = f'blocked by {entry[4]} trying to access {entry[5]}'
                if ip not in ip_dict.keys():
                    ip_dict[ip] = int(count)
                    block_dict[ip] = block
                else:
                    ip_dict[ip] += int(count)
        except ValueError:
            pass
    count_blocks()


blocks_total = 0
blocks_unique = 0


def count_blocks():
    global blocks_total
    global blocks_unique
    sorted_list = {k: v for k, v in sorted(ip_dict.items(), reverse=True, key=lambda x: x[1])}
    for s in sorted_list:
        blocks_total += sorted_list[s]
        blocks_unique += 1

    get_whois(sorted_list)


def get_whois(sl):
    owners = []
    top_one_hundred = dict(list(sl.items()))[0: 100]
    print("### GATHERING WHOIS DATA ###")
    for k in top_one_hundred:
        info = IPWhois(k).lookup_whois()
        try:
            if info["nets"][0]["description"].lower() != "na" and info["nets"][0]["description"].lower() != "n/a" and \
                    "\n" not in info["nets"][0]["description"]:
                owners.append(info["nets"][0]["description"].replace(',', " "))
            elif info["nets"][0]["name"].lower() != "na" and info["nets"][0]["name"].lower() != "n/a" and "\n" not in \
                    info["nets"][0]["name"]:
                owners.append(info["nets"][0]["name"])
        except AttributeError:
            if info["asn_description"].lower() != "na" and info["asn_description"].lower() != "n/a" and \
                    "\n" not in info["asn_description"]:
                owners.append(info["asn_description"])

            else:
                owners.append("Unable to locate Owner")
    parse_data(top_one_hundred, owners, sl)


csv_list = []


def parse_data(top, owners, ip_sorted):
    print("### PARSING ALL DATA ###")
    idx = 0
    for i in top:
        host_dict = {"ip": i, "blocks": str(ip_sorted[i]), "owner": owners[idx], "block": block_dict[i] }
        csv_list.append(host_dict)
        idx += 1
    write_file(csv_list)


def write_file(csv):
    print("### WRITING TO OUTPUT FILE ###")
    now = str(dt.now().strftime("%Y_%m_%d_$H$M$S"))
    new_file = f"./{now}.output.csv"
    column_headers_written = False
    total_unique_blocks_written = False
    with open(new_file, "w") as fw:
        if not column_headers_written:
            fw.write("Unique Blocks, Total Blocks, Source IP, Blocks, Owner, Blocked by \n")
            column_headers_written = True
        fw.close()
    with open(new_file, "a") as fa:
        for i in csv:
            if not total_unique_blocks_written:
                fa.write(f'{blocks_unique}, {blocks_total}, {i["ip"]}, {i["blocks"]}, {i["owner"]}, {i["block"]} \n')
            else:
                fa.write(f', , {i["ip"]}, {i["blocks"]}, {i["owner"]}, {i["block"]} \n')

        fa.close()
    print(f'### CSV FILE CREATED {new_file}')


build_from_source(path_name)
