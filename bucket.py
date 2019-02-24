def bucket_sort(array, bucket_size):
    if len(array) == 1:
        return array
    min_val = min(array)
    max_val = max(array)
    num_bucket = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(num_bucket)]
    for x in array:
        buckets[(x - min_val) // bucket_size].append(x)
    sort_arr = []
    for bucket in buckets:
        bucket.sort()
        for x in bucket:
            sort_arr.append(x)
    return sort_arr

def main():
    array = [int(s) for s in input().split()]
    print(bucket_sort(array, len(array)))

if __name__ == '__main__':
    main()
