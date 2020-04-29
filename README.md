YamlWalker introduction
-----------------------
Provide comfortable interface for operate yaml data

Containing 2 main features:
* `YQuery`
* `YamlDict`

**YQuery**

Allow querying of Yaml file in `Xpath` look alike style

**YamlDict**

Allow operate yamll data with dot notation style with extention 
to query list items by property value

**Installation**

*From PIP*

[Link to PYPI] (https://pypi.org/project/YamlWalker/)

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
        value: asfasf
      - id: 2
        name: node2
        type: str
        value: 23wefqrq
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

# YamlDict example
yaml_dict = yaml_data.node.hd_1.data['id>0']


# YQuery example
yquery = YQuery('yaml_data.node.hd_1.data[id>0]')
yaml_query = yquery(yaml_data)

"""Result: {
            id: 2
            name: node2
            type: str
            value: 23wefqrq
            sub_data:
              item: any
              value: four
        }"""
```

