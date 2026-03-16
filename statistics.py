def get_stat_arrays(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()

    results = {}
    current_label = ""
    buffer_text = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if '[' not in line and ']' not in line and ',' not in line:
            current_label = line
            if current_label not in results:
                results[current_label] = {"means": [], "stds": []}
            buffer_text = ""
            continue

        buffer_text += line

        if ']' in line:
            clean_text = buffer_text.replace('[', '').replace(']', '').replace("'", "")
            raw_elements = clean_text.split(',')

            values = []
            for element in raw_elements:
                clean_val = element.strip()
                if clean_val:
                    values.append(float(clean_val))

            for i in range(0, len(values), 10):
                batch = values[i: i + 10]
                if not batch:
                    continue

                n = len(batch)
                total_sum = 0.0
                for x in batch:
                    total_sum += x
                mean = total_sum / n

                var_sum = 0.0
                for x in batch:
                    var_sum += (x - mean) ** 2

                std = (var_sum / n) ** 0.5

                results[current_label]["means"].append(f"{mean:.8f}")
                results[current_label]["stds"].append(f"{std:.8f}")

            buffer_text = ""

    return results

if __name__=="__main__":
    data_stats = get_stat_arrays('line_a_times.txt')

    for alg, stats in data_stats.items():
        print(f"Algorithm: {alg}")
        print(f"Means: [{', '.join(stats['means'])}]")
        print(f"Stds:  [{', '.join(stats['stds'])}]")
        print("-" * 30)