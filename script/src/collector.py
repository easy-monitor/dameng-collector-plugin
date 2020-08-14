# -*- coding: utf-8 -*-

import time
import copy
import json
import os
import logging
import logging.handlers
import traceback

from metric_define import check_list

import dmPython


metric_data = {
    "dims": {},
    "vals": {}
}

sql_template = "select * from {}"
host = os.environ.get("EASYOPS_COLLECTOR_host")
port = os.environ.get("EASYOPS_COLLECTOR_port")
user = os.environ.get("EASYOPS_COLLECTOR_user")
password = os.environ.get("EASYOPS_COLLECTOR_password")


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file_path = os.path.join(BASE_PATH, "log")
if not os.path.exists(log_file_path):
    os.mkdir(log_file_path)


def log_setup():
    log_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_file_path, 'dm_collector.log'),
        maxBytes=20000000,
        backupCount=5
    )

    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)


class DMCollector:
    SHOW_SQL = True

    def __init__(self, host='127.0.0.1', port=5236, user='SYSDBA', password='SYSDBA'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = None

    def get_con(self):
        try:
            if not self.conn:
                self.conn = dmPython.connect(user=self.user, password=self.password, server=self.host, port=self.port,
                                             autoCommit=True)
            return self.conn
        except dmPython.Error, e:
            print "dmPython Error:%s" % e

    def select_all(self, sql):
        try:
            con = self.get_con()
            # print con
            cur = con.cursor()
            cur.execute(sql)
            fc = cur.fetchall()
            cur.close()
            return fc
        except dmPython.Error, e:
            print "dmPython Error:%s" % e

    def parser_output(self, metric_define, raw_rows):
        row_data = []
        for row in raw_rows:
            row_data.append(zip(metric_define["row_header"], row))

        output = []
        for row in row_data:
            one_data = copy.deepcopy(metric_data)
            for one_tuple in row:
                key, val = one_tuple
                if val is None:
                    continue
                if key in metric_define["dim"]:
                    one_data["dims"][metric_define["metric"][key]["metric_name"]] = str(val)
                    continue

                if metric_define["metric"][key].get("type") == "time":
                    val = time.mktime(val.timetuple())
                if metric_define["metric"][key].get("data_type") == "long":
                    val = int(val)
                one_data['vals'][metric_define["metric"][key]["metric_name"]] = val
            output.append(one_data)
        return output

    def get_data(self, collector_detail):
        sql = sql_template.format(collector_detail['source'])
        rows = db.select_all(sql)
        return self.parser_output(collector_detail, rows)

    def check(self):
        join_list = []
        for item in check_list:
            try:
                join_list.extend(self.get_data(item))
            except Exception as e:
                logging.error("get data with %s error, msg: %s", item, e.message)
                logging.error(traceback.format_exc())
        return join_list

    def close_con(self):
        if not self.conn:
            self.conn.close()

if __name__ == "__main__":
    log_setup()
    try:
        db = DMCollector(host, port, user, password)
        db.get_con()
        res = db.check()
        db.close_con()
        print json.dumps(res)
    except Exception as e:
        logging.error("collect return error, msg=%s", e.message)
        logging.error(traceback.format_exc())
