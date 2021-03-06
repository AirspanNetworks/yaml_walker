YamlWalker introduction
-----------------------
Provide comfortable interface for operate yaml data

Containing 2 main features:
* `YPath`
* `YDict`

**YPath**

Allow querying of Yaml file in `Xpath/XQuery` look alike style
Comfortable when path sub elements not pre-defined

**YDict**

Allow operate yaml data with dot notation style with extension 
to Ypath list items by property value
Suitable when path to desired sub element are static or well known

**Installation**

*From PIP*

[Link to PYPI] (https://pypi.org/project/yaml_walker/)

~~~
pip.exe install YamlWalker
~~~

*From GitHub*

[Lint to GiHub] (https://github.com/doguz2509/YamlWalker)

## Usage
```
file.yaml
---
node:
  nd_1:
    data:
      - id: 0
        name: node1
        type: str
        value: any value
      - id: 2
        name: node2
        type: str
        value: any str
        sub_data:
          item: any
          value: four
```
```
python

import yaml
from yaml_walker import api

with open(file.yaml) as fr:
    yaml_data = yaml.load(fr)

# YDict example
yaml_dict = api.YDict(yaml_data)
yaml_result = yaml_dict.node.hd_1.data['id>0']

# YQuery example
y_query = api.YPath('yaml_data.node.hd_1.data[id>0]')
yaml_result = y_query(yaml_data)
```
```
shell script

python -m yaml_walker 'yaml_data.node.hd_1.data[id>0]' file.yaml

```
```
Result in all cases: 
    {
        id: 2
        name: node2
        type: str
        value: any str
        sub_data:
          item: any
          value: four
    }
```
