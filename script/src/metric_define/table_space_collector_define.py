# -*- coding: utf-8 -*-

table_space_collector_define = {
    "source": "V$TABLESPACE",
    "dim": ["NAME"],
    "metric": {
        "ID": {
            "metric_type": "gauge",
            "desc": "表空间 ID",
            "metric_name": "table_space_id",
            "data_type": "long"
        },
        "NAME": {
            "metric_type": "gauge",
            "desc": "表空间名称",
            "metric_name": "table_space_name",
            "data_type": "string",
        },
        "CACHE": {
            "metric_type": "gauge",
            "desc": "CACHE 名",
            "data_type": "string",
            "metric_name": "table_space_cache_name"
        },
        "TYPE": {
            "metric_type": "gauge",
            "desc": "表空间类型(1 DB 类型，2 临时表空间)",
            "data_type": "long",
            "metric_name": "table_space_type"
        },
        "STATUS": {
            "metric_type": "gauge",
            "desc": "状态(0 ONLINE，1 OFFLINE，2 RES_OFFLINE 3 CORRUPT)",
            "metric_name": "table_space_status",
            "data_type": "long",
        },
        "MAX_SIZE": {
            "metric_type": "gauge",
            "desc": "最大大小(0 代表只受操作系统限制)",
            "metric_name": "table_space_max_size",
            "data_type": "long",
        },
        "TOTAL_SIZE": {
            "metric_type": "gauge",
            "desc": "总大小(以页为单位)",
            "metric_name": "table_space_total_size",
            "data_type": "long",
        },
        "FILE_NUM": {
            "metric_type": "gauge",
            "desc": "包含的文件数",
            "data_type": "long",
            "metric_name": "table_space_file_num"
        },
        "ENCRYPT_NAME": {
            "metric_type": "gauge",
            "desc": "加密算法名",
            "metric_name": "table_space_encrypt_name",
            "data_type": "string",
        },
        "ENCRYPTED_KEY": {
            "metric_type": "gauge",
            "desc": "加密密钥(16 进制)",
            "data_type": "string",
            "metric_name": "table_space_encrypt_key"
        },
    },
    "row_header": ["ID", "NAME", "CACHE", "TYPE", "STATUS", "MAX_SIZE", "TOTAL_SIZE", "FILE_NUM", "ENCRYPT_NAME",
                   "ENCRYPTED_KEY"]
}
