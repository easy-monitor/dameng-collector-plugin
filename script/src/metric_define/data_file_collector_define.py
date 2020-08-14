# -*- coding: utf-8 -*-

data_file_collector_define = {
    "row_header": ["FILE_NAME", "FILE_ID", "TABLESPACE_NAME", "BYTES", "BLOCKS", "STATUS", "RELATIVE_FNO",
                   "AUTOEXTENSIBLE", "MAXBYTES", "MAXBLOCKS", "INCREMENT_BY", "USER_BYTES", "USER_BLOCKS",
                   "ONLINE_STATUS"],
    "metric": {
        "FILE_NAME": {
            "desc": "数据文件名称",
            "data_type": "string",
            "metric_type": "gauge",
            "metric_name": "data_file_name"
        },
        "FILE_ID": {
            "desc": "数据文件所属文件id",
            "data_type": "string",
            "metric_type": "gauge",
            "metric_name": "data_file_id"
        },
        "TABLESPACE_NAME": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "数据文件所属表空间名",
            "metric_name": "tablespace_name"
        },
        "BYTES": {
            "metric_type": "gauge",
            "desc": "数据文件大小",
            "data_type": "long",
            "unit": "byte",
            "metric_name": "data_file_size"
        },
        "BLOCKS": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "数据文件块大小",
            "metric_name": "data_file_block_size"
        },
        "STATUS": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "数据文件状态(AVAILABLE 可用，INVALID 不可用)",
            "metric_name": "data_file_status"
        },
        "RELATIVE_FNO": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "所在表空间的数据文件个数",
            "metric_name": "data_file_relative_fno"
        },
        "AUTOEXTENSIBLE": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "是否可自动扩展",
            "metric_name": "is_auto_extensible"
        },
        "MAXBYTES": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "最大数据文件大小",
            "unit": "byte",
            "metric_name": "data_file_max_size"
        },
        "MAXBLOCKS": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "最大数据文件块大小",
            "metric_name": "data_file_max_block_size"
        },
        "INCREMENT_BY": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "可用于自动扩展的数据块数量",
            "metric_name": "data_file_increment_by"
        },
        "USER_BYTES": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "用户数据可使用的文件大小",
            "metric_name": "data_file_user_byte"
        },
        "USER_BLOCKS": {
            "data_type": "long",
            "metric_type": "gauge",
            "desc": "数据可使用的块数量",
            "metric_name": "data_file_user_block"
        },
        "ONLINE_STATUS": {
            "data_type": "string",
            "metric_type": "gauge",
            "desc": "文件状态(SYSOFF/SYSTEM/OFFLINE/ONLINE/RECOVER",
            "metric_name": "data_file_online_status"
        },
    },
    "dim": ["FILE_NAME"],
    "source": "dba_data_files",
}