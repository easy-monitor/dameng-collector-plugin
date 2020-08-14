# -*- coding: utf-8 -*-

connect_collector_define = {
    "row_header": ["NAME", "SADDR", "CREATE_TIME", "STATUS", "TYPE", "PROTOCOL_TYPE", "IP_ADDR"],
    "metric": {
        "NAME": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "连接名称",
            "metric_name": "connect_name"
        },
        "SADDR": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "会话地址",
            "metric_name": "connect_saddr"
        },
        "CREATE_TIME": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "会话创建时间",
            "metric_name": "connect_create_time",
            "type": "time"
        },
        "STATUS": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "连接状态",
            "metric_name": "connect_status"
        },
        "TYPE": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "连接类型",
            "metric_name": "connect_type"
        },
        "PROTOCOL_TYPE": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "协议类型",
            "metric_name": "connect_protocol_type"
        },
        "IP_ADDR": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "IP 地址",
            "metric_name": "connect_ip_addr"
        },
    },
    "dim": ["NAME"],
    "source": "V$CONNECT",
}