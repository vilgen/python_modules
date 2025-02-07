class Athlete:    
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])
    
    def add_time(self, time_value):
        self.times.append(time_value)
    
    def add_times(self, list_of_times):
        self.times.extend(list_of_times)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

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
            temp = data.strip().split(",")
        return (Athlete(temp.pop(0), temp.pop(0), temp))
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return None

def main():
    sarah = get_coach_data("sarah2.txt")
    print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

    vera = AthleteList("Vera Vi")
    vera.append("1.31")
    vera.extend(["1-29", "1.32"])
    print(vera.top3())

if __name__ == "__main__":
    main()