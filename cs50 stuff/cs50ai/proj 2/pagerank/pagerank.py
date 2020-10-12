import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = dict()
    links = corpus[page]
    num_pages = len(corpus)
    num_links = len(links)

    if(links):
        # assigns probabilities to each key of the corpus
        for key in corpus:
            distribution[key] = (1 - damping_factor) / num_pages

        # assigns probabilities for each key (page) in corpus.
        for key in links:
            distribution[key] = distribution[key] + (damping_factor / num_links)

    else:
        # assigns probabilities for a case where a page has no links from it
        for key in corpus:
            distribution[key] = 1.0 / num_pages

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = dict().fromkeys(corpus.keys(), 0)
    currentpage = random.choices(list(corpus.keys()))[0]

    for i in range(1, n):
        current_dist = transition_model(corpus, currentpage, damping_factor)
        for pagerankValue in pagerank:
            pagerank[pagerankValue] = (((i - 1) * pagerank[pagerankValue]) + current_dist[pagerankValue]) / i
        currentpage = random.choices(list(pagerank.keys()), weights = list(pagerank.values()), k = 1)[0]

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = dict()

    # add all pages in corpus to pagerank and give initial values 1/n
    for everypage in corpus:
        pagerank[everypage] = 1 / len(corpus)
    
    # calculate new pagerank values
    while True:
        loop = False
        for p in pagerank:
            # get starting pagerank to check difference
            startrank = pagerank[p]
            # calculate probability of randomly landing on page
            probability = (1 - damping_factor / len(corpus))
            # check all pages in corpus
            for page in corpus.keys():
                # if page has a link to p, update probability
                if(p in corpus[page]):
                    probability = probability + (damping_factor * (pagerank[page] / len(corpus[page])))
            # update pagerank
            pagerank[p] = probability
            # if value for any page has changed by more than 0.001, loop again
            if(abs(startrank - probability) > 0.001):
                loop = True

        if(not loop):
            break

    # normalize all pagerank values
    alpha = 1 / sum(pagerank.values())
    for page in pagerank:
        pagerank[page] = alpha * pagerank[page]

    return pagerank


if __name__ == "__main__":
    main()
