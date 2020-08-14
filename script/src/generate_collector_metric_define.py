# -*- coding: utf-8 -*-

import json
from metric_define import check_list

agent_type = "easyops"


def get_metric_define():
    metric_list = []
    for item in check_list:
        tags = []
        for dim in item["dim"]:
            dim_define = item["metric"].pop(dim, None)
            if dim_define:
                tags.append(
                    {
                        "name": dim,
                        "default": "",
                        "readOnly": True,
                        "description": dim_define["desc"]
                    }
                )

        for name, metric_define in item["metric"].iteritems():
            metric = {}
            metric['name'] = metric_define["metric_name"]
            metric['key'] = metric_define["metric_name"]
            metric['agentType'] = agent_type
            metric['tagDefine'] = tags
            metric['data_type'] = metric_define["data_type"]
            metric['metric_type'] = metric_define["metric_type"]
            metric['unit'] = metric_define.get("unit", "")
            metric_list.append(metric)
    return metric_list


if __name__ == "__main__":
    with open("./origin_metric.json", "w") as origin_metric_file:
        origin_metric_file.write(json.dumps(get_metric_define(), indent=4))

