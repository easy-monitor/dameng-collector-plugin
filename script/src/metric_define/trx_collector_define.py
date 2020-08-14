# -*- coding: utf-8 -*-

trx_collector_define = {
    "row_header": ["ID", "NEXTID", "STATUS", "ISOLATION", "SESS_ID", "SESS_SEQ", "XID"],
    "dim": ["ID"],
    "source": "V$TRX",
    "metric": {
        "ID": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "当前活动事务的 ID 号",
            "metric_name": "trx_id"
        },
        "NEXTID": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "下一个事务 ID 号",
            "metric_name": "next_trx_id"
        },
        "STATUS": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "当前事务的状态",
            "metric_name": "trx_status"
        },
        "ISOLATION": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "隔离级。0:读未提交;1:读提交;2:可重复读;3:串 行化",
            "metric_name": "trx_isolation_level"
        },
        "SESS_ID": {
            "data_type": "long",
            "desc": "当前事务的所在会话",
            "metric_type": "gauge",
            "metric_name": "trx_session_id"
        },
        "SESS_SEQ": {
            "data_type": "string",
            "desc": "会话序列号，用来唯一标识会话",
            "metric_type": "gauge",
            "metric_name": "trx_session_seq"
        },
        "XID": {
            "data_type": "string",
            "desc": "XA 事务唯一标识",
            "metric_name": "trx_xid",
            "metric_type": "gauge",
        }
    },
}