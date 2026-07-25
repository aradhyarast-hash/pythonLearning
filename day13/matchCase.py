def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "not found"
        case 500:
            return "Internal server error"
        # default case
        case _:
            return "unknown status"
        
print(http_status(5009))

