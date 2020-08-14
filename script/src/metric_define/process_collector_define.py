# -*- coding: utf-8 -*-

process_collector_define = {
    "row_header": ["PID", "PNAME", "TRACE_NAME", "TYPE"],
    "dim": ["PNAME"],
    "source": "V$PROCESS",
    "metric": {
        "PID": {
            "data_type": "long",
            "desc": "进程 ID",
            "metric_type": "gauge",
            "metric_name": "pid"
        },
        "PNAME": {
            "data_type": "string",
            "desc": "进程名",
            "metric_type": "gauge",
            "metric_name": "pname"
        },
        "TRACE_NAME": {
            "data_type": "string",
            "desc": "SQL 日志路径",
            "metric_type": "gauge",
            "metric_name": "trace_name"
        },
        "TYPE": {
            "data_type": "long",
            "desc": "类型",
            "metric_name": "ptype",
            "metric_type": "gauge",

        },
    },
}