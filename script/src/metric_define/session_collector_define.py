# -*- coding: utf-8 -*-

session_collector_define = {
    "row_header": ["SESS_ID", "SESS_SEQ", "STATE", "CURR_SCH", "USER_NAME", "TRX_ID", "CREATE_TIME",
                   "CLNT_TYPE", "CLNT_HOST", "CLNT_IP"],
    "dim": ["SESS_SEQ"],
    "source": "V$SESSIONS",
    "metric": {
        "SESS_ID": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "会话 ID",
            "metric_name": "sess_id"
        },
        "SESS_SEQ": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "会话序列号，用来唯一标识会话",
            "metric_name": "sess_seq"
        },
        "STATE": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "会话状态。共 6 种状态:CREATE 创建、STARTUP 启动、 IDLE 空闲、ACTIVE 活动、WAIT 等待、UNKNOWN 未知",
            "metric_name": "sess_state"
        },
        "CURR_SCH": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "当前模式",
            "metric_name": "sess_curr_sch"
        },
        "USER_NAME": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "当前用户",
            "metric_name": "sess_user_name"
        },
        "TRX_ID": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "事务 id",
            "metric_name": "sess_trx_id"
        },
        "CREATE_TIME": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "会话创建时间",
            "metric_name": "sess_create_time",
        },
        "CLNT_TYPE": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "客户端类型",
            "metric_name": "sess_client_type"
        },
        "CLNT_HOST": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "客户端主机名",
            "metric_name": "sess_client_host"
        },
        "CLNT_IP": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "客户端 IP",
            "metric_name": "sess_client_ip"
        },
    },
}