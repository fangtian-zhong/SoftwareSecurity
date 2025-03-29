# Software Vulnerability Analysis Across Programming Language and Program Representation Landscapes: A Survey

**The dataset is available here:** [Dataset](https://github.com/fangtian-zhong/SoftwareSecurity/blob/main/Dataset.md)

------

## How to Use the Paper Crawling Code

### Retrieve PDF Links of Papers

You can implement your crawling logic in the `main.py` file by calling the functions defined in other `*.py` files.

To crawl papers from the ACM Digital Library, use the `search_acm(title, keyword, store_path)` function defined in `search.py` to retrieve metadata of the target papers and save the results in a CSV file.

```python
def search_acm(title, keyword, store_path):
    """
    Retrieve metadata of target articles from the ACM Digital Library and store them in a CSV file.
    
    :param title: Keyword(s) from the article title.
    :param keyword: Keyword(s) from the abstract.
    :param store_path: File path to save the CSV data.
    :return: None
    """
```

Similarly, you can crawl papers from the IEEE Xplore and Springer libraries:

```python
def search_ieee(keyword, store_path):
    """
    Retrieve metadata of articles from IEEE Xplore and save them in a CSV file.
    
    :param keyword: Keyword(s) for the search.
    :param store_path: File path to save the CSV data.
    :return: None
    """

def search_springer(keyword, store_path, file):
    """
    Retrieve metadata of articles from the Springer database and save them in a CSV file.

    :param keyword: Keyword(s) for the search.
    :param store_path: Directory where metadata will be stored.
    :param file: File path to log failed URLs.
    :return: None
    """
```

Additionally, you can crawl papers from Google Scholar by calling these functions:

`````python
def search_papers(base_url, keyword):
    """
    Retrieve paper links by performing a search on the Google Scholar using the given keyword.

    :param base_url: "https://scholar.google.com/scholar?q="
    :param keyword: Keyword(s) used to search for relevant papers.
    :return: A list of URLs pointing to the search results or paper entries.
    """


def store_links(store_path, url_list):
    """
    Save a list of paper URLs to a CSV file for manual download.

    :param store_path: The path where the CSV file will be saved.
    :param url_list: A list of paper URLs retrieved from the search_papers function.
    :return: None
    """

`````



------

### Downloading PDF Files

We have implemented functions to download PDF files from the ACM and Springer libraries. Unfortunately, downloading from IEEE is not yet supported due to its download restrictions.

To download articles from ACM:

```python
def download_pdf_acm(url_list, from_, store_to_path, file):
    """
    Download PDF files of articles from the ACM Digital Library.

    :param url_list: List of article URLs.
    :param from_: Starting index in the URL list.
    :param store_to_path: Destination folder to save the PDFs.
    :param file: File to log URLs that fail to download.
    :return: None
    """
```

> **Note:** ACM enforces an IP-based download limit (approximately 30 articles per IP). As a result, downloading may be slow and manual downloads might be more efficient.

To download articles from Springer, use the `download_pdf` function in `dealfile.py`:

```python
def download_pdf(pdf_url, store_path, seq_num, file):
    """
    Download a PDF from the given URL to the target directory.

    :param pdf_url: URL of the article PDF.
    :param store_path: Directory to save the downloaded article.
    :param seq_num: Index or count of articles downloaded so far.
    :param file: File to record failed download URLs.
    :return: None
    """
```


To download articles from IEEE and Google Scholar, you should do that manually.


------

### Final Processing of Downloaded Papers

We perform filtering and categorization based on two major rules:

1. **Filter based on paper length:**
   - Single-column articles with fewer than 20 pages are discarded.
   - Double-column articles with fewer than 10 pages are also discarded.
2. **Categorization based on keywords:**
    Papers are categorized according to the presence of specific keywords in their title or abstract.

You can apply these operations using methods defined in `Filter.py`. For example, for Springer articles:

```python
class Springer_filter:
    """
    This class provides filtering and categorization methods for articles retrieved from Springer.
    """
    
    def __init__(self, article_path, article_filter_to, csv_path, wrong_folder_name):
        self.article_path = article_path
        self.article_filter_to = article_filter_to
        self.csv_path = csv_path
        self.wrong_folder = wrong_folder_name

    def convert_name(self, url_key):
        """
        Rename articles in sequential order (e.g., 1.pdf, 2.pdf, ... n.pdf), based on a key from the CSV file.
        """
        
    def delete_size_lower(self, filter_size):
        """
        Remove articles that do not meet the page length requirement.
        :param filter_size: Threshold for filtering based on the number of pages.
        """
        
    def get_title_and_abstract(self, article_name, just_title):
        """
        Extract the title and/or abstract of a given paper.
        """
        
    def filtering_abstractAndtitle(self, keywords, target_folder, just_title):
        """
        Categorize papers based on keywords found in their title or abstract.

        :param keywords: A list of keywords used for categorization.
        :param target_folder: Directory to store the categorized papers.
        :param just_title: Boolean indicating whether to filter using title only.
        """
```

Similar filtering classes and methods are provided for IEEE and ACM papers in the same file.

### If you use our code, please cite the following paper by
@article{qian2025software,
  title={Software Vulnerability Analysis Across Programming Language and Program Representation Landscapes: A Survey},
  author={Qian, Zhuoyun and Zhong, Fangtian and Hu, Qin and Jiang, Yili and Huang, Jiaqi and Ren, Mengfei and Yu, Jiguo},
  journal={arXiv preprint arXiv:2503.20244},
  year={2025}
}
