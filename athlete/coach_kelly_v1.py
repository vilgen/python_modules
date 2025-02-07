def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(",")
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return None

def main():
    clean_jule_data = []
    clean_james_data = []
    clean_sarah_data = []
    clean_mikey_data = []

    jule_data = get_coach_data("jule.txt")
    james_data = get_coach_data("james.txt")
    sarah_data = get_coach_data("sarah.txt")
    mikey_data = get_coach_data("mikey.txt")

    clean_james_data = sorted(set([sanitize(each_time) for each_time in james_data]))[0:3]
    clean_sarah_data = sorted(set([sanitize(each_time) for each_time in sarah_data]))[0:3]
    clean_mikey_data = sorted(set([sanitize(each_time) for each_time in mikey_data]))[0:3]
    clean_jule_data = sorted(set([sanitize(each_time) for each_time in jule_data]))[0:3]
    
    print(clean_jule_data)
    print(clean_james_data)
    print(clean_sarah_data)
    print(clean_mikey_data)

if __name__ == "__main__":
    main()