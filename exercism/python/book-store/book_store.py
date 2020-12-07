from collections import Counter, defaultdict

rates = [1.0, 1.0, 0.95, 0.90, 0.80, 0.75]

def total(basket):
    num_bundles_by_size = defaultdict(int)
    title_counts = Counter(basket)
    while title_counts:
        titles = title_counts.keys()
        num_bundles_by_size[len(titles)] = num_bundles_by_size[len(titles)] + 1
        title_counts.subtract(titles)
        title_counts = title_counts + Counter()

    fixes = min(num_bundles_by_size[5], num_bundles_by_size[3])
    num_bundles_by_size[5] = num_bundles_by_size[5] - fixes
    num_bundles_by_size[3] = num_bundles_by_size[3] - fixes
    num_bundles_by_size[4] = num_bundles_by_size[4] + (2 * fixes)

    return sum(num_bundles * bundle_size * 800 * rates[bundle_size] for (bundle_size, num_bundles) in num_bundles_by_size.items())
