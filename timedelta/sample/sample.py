from datetime import datetime as dt

def time_delta(t1, t2):
    format_time='%a,%d,%b,%Y,%H:%M:%S,%z'
    t1tm = dt.strptime(t1,format_time)
    t2tm = dt.strptime(t2,format_time)
    return str(round(abs((t1tm-t2tm).total_seconds())))