def extract_string_details(phrase):
    details = {
        'first_6': phrase[0:6],
        'last_9': phrase[-9:],
        'slice_13_38': phrase[13:38],
        'reversed': phrase[::-1],
    }
    return details
