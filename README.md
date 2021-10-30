# schulich-cibc-acp-21
This project is intended to build connection graphs of high-net worth people in Canada.

1. Run the [namelist crawler](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/namelistcrawler/main.py) to get the names and basic profile information from yahoo finance.
   This crawler is modified from [yahoo_finance_scrap](https://github.com/Jaydeeph/MakeMeMoney/blob/809ca2a560858f6559d94f9f18a218bb715fcc4a/python_scripts/yahoo_finance_scrape.py).
2. Send a [name list](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/searchenginecrawler/namelist_canada_2.csv) to [search engine crawler](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/searchenginecrawler/bingcrawler.py). (When quotation marks are added to the key words, search engine will only return the results that exactly contain the targets that you need, meaning that the search amount can represent the connection strength between 2 targets. In this project I use bing to get the search amounts, and the reason is that the search results of bing are more accurate than the ones of google, and the anti-crawler algorithm is too powerful).
   [proxy ips](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/searchenginecrawler/getproxyip.py) and random sudo-headers are applied, and the crawler can be run on an AWS instance.
3. Draw the graphs with [pyecharts](https://pyecharts.org/#/en-us/). You will need to prepare 3 variables: [categories](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/categories.csv), [links.csv](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/links), and [nodes](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/nodes.csv).
4. 2 different types of graphs are provided: [circular](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/graph_2million.py) and [float](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/graph_2million_net.py)
5. The strength level is defined by the total search amount of a people, the size of a dot is defined by the total number of connections with other people.

# Screenshot of samples

1. The outputs are based on the executives (126 people) whose anual salaries are higher than 2 million CAD and coming from Canadian listed companies.
2. The final interactive outputs from pyecharts are coded in html. Please download them [circular](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/graph_1.html) [float](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/graph_2million_net.py) to read them in full functions.

![alt text](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/2021-10-29_190310.png?raw=true)
![alt text](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/2021-10-29_190338.png?raw=true)
![alt text](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/2021-10-29_190400.png?raw=true)
![alt text](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/2021-10-29_190204.png?raw=true)
![alt text](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/2021-10-29_190433.png?raw=true)
![alt text](https://github.com/yuehuca/schulich-cibc-acp-21/blob/main/buildconnectiongraph/2021-10-29_190552.png?raw=true)

