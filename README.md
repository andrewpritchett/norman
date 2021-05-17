# Norman for normalizing
Let Norman help you with JSON normalization!

```
usage: norman.py [-h] [-p PATH] [-d DATA] [-c CSV]

Let Norman help you with JSON normalization!

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to your raw log json input file
  -d DATA, --data DATA  raw log json data
  -c CSV, --csv CSV     output path for csv file
```

**Install:**
```
$ python setup.py install
```

**Example 1:**
```
$ norman -p /path/to/input/file.json
```

**Example 2:**
```
$ norman -p /path/to/input/file.json -c /path/to/output/file.csv
```

**Example 3:**
```
$ norman -d '{"order": 1, "settings": {"index": {"mapping": {"total_fields": {"limit": 10000}},"refresh_interval": "5s"}}}' -c /path/to/output/file.csv
```

**Example Terminal Output:**
```
order : int : 1
settings.index.mapping.total_fields.limit : int : 10000
settings.index.refresh_interval : str : 5s
```

**Example File Output:**
output_file.csv:
```
path,type,sample_value
order,int,1
settings.index.mapping.total_fields.limit,int,10000
settings.index.refresh_interval,str,5s
```