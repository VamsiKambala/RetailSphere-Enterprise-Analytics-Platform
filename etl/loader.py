
def infer_mysql_type(dtype)->str:

    dtype=str(dtype)
    if "int" in dtype:
        return "INT"
    elif "bool" in dtype:
        return "BOOLEAN"
    elif "datetime" in dtype:
        return "DATETIME"
    elif "float" in dtype:
        return "DOUBLE"
    else:
        return "VARCHAR(255)"