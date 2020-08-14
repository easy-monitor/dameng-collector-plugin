# -*- coding: utf-8 -*-

threads_collector_define = {
    "row_header": ["ID", "NAME", "START_TIME", "THREAD_DESC"],
    "dim": ["NAME"],
    "source": "V$THREADS",
    "metric": {
        "ID": {
            "data_type": "string",
            "desc": "线程 ID",
            "metric_name": "thread_id",
            "metric_type": "gauge",
        },
        "NAME": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "线程名",
            "metric_name": "thread_name"
        },
        "START_TIME": {
            "data_type": "long",
            "desc": "线程开始时间",
            "metric_name": "thread_time",
            "type": "time",
            "metric_type": "gauge",
        },
        "THREAD_DESC": {
            "data_type": "string",
            "desc": "线程描述",
            "metric_name": "thread_desc",
            "metric_type": "gauge",
        },
    },
}